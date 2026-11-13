#!/usr/bin/env python3
"""Spark works twelve arcade games out, one after another, with nobody testing in between.

    python3 -I run_arcade.py                      every game in games.tsv, three stages each
    options: --only 03,05   --model spark-x2.6-4b   --work-minutes 20   --rest-seconds 15   (or pace.txt: "20 15", read live)
             --pause 5 (seconds between requests)   --force (redo finished stages)

Per game (out/<id>_<Title>/): 1_concept.md, 2_levels.md, 3_script.livecodescript (+ 3_script.raw.md
when the answer was more than one code block). Finished stages are skipped, so stopping and
starting again is safe. Every request is timed in out/_timings.tsv (LIB_SPARK keeps the record
of gains and time frames). Work/rest: after --work-minutes it pauses for --rest-seconds
(the model is unloaded only for rests of two minutes or more). If LM Studio is not answering the runner waits and
tries again every minute; it does not give up.

Spark runs in LM Studio on Windows (port 1234), reached through Windows' curl.exe.
"""
import argparse, json, os, re, subprocess, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'out')
URL = 'http://127.0.0.1:1234/v1/chat/completions'
WORK_START = [time.time()]


def log(msg):
    line = '%s  %s' % (time.strftime('%H:%M:%S'), msg)
    print(line, flush=True)
    with open(os.path.join(OUT, '_run.log'), 'a', encoding='utf-8') as f:
        f.write(line + '\n')


def prompts():
    text = open(os.path.join(HERE, 'arcade_prompt.md'), encoding='utf-8').read()
    parts = re.split(r'^## (SYSTEM|CONCEPT|LEVELS|SCRIPT)\s*$', text, flags=re.M)
    return {parts[i]: parts[i + 1].strip() for i in range(1, len(parts), 2)}


def fill(template, **values):
    # one pass, so braces inside a filled-in value (Spark's own text, the example) are left alone
    return re.sub(r'\{(\w+)\}', lambda m: str(values.get(m.group(1), m.group(0))), template)


def games():
    out = []
    for line in open(os.path.join(HERE, 'games.tsv'), encoding='utf-8'):
        if line.strip() and not line.startswith('#'):
            f = line.rstrip('\n').split('\t')
            out.append(dict(id=f[0], title=f[1], prefix=f[2], brief=f[3], columns=f[4], legend=f[5]))
    return out


def lms(*args):
    try:
        home = subprocess.run(['cmd.exe', '/c', 'echo %USERPROFILE%'], capture_output=True, text=True,
                              cwd='/mnt/c').stdout.strip()
        exe = subprocess.run(['wslpath', home], capture_output=True, text=True).stdout.strip() \
            + '/.cache/lm-studio/bin/lms.exe'
        r = subprocess.run([exe] + list(args), capture_output=True, text=True, cwd='/mnt/c', timeout=300)
        return re.sub(r'\x1b\[[0-9;]*m', '', r.stdout + r.stderr)
    except Exception as e:
        return str(e)


def load(model):
    lms('server', 'start', '--port', '1234')
    if not re.search(r'^%s\s' % re.escape(model), lms('ps'), flags=re.M):
        log('loading %s (about 3.5 GB)...' % model)
        lms('load', model, '--identifier', model, '--context-length', '8192', '--parallel', '1',
            '--ttl', '900', '--yes')


def chat(model, system, user, max_tokens):
    """-> (text, finish_reason, usage dict, seconds). Waits and retries while LM Studio is away."""
    body = {'model': model, 'temperature': 0.3, 'max_tokens': max_tokens, 'reasoning_effort': 'none',
            'messages': [{'role': 'system', 'content': system}, {'role': 'user', 'content': user}]}
    tries = 0
    while True:
        t0 = time.time()
        r = subprocess.run(['curl.exe', '-sS', '-m', '1500', URL, '-H', 'Content-Type: application/json',
                            '--data-binary', '@-'], input=json.dumps(body).encode('utf-8'),
                           capture_output=True, cwd='/mnt/c')
        secs = time.time() - t0
        try:
            d = json.loads(r.stdout.decode('utf-8', 'replace'))
            c = d['choices'][0]
            text = re.sub(r'<think>.*?</think>', '', c['message'].get('content') or '', flags=re.S).strip()
            return text, c.get('finish_reason'), d.get('usage') or {}, secs
        except Exception:
            tries += 1
            why = (r.stderr.decode(errors='replace').strip() or r.stdout.decode(errors='replace')[:200]).strip()
            log('  LM Studio did not answer (%s); try %d, waiting 60 s' % (why[:160], tries))
            time.sleep(60)
            load(model)


def pace(a):
    """(work minutes, rest seconds): from pace.txt when it is there (two numbers; read before every
    request, so the owner can change the pace of a running job), else from the command line"""
    try:
        w, r = open(os.path.join(HERE, 'pace.txt')).read().split()[:2]
        return float(w), float(r)
    except Exception:
        return a.work_minutes, a.rest_seconds


def breathe(a):
    work, rest = pace(a)
    if work <= 0 or time.time() - WORK_START[0] < work * 60:
        return
    if rest >= 120:
        log('RESTING %g s (model unloaded, RAM and heat come down)' % rest)
        lms('unload', a.model)
        time.sleep(rest)
        load(a.model)
    else:
        log('RESTING %g s' % rest)
        time.sleep(rest)
    log('back to work')
    WORK_START[0] = time.time()


def code_of(text):
    """the code of an answer: the longest fenced block, or the whole text when there is no fence"""
    blocks = re.findall(r'```[^\n]*\n(.*?)(?:```|\Z)', text, flags=re.S)
    return (max(blocks, key=len) if blocks else text).strip() + '\n'


def stage(a, g, folder, name, system, user, max_tokens):
    path = os.path.join(folder, name)
    if os.path.exists(path) and not a.force:
        return open(path, encoding='utf-8').read()
    breathe(a)
    log('%s %s: %s ...' % (g['id'], g['title'], name))
    text, finish, usage, secs = chat(a.model, system, user, max_tokens)
    cut = finish == 'length'
    if name.endswith('.livecodescript'):
        open(os.path.join(folder, '3_script.raw.md'), 'w', encoding='utf-8').write(text + '\n')
        text = code_of(text)
    open(path, 'w', encoding='utf-8').write(text if text.endswith('\n') else text + '\n')
    out_tok = usage.get('completion_tokens', 0)
    with open(os.path.join(OUT, '_timings.tsv'), 'a', encoding='utf-8') as f:
        f.write('\t'.join(str(x) for x in (
            time.strftime('%Y-%m-%d %H:%M:%S'), a.model, g['id'], g['title'], name,
            usage.get('prompt_tokens', ''), out_tok, '%.1f' % secs,
            '%.1f' % (out_tok / secs if secs else 0), len(text.splitlines()), 'CUT' if cut else 'ok')) + '\n')
    log('  %s: %d lines, %s tokens out in %.0f s%s' % (name, len(text.splitlines()), out_tok, secs,
                                                    '  ** CUT OFF at max_tokens **' if cut else ''))
    time.sleep(a.pause)
    return text


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--only', default='', help='comma list of game ids, e.g. 03,05')
    ap.add_argument('--model', default='spark-x2.6-4b')
    ap.add_argument('--work-minutes', type=float, default=20)
    ap.add_argument('--rest-seconds', type=float, default=15)
    ap.add_argument('--pause', type=float, default=5)
    ap.add_argument('--force', action='store_true')
    a = ap.parse_args()
    os.makedirs(OUT, exist_ok=True)
    tim = os.path.join(OUT, '_timings.tsv')
    if not os.path.exists(tim):
        open(tim, 'w').write('when\tmodel\tid\ttitle\tstage\ttokens_in\ttokens_out\tseconds\ttok_per_s\tlines\tfinish\n')
    p = prompts()
    example = open(os.path.join(HERE, 'example_Catch.livecodescript'), encoding='utf-8').read().strip()
    only = [x.strip() for x in a.only.split(',') if x.strip()]
    todo = [g for g in games() if not only or g['id'] in only]
    log('=== start: %d games, work %g min / rest %g s, model %s' % ((len(todo),) + pace(a) + (a.model,)))
    load(a.model)
    WORK_START[0] = time.time()
    for g in todo:
        folder = os.path.join(OUT, '%s_%s' % (g['id'], g['title'].replace(' ', '_')))
        os.makedirs(folder, exist_ok=True)
        concept = stage(a, g, folder, '1_concept.md', p['SYSTEM'], fill(p['CONCEPT'], **g), 700)
        levels = stage(a, g, folder, '2_levels.md', p['SYSTEM'],
                       fill(p['LEVELS'], concept=concept[:2600], **g), 900)
        stage(a, g, folder, '3_script.livecodescript', p['SYSTEM'],
              fill(p['SCRIPT'], concept=concept[:2600], levels=levels[:2400], example=example, **g), 3600)
    log('=== done: every game has its three files. Claude reviews next.')


if __name__ == '__main__':
    main()

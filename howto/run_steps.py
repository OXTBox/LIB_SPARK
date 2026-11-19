#!/usr/bin/env python3
"""Spark writes the WORDS of each LIB_HOWTO step; Claude has already written and tested the code.

    python3 -I run_steps.py                 every topic folder in ../../LIB_HOWTO/topics with step code
    options: --only 01,02   --force   --model spark-x2.6-4b

For each LIB_HOWTO/topics/<id>_<Title>/step_<n>.livecodescript without a step_<n>.txt, Spark gets
the step's lines from OUTLINE.md (the approved outline) and the step's code, and writes
step_<n>.txt: Title / Makes this happen / Look for. Spark never writes or changes code.
Prompt: the STEP section of steps_prompt.md. LM Studio + timings: ../arcade/run_arcade.py.
"""
import argparse, glob, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'arcade'))
import run_arcade as ra                                           # noqa: E402

OUT = os.path.join(HERE, 'out')
ra.OUT = OUT
TOPICS = os.path.join(HERE, '..', '..', 'LIB_HOWTO', 'topics')


def prompts():
    text = open(os.path.join(HERE, 'steps_prompt.md'), encoding='utf-8').read()
    parts = re.split(r'^## (SYSTEM|STEP)\s*$', text, flags=re.M)
    return {parts[i]: parts[i + 1].strip() for i in range(1, len(parts), 2)}


def outline_steps(tid):
    """-> (topic title, goal, {n: the step's outline lines})"""
    text = open(os.path.join(HERE, 'OUTLINE.md'), encoding='utf-8').read()
    m = re.search(r'^# %s (.+?)\n(.*?)(?=^---|\Z)' % re.escape(tid), text, flags=re.M | re.S)
    if not m:
        return '', '', {}
    title, body = m.group(1).strip(), m.group(2)
    goal = (re.search(r'^Goal: (.+)$', body, flags=re.M) or [None, ''])[1]
    steps = {}
    for s in re.finditer(r'^(\d+)\. (.+?)(?=^\d+\. |^Pitfalls:|\Z)', body, flags=re.M | re.S):
        steps[int(s.group(1))] = (s.group(1) + '. ' + s.group(2)).rstrip()
    return title, goal, steps


def clean(text):
    keep = []
    for line in text.splitlines():
        if re.match(r'^(Title|Makes this happen|Look for):', line):
            keep.append(line.strip())
    return '\n'.join(keep) + '\n' if len(keep) == 3 else ''


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--only', default='')
    ap.add_argument('--force', action='store_true')
    ap.add_argument('--model', default='spark-x2.6-4b')
    a = ap.parse_args()
    p = prompts()
    only = [x for x in a.only.split(',') if x]
    todo = []
    for d in sorted(glob.glob(os.path.join(TOPICS, '[0-9][0-9]_*'))):
        tid = os.path.basename(d)[:2]
        if only and tid not in only:
            continue
        for code in sorted(glob.glob(os.path.join(d, 'step_*.livecodescript'))):
            words = code[:-len('.livecodescript')] + '.txt'
            if a.force or not os.path.exists(words):
                todo.append((tid, int(re.search(r'step_(\d+)', code).group(1)), code, words))
    ra.log('=== LIB_HOWTO step words: %d steps, model %s' % (len(todo), a.model))
    if not todo:
        return
    ra.load(a.model)
    for tid, n, code, words in todo:
        title, goal, steps = outline_steps(tid)
        user = p['STEP'].format(id=tid, title=title, goal=goal, n=n, total=len(steps),
                                outline=steps.get(n, '(not in the outline)'),
                                code=open(code, encoding='utf-8').read())
        for attempt in (1, 2):
            text, finish, usage, secs = ra.chat(a.model, p['SYSTEM'], user, 400)
            out = clean(text)
            ra.log('  %s step %d: %.0f s, %s%s' % (tid, n, secs, finish, '' if out else ' (bad format)'))
            if out:
                break
        if out:
            with open(words, 'w', encoding='utf-8') as f:
                f.write(out)


if __name__ == '__main__':
    main()

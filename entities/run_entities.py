#!/usr/bin/env python3
"""run_entities.py - Spark designs procedural entities as RECIPES (words and numbers, never code).

    python3 -I entities/run_entities.py [--only 01,05] [--force] [--model spark-x2.6-4b]

For every row of entities.tsv (id, name, game, brief, size) Spark writes a recipe
(entity_prompt.md, the boat as its example). entity.py checks it; if the check fails, the report
goes back to Spark ONCE for a retry. Into out/<id>_<Name>/:
    1_recipe.txt     Spark's first recipe          1_check.txt   entity.py's report and views
    2_recipe.txt     the retry (only when needed)  2_check.txt
    recipe.txt       the one that passed (or the last try)
    mesh.livecodescript   the Vibecode3D function, written by entity.py (only when it passed)
Done entities are skipped. Spark's pace and rests are shared with the arcade runner (pace.txt
and the work clock in arcade/out/.work_clock): one Spark, one rest schedule.
"""
import argparse, json, os, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(os.path.dirname(HERE), 'arcade'))
import entity        # noqa: E402
import run_arcade    # noqa: E402  chat, load, breathe, the shared work clock

OUT = os.path.join(HERE, 'out')
ARCADE_LOCK = os.path.join(os.path.dirname(HERE), 'arcade', 'out', '.running')


def prompts():
    text = open(os.path.join(HERE, 'entity_prompt.md'), encoding='utf-8').read()
    parts, cur = {}, None
    for line in text.split('\n'):
        if line.startswith('## '):
            cur = line[3:].strip()
            parts[cur] = []
        elif cur:
            parts[cur].append(line)
    return {k: '\n'.join(v).strip() for k, v in parts.items()}


def queue():
    rows = []
    for line in open(os.path.join(HERE, 'entities.tsv'), encoding='utf-8'):
        if line.startswith('#') or not line.strip():
            continue
        f = line.rstrip('\n').split('\t')
        if len(f) >= 5:
            rows.append(dict(id=f[0], name=f[1], game=f[2], brief=f[3], size=f[4]))
    return rows


def recipe_of(text):
    """the recipe part of an answer (drops a code fence or chatter before ENTITY:)"""
    text = text.replace('```', '')
    i = text.find('ENTITY:')
    return (text[i:] if i >= 0 else text).strip() + '\n'


def ask(a, system, user, tag):
    run_arcade.breathe(a)
    run_arcade.log('%s ...' % tag)
    text, finish, usage, secs = run_arcade.chat(a.model, system, user, 1100)
    toks = usage.get('completion_tokens', 0)
    run_arcade.log('   %d tokens out in %.0f s%s' % (toks, secs, '  ** CUT OFF **' if finish == 'length' else ''))
    with open(os.path.join(OUT, '_timings.tsv'), 'a', encoding='utf-8') as f:
        f.write('%s\t%s\t%s\t%d\t%.1f\t%.1f\t%s\n' % (time.strftime('%Y-%m-%d %H:%M:%S'), a.model, tag, toks, secs,
                                                    toks / secs if secs else 0, finish))
    return recipe_of(text)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--only', default='')
    ap.add_argument('--force', action='store_true')
    ap.add_argument('--model', default='spark-x2.6-4b')
    ap.add_argument('--work-minutes', type=float, default=10)
    ap.add_argument('--rest-seconds', type=float, default=900)
    a = ap.parse_args()
    os.makedirs(OUT, exist_ok=True)
    try:
        pid = int(open(ARCADE_LOCK).read().strip())
        os.kill(pid, 0)
        print('the arcade runner is using Spark (process %d); start this when it is done' % pid)
        return 1
    except (OSError, ValueError):
        pass
    run_arcade.OUT = OUT                     # log into entities/out/_run.log (the clock stays shared)
    p = prompts()
    only = [x.strip() for x in a.only.split(',') if x.strip()]
    todo = [g for g in queue() if not only or g['id'] in only]
    run_arcade.log('=== start: %d entities, model %s' % (len(todo), a.model))
    run_arcade.load(a.model)
    run_arcade.WORK_START[0] = run_arcade.resume_clock(a)
    passed = 0
    for g in todo:
        folder = os.path.join(OUT, '%s_%s' % (g['id'], entity.lc_name(g['name'])))
        final = os.path.join(folder, 'recipe.txt')
        if os.path.exists(final) and not a.force:
            continue
        os.makedirs(folder, exist_ok=True)
        recipe = ask(a, p['SYSTEM'], run_arcade.fill(p['RECIPE'], **g), '%s %s: recipe' % (g['id'], g['name']))
        for attempt in (1, 2):
            open(os.path.join(folder, '%d_recipe.txt' % attempt), 'w', encoding='utf-8').write(recipe)
            rep, ok, whole = entity.check(recipe)
            views = entity.view(whole, (0, 2), title='top (front up the page)') + '\n' + \
                entity.view(whole, (2, 1), title='side (front to the right)')
            open(os.path.join(folder, '%d_check.txt' % attempt), 'w', encoding='utf-8').write(
                '%s\n%s\n\n%s\n' % ('OK' if ok else 'FAULTS', '\n'.join(rep), views))
            run_arcade.log('   try %d: %s %s' % (attempt, 'OK' if ok else 'FAULTS',
                                                 '; '.join(r for r in rep if 'FAIL' in r)[:200]))
            if ok or attempt == 2:
                break
            faults = '\n'.join('- ' + r.split(':', 1)[-1].strip() if 'FAIL' in r else '' for r in rep).strip()
            recipe = ask(a, p['SYSTEM'], run_arcade.fill(p['RETRY'], recipe=recipe, faults=faults, **g),
                         '%s %s: retry' % (g['id'], g['name']))
        open(final, 'w', encoding='utf-8').write(recipe)
        if ok:
            passed += 1
            try:
                open(os.path.join(folder, 'mesh.livecodescript'), 'w', encoding='utf-8').write(entity.code(recipe)[0])
            except ValueError as e:
                run_arcade.log('   code: %s' % e)
    run_arcade.log('=== done: %d passed the check. Claude reviews next.' % passed)
    return 0


if __name__ == '__main__':
    sys.exit(main())

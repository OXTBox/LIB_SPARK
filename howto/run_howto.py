#!/usr/bin/env python3
"""Spark writes the big outline for LIB_HOWTO (step-by-step game programming tutorials).

    python3 -I run_howto.py                 every stage; finished files are skipped (safe to stop and restart)
    options: --only 01,15 (topic ids)   --skip-games   --assemble (just rebuild OUTLINE.md)   --force
             --model spark-x2.6-4b   --work-minutes 20   --rest-seconds 15   --pause 5   (or ../arcade/pace.txt)

Stages (prompts in howto_prompt.md; topics in topics.tsv; games in games.tsv):
  1. out/00_missing.md                 fundamentals Spark thinks topics.tsv is missing
  2. out/<id>_<Title>/outline.md       4-7 steps a topic: "Adding: X / Makes this happen: Y"
  3. out/games/<Game>.md               which 4 topics each existing game teaches best
  4. OUTLINE.md                        everything above in one file, for Claude and the owner to review
Spark writes words only, never code. LM Studio and the work/rest pace are handled by
../arcade/run_arcade.py (same model loading, retries, timings in out/_timings.tsv).
"""
import argparse, os, re, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'arcade'))
import run_arcade as ra                                           # noqa: E402

OUT = os.path.join(HERE, 'out')
ra.OUT = OUT                                                      # its log and timings go to howto/out


def prompts():
    text = open(os.path.join(HERE, 'howto_prompt.md'), encoding='utf-8').read()
    parts = re.split(r'^## (SYSTEM|OUTLINE|MISSING|GAME)\s*$', text, flags=re.M)
    return {parts[i]: parts[i + 1].strip() for i in range(1, len(parts), 2)}


def rows(name):
    out = []
    for line in open(os.path.join(HERE, name), encoding='utf-8'):
        if line.strip() and not line.startswith('#'):
            out.append(line.rstrip('\n').split('\t'))
    return out


def slug(s):
    return re.sub(r'[^A-Za-z0-9]+', '_', s).strip('_')


def assemble(topics, games):
    def read(p):
        return open(p, encoding='utf-8').read().strip() if os.path.exists(p) else '(not written yet)'
    out = ['# LIB_HOWTO: the big outline (Spark draft, %s)' % time.strftime('%Y-%m-%d %H:%M'), '',
           'Written by Spark (local model) from `LIB_SPARK/howto/` for Claude and the owner to review.',
           'Nothing here is code. "NEW:" marks a call Spark wanted that the engine does not have.', '',
           '## Topics (the left-side list)', '']
    out += ['%s. %s' % (t[0], t[1]) for t in topics]
    for t in topics:
        text = read(os.path.join(OUT, '%s_%s' % (t[0], slug(t[1])), 'outline.md'))
        # Spark sometimes answers, then starts "Wait, let me check the format..." and writes it all
        # again until it is cut off: keep the first answer (up to its "Games that show it" line)
        m = re.search(r'^Games that show it:.*$', text, flags=re.M)
        if m:
            text = text[:m.end()]
        out += ['', '---', '', text]
    out += ['', '---', '', '## Missing fundamentals (Spark\'s suggestions)', '',
            read(os.path.join(OUT, '00_missing.md')), '', '---', '', '## Which game teaches what', '']
    by_topic = {}
    for g in games:
        p = os.path.join(OUT, 'games', slug(g[0]) + '.md')
        if not os.path.exists(p):
            continue
        out.append('### %s' % g[0])
        seen = set()
        for line in read(p).splitlines():
            m = re.match(r'\s*-?\s*(\d+)\s*\|', line)           # only "<topic> | <title> | <why>" lines
            if not m or m.group(1).zfill(2) in seen or len(seen) >= 4:
                continue
            seen.add(m.group(1).zfill(2))
            out.append('- ' + line.strip().lstrip('- '))
            by_topic.setdefault(m.group(1).zfill(2), []).append(g[0])
        out.append('')
    out += ['## Games by topic', '']
    for t in topics:
        out.append('- %s %s: %s' % (t[0], t[1], ', '.join(by_topic.get(t[0], [])) or '-'))
    open(os.path.join(HERE, 'OUTLINE.md'), 'w', encoding='utf-8').write('\n'.join(out) + '\n')
    ra.log('OUTLINE.md written (%d topics, %d game maps)' % (len(topics), sum(
        os.path.exists(os.path.join(OUT, 'games', slug(g[0]) + '.md')) for g in games)))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--only', default='', help='comma list of topic ids, e.g. 01,15')
    ap.add_argument('--skip-games', action='store_true')
    ap.add_argument('--assemble', action='store_true', help='only rebuild OUTLINE.md from what is there')
    ap.add_argument('--model', default='spark-x2.6-4b')
    ap.add_argument('--work-minutes', type=float, default=20)
    ap.add_argument('--rest-seconds', type=float, default=15)
    ap.add_argument('--pause', type=float, default=5)
    ap.add_argument('--force', action='store_true')
    a = ap.parse_args()
    os.makedirs(os.path.join(OUT, 'games'), exist_ok=True)
    topics, games = rows('topics.tsv'), rows('games.tsv')
    if a.assemble:
        return assemble(topics, games)
    tim = os.path.join(OUT, '_timings.tsv')
    if not os.path.exists(tim):
        open(tim, 'w').write('when\tmodel\tid\ttitle\tstage\ttokens_in\ttokens_out\tseconds\ttok_per_s\tlines\tfinish\n')
    p = prompts()
    topic_list = '\n'.join('%s. %s: %s' % tuple(t[:3]) for t in topics)
    game_names = ', '.join(g[0] for g in games)
    only = [x.strip() for x in a.only.split(',') if x.strip()]
    todo = [t for t in topics if not only or t[0] in only]
    ra.log('=== LIB_HOWTO outline: %d topics, %d games, work %g min / rest %g s, model %s' % (
        (len(todo), 0 if a.skip_games else len(games)) + ra.pace(a) + (a.model,)))
    ra.load(a.model)
    ra.WORK_START[0] = time.time()
    if not only:
        ra.stage(a, {'id': '00', 'title': 'missing'}, OUT, '00_missing.md', p['SYSTEM'],
                 ra.fill(p['MISSING'], topics=topic_list), 500)
    for t in todo:
        folder = os.path.join(OUT, '%s_%s' % (t[0], slug(t[1])))
        os.makedirs(folder, exist_ok=True)
        ra.stage(a, {'id': t[0], 'title': t[1]}, folder, 'outline.md', p['SYSTEM'],
                 ra.fill(p['OUTLINE'], id=t[0], title=t[1], about=t[2], games=game_names), 900)
    if not a.skip_games and not only:
        for g in games:
            ra.stage(a, {'id': 'game', 'title': g[0]}, os.path.join(OUT, 'games'), slug(g[0]) + '.md',
                     p['SYSTEM'], ra.fill(p['GAME'], name=g[0], about=g[1][:600], topics=topic_list), 300)
    assemble(topics, games)
    ra.log('=== done: Claude reviews LIB_SPARK/howto/OUTLINE.md next.')


if __name__ == '__main__':
    main()

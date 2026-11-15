#!/usr/bin/env bash
# Spark game designs: every idea in LIB_LLMIN/LIB_SPARK/GAME_IDEAS.txt ("Title | what happens",
# optionally "| columns: maze size, keys, par moves" for the level table's own columns)
# becomes a concept and a 5-level table in arcade/out/ (Spark writes words and numbers only;
# Claude writes the scripts). Started by START_SPARK_GAME_DESIGNS.bat. Done ideas are skipped.
HERE="$(cd "$(dirname "$0")" && pwd)"
IDEAS="${SPARK_IDEAS:-/home/igame3d/projects/LIB_LLMIN/LIB_SPARK/GAME_IDEAS.txt}"
Q="$HERE/arcade/games_ideas.tsv"
python3 -I - "$IDEAS" "$Q" <<'PY'
import sys, re, zlib
ideas, out = sys.argv[1], sys.argv[2]
rows = ['# id\ttitle\tprefix\tbrief\tlevel columns\tlayout legend']
for line in open(ideas, encoding='utf-8', errors='replace'):
    line = line.strip()
    if not line or line.startswith('#') or '|' not in line: continue
    parts = [x.strip() for x in line.split('|')]
    title, brief = parts[0], parts[1]
    cols, legend = 'speed | count | lives | bonus', '. empty, # wall, P player start'
    if len(parts) > 2 and parts[2].lower().startswith('columns:'):   # Title | what happens | columns: a, b, c
        cols = ' | '.join(c.strip() for c in parts[2][8:].split(',') if c.strip()) or cols
        legend = 'none'                       # own columns: no layout pictures (run_arcade.levels_prompt)
    else:
        brief = ' | '.join(parts[1:])
    if not title: continue
    gid = str(100 + zlib.crc32(title.lower().encode()) % 900)          # the same title keeps its number
    prefix = ''.join(w[:1].upper() + w[1:] for w in re.findall(r'[A-Za-z]+', title))[:5] or 'Game'
    rows.append('\t'.join([gid, title, prefix, brief, cols, legend]))
open(out, 'w', encoding='utf-8').write('\n'.join(rows) + '\n')
print(f'{len(rows) - 1} idea(s) in the queue')
PY
cd "$HERE/arcade" && exec bash run_arcade.sh --games games_ideas.tsv --no-script

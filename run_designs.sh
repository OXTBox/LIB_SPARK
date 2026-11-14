#!/usr/bin/env bash
# Spark game designs: every idea in LIB_LLMIN/LIB_SPARK/GAME_IDEAS.txt ("Title | what happens")
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
    title, brief = [x.strip() for x in line.split('|', 1)]
    if not title: continue
    gid = str(100 + zlib.crc32(title.lower().encode()) % 900)          # the same title keeps its number
    prefix = ''.join(w[:1].upper() + w[1:] for w in re.findall(r'[A-Za-z]+', title))[:5] or 'Game'
    rows.append('\t'.join([gid, title, prefix, brief, 'speed | count | lives | bonus', '. empty, # wall, P player start']))
open(out, 'w', encoding='utf-8').write('\n'.join(rows) + '\n')
print(f'{len(rows) - 1} idea(s) in the queue')
PY
cd "$HERE/arcade" && exec bash run_arcade.sh --games games_ideas.tsv --no-script

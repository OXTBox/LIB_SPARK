#!/usr/bin/env bash
# Start (or resume) Spark's arcade run. Started by START_SPARK_ARCADE.bat or: bash run_arcade.sh
# Finished stages are skipped, so closing the window and starting again is safe.
HERE="$(cd "$(dirname "$0")" && pwd)"
LOCK="$HERE/out/.running"
mkdir -p "$HERE/out"
if [ -f "$LOCK" ] && kill -0 "$(cat "$LOCK")" 2>/dev/null; then
    echo "Spark's arcade run is already going (process $(cat "$LOCK")). Close its window to stop it."
    exit 0
fi
echo $$ > "$LOCK"
trap 'rm -f "$LOCK"' EXIT
python3 -u -I "$HERE/run_arcade.py" --work-minutes "${SPARK_WORK:-20}" --rest-seconds "${SPARK_REST:-15}" "$@"

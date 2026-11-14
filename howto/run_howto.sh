#!/usr/bin/env bash
# Start (or resume) Spark's LIB_HOWTO outline run. Started by START_SPARK_HOWTO.bat or: bash howto/run_howto.sh
# Finished files are skipped, so closing the window and starting again is safe.
HERE="$(cd "$(dirname "$0")" && pwd)"
LOCK="$HERE/out/.running"
mkdir -p "$HERE/out"
if [ -f "$LOCK" ] && kill -0 "$(cat "$LOCK")" 2>/dev/null; then
    echo "Spark's LIB_HOWTO run is already going (process $(cat "$LOCK")). Close its window to stop it."
    exit 0
fi
echo $$ > "$LOCK"
trap 'rm -f "$LOCK"' EXIT
python3 -u -I "$HERE/run_howto.py" --work-minutes "${SPARK_WORK:-20}" --rest-seconds "${SPARK_REST:-15}" "$@"

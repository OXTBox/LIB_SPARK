#!/usr/bin/env python3
"""LIB_SPARK's check that runs without LiveCode or LM Studio (A-50): the runner takes the code out of
an answer and reads the pace the way the README says. Nothing is sent to the model.

    python3 -I tests/run_tests.py
"""
import os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'arcade'))
import types
import run_arcade                             # noqa: E402

CHECKS, FAILS = [0], []


def check(name, ok, got=None):
    CHECKS[0] += 1
    if not ok:
        FAILS.append(name)
        print("FAIL  %s%s" % (name, "" if got is None else "  (got %r)" % (got,)))
    else:
        print("ok    %s" % name)


def done():
    print("\n%d of %d passed" % (CHECKS[0] - len(FAILS), CHECKS[0]))
    return 1 if FAILS else 0


def main():
    check('code_of: the longest fenced block', run_arcade.code_of('hi\n```\nshort\n```\n```livecode\non a\nend a\n```') == 'on a\nend a\n')
    check('code_of: no fence, the whole text', run_arcade.code_of('on a\nend a') == 'on a\nend a\n')
    check('code_of: an unclosed fence still counts', run_arcade.code_of('```\non a') == 'on a\n')
    a = types.SimpleNamespace(work_minutes=20, rest_seconds=15)
    w, r = run_arcade.pace(a)
    check('pace: two numbers (pace.txt or the defaults)', isinstance(w, float) and isinstance(r, float), (w, r))
    lv = run_arcade.prompts()['LEVELS']
    check('own level columns: no LAYOUTS picture asked for', 'LAYOUTS' not in run_arcade.levels_prompt(lv, {'legend': 'none'})
          and 'NOTES' in run_arcade.levels_prompt(lv, {'legend': 'none'}))
    check('old ideas still get LAYOUTS', 'LAYOUTS' in run_arcade.levels_prompt(lv, {'legend': '. empty, # wall'}))
    import tempfile, time as _t
    with tempfile.TemporaryDirectory() as d:
        old = run_arcade.CLOCK
        run_arcade.CLOCK = os.path.join(d, 'clock')
        a2 = types.SimpleNamespace(work_minutes=10, rest_seconds=900)
        open(run_arcade.CLOCK, 'w').write('%f %f' % (_t.time() - 1800, _t.time() - 60))
        check('a run soon after the last one continues its work period', run_arcade.resume_clock(a2) < _t.time() - 1700)
        open(run_arcade.CLOCK, 'w').write('%f %f' % (_t.time() - 5000, _t.time() - 1000))
        check('a run after a full rest starts a new period', run_arcade.resume_clock(a2) > _t.time() - 5)
        run_arcade.CLOCK = old
    return done()


if __name__ == '__main__':
    sys.exit(main())

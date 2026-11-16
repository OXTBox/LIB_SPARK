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
    # entities (the procedural entity pilot): the calibration boat and a broken recipe
    sys.path.insert(0, os.path.join(ROOT, 'entities'))
    import entity
    boat = open(os.path.join(ROOT, 'entities', 'recipes', '000_sail_boat_calibration.txt')).read()
    rep, ok, whole = entity.check(boat)
    check('entity: the demo boat as a recipe passes, 31 edges as its comment says', ok and len(whole.edges()) == 31, rep)
    lc, fn = entity.code(boat)
    check('entity: code uses the engine calls', fn == 'Ent.SailBoatMesh' and 'MeshLoft(' in lc and 'MeshBox(24, 14, 30)' in lc)
    loose = boat.replace('cabin | box | 24,14,30 | 0,7,-15', 'cabin | box | 24,14,30 | 0,300,-15')
    check('entity: a part floating loose fails "joined"', any('joined' in r and 'FAIL' in r and 'cabin' in r for r in entity.check(loose)[0]))
    lop = boat.replace('0,0,10; 0,70,10', '0,0,10; 0,70,10; 0,0,0')
    check('entity: a bad line is a parse fault, not a crash', not entity.check(lop)[1])
    upside = boat.replace('cabin | box | 24,14,30 | 0,7,-15', 'cabin | box | 24,14,30 | 0,-32,-15')
    check('entity: a relation that is not true fails (cabin under the hull)', any('relate' in r and 'FAIL' in r for r in entity.check(upside)[0]))
    words = boat.replace('RELATIONS: cabin on top of hull; sail above hull',
                         'RELATIONS: the cabin sits on hull; sail above the hull; hull on the ground; cabin on the back of hull')
    rep = entity.check(words)[0]
    check('entity: Spark\'s wordings read ("sits on", "the hull", "on the ground", "on the back of")',
          any('relate   ok: 4' in r for r in rep), rep)
    front = boat.replace('RELATIONS: cabin on top of hull; sail above hull', 'RELATIONS: cabin in front of hull')
    check('entity: front is +z (the cabin sits at the back, so "in front of" fails)',
          any('relate' in r and 'front is +z' in r for r in entity.check(front)[0]))
    two = ('ENTITY: Twins\nBASE: ground\nRELATIONS: arms on the sides of body\nPARTS:\n'
           'body | box | 20,40,20 | 0,20,0 | 0,0,0 | body\narm_left | box | 6,20,6 | -13,25,0 | 0,0,0 | arm\n'
           'arm_right | box | 6,20,6 | 13,25,0 | 0,0,0 | arm\n')
    rep = entity.check(two)[0]
    check('entity: a plural ("arms") checks every part of that kind', any('relate   ok: 1' in r for r in rep), rep)
    hut = 'ENTITY: Hut\nBASE: ground\nPARTS:\nwalls | box | 40,30,40 | 0,27,0 | 0,0,0 | walls\nWait, the walls float.\nroof | pyramid | 4,30,20 | 0,52,0 | 0,0,0 | roof\n'
    rep, ok, whole = entity.check('chatter\n' + hut.replace('ENTITY: Hut', 'ENTITY: Old') + hut)
    check('entity: the last recipe is read, musing lines skipped, a floating hut set down on y 0', ok and
          any('moved down by 12.0' in r for r in rep) and abs(max(p[1] for p in whole.v)) < 1e-6, rep)
    return done()


if __name__ == '__main__':
    sys.exit(main())

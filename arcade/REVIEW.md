# Spark arcade test: review

Friday, November 13, 2026. Model `spark-x2.6-4b` in LM Studio, 8k context, one request at a
time. Reviewed by Claude (Fable 5.2).

**Question:** can Spark take a small arcade game from a one-line brief to a Vibecode3D card
script, working the concept, the levels and the script out one after another, with nobody
testing in between?

**Answer:** the concepts and level tables are usable; the scripts are not. 1 of 12 compiles,
and that one is not a game. Spark should write the words and the numbers, not the code.

## The run

12 original games in classic arcade genres, 3 requests each (concept → 5 levels → script):
36 requests, 950 s of model time, 16 minutes on the clock, 39,045 tokens out. It finished before
the first 20-minute rest came due.

| Stage | Tokens out | Seconds | Kept the format |
|---|---|---|---|
| Concept | 274 to 454 | 4 to 26 | 12 of 12 |
| Levels | 354 to 542 | 6 to 33 | 12 of 12 tables; 0 of 12 layouts |
| Script | 1,519 to 3,600 | 23 to 116 | 12 of 12 one code block; 2 cut off at the 3,600-token cap |

Speed was 55 to 70 tokens a second, except from 12:39 to 12:46 (games 3 to 5), when it fell to
15 to 27. Claude was running LiveCode compile checks and a path-finding benchmark on the same
machine in those minutes; that is the likely cause, not proven.

## What came back

**Concepts (good enough to use).** Right format, sensible objects and rules. Faults: invented
controls that contradict the brief (Bat Duel: "press Space to score a point"; Long Worm: "Space
to move forward"), numbers with no thought behind them (ball speed 40 a step would cross the
screen in under a second), and rules that restate the brief.

**Levels (the tables are usable, the layouts are not).** All 12 tables have 5 rows that get
harder in a straight line; the corrected games use them with the speeds rescaled. The layouts
ignore "5 lines of 12 characters" (Vine Run's rows are 17 to 20 characters of `._._._`) and do
not describe a playable arrangement. As `level-recipes.md` already says: a small model picks
from lists well and places things in space badly.

**Scripts (not usable).**

| Game | Lines | Compiles | First fault |
|---|---|---|---|
| 01 Bat Duel | 225 | no | `constant kHalfBatX = kBatW / 2` (a constant from an expression) |
| 02 Wall Breaker | 137 | no | `local sBallX, sBallY, sBallVY = 0, -300, 120` (tuple assignment) |
| 03 Long Worm | 196 | **yes** | not a game: arrows multiply the speed by -1 twice, the worm moves diagonally for ever, no food, no collisions, 13 copies of the same `if sWormLen > n` block |
| 04 Sky Raiders | 168 | no | tuple assignment in `local` |
| 05 Vine Run | 164 | no | `for i = 1 to ...` (not xTalk) |
| 06 Rock Field | 274, cut off | no | tuple assignment in `local` |
| 07 Cross Traffic | 344 | no | `add x into y` |
| 08 Dot Maze | 347, cut off | no | `local` inside a handler shadowing a script local (and named for another game's bricks) |
| 09 Stack Down | 149 | no | tuple assignment in `local` |
| 10 Soft Landing | 140 | no | `put Land.StartLevel 1 into sLevel` (a command used as a function) |
| 11 City Shield | 278 | no | `==` |
| 12 Deep Dive | 148 | no | tuple assignment in `local` |

The same faults repeat: 5 of 12 open with a Python-style tuple assignment, which the prompt's
example did not show and its language notes did not forbid; 3 use syntax the prompt forbade by
name (`==`, `for`). Past the first error the pattern is the same as Long Worm: the shape of the
example copied faithfully (header, constants, hooks, HUD), and no working rules inside it.

## What was done with it

Claude wrote a working script for each game from Spark's concept and level table:
`LIB_GAMES/Vibecode3D_Games/Vibecode3D_Play_<Game>.livecodescript` (BatDuel, WallBreaker,
LongWorm, SkyRaiders, VineRun, RockField, CrossTraffic, DotMaze, StackDown, SoftLanding,
CityShield, DeepDive). Each header says what is Spark's. Draft and corrected script are a pair:
`out/<nn>_<Title>/3_script.livecodescript` and the file above.

All 12 compile and were played without a window through `LIB_GAMES/tools/headless_play.sh`
(keys held for so many steps, state printed): no run-time errors; balls bounce and score,
bricks break, the worm grows and dies, raiders march and fall, rows clear, landers crash.
**None has been seen on screen or played by a person yet**: sizes, speeds and whether the
playfield fits the window are untested.

## For the next run

1. Do not ask Spark for code. Ask for the concept, the level table and a **recipe** (which of a
   few ready-made game frames, with which numbers), and let a script build the card.
2. If code is wanted anyway: add "one variable per `put`; `local a, b, c` takes no values" and a
   second example to the prompt, and compile each draft in the runner, sending the first error
   back for one retry (the runner has no compiler step today).
3. Layouts: ask for a list (`row 2: brick brick empty ...`) or for counts only; never for a
   picture in characters.
4. Pace: `pace.txt` holds "work minutes, rest seconds" and is read before every request. It is
   `20 15` (the owner, 2026-11-13). A whole 36-request run fits inside one work period.

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

## Maze and rooms batch 1 (2026-11-15, 12 ideas, Claude's verdicts)

Run: 03:31 to 03:36, 24 requests, 160 s of model time, 67 to 72 tokens/s; the whole
batch fit inside one 10-minute work period, so the 15-minute rest never came. Ideas: "Maze and
rooms batch 1" in `LIB_LLMIN/LIB_SPARK/GAME_IDEAS.txt`.

**For all 12:** the concepts are usable; the LAYOUTS are not (rows of different lengths, outer
walls with holes, the same room copied five times; as the round-1 review said, a picture in
characters is the wrong thing to ask for). Every one of these is a maze or a room game, so the
levels should come the way Amazing Couple's do: made once as cellmap v2 files by a Python tool
that also checks them (reachable goals, solvable puzzles), drawn and walked from the same file.
Spark's level tables are often flat (the same five rows) or have the speed column going the wrong
way; the numbers below are the ones to use.

| Game | Verdict | What to change |
|---|---|---|
| Lantern Crawl (595) | needs a change | Charge 3 is far too small: lantern = 40 steps at level 1, 30 at level 5; a flask lying in a dead end adds 15 when walked over (Spark garbled it into "refills only when you stand in a dead end"). Drop "score resets each level". First-person in Vibecode3D with the wire walls fading past 3 cells. |
| Two Key Doors (522) | needs a change, **best fit for PROMPT & GLAZE** | No Space key: a coloured door opens when its own hero walks into it. Plates hold a door open while either hero stands on one (that is the puzzle: one holds, the other passes). Timed doors only from level 3. Exit is white (both). Level table: plates 1, 2, 3, 3, 4; timed doors 0, 0, 1, 2, 3. Fits Amazing Couple's code (TAB swap, follower already there). |
| Echo Rescue (630) | needs a change | Spark mixed up the losing rule: a sentry touching a *survivor* sends that survivor back to where they were found (no life lost); a sentry touching *you* costs a life. Drop "survivors call out for one step before moving". Speed column should be the sentries' and go up (60, 70, 80, 90, 100), not down. Pings: 5, 5, 4, 4, 3. |
| Push Block Vault (529) | needs a change | Arrow keys move the player, who pushes (Spark wrote "move blocks"). 3 blocks for 4 marked tiles cannot be won: blocks = tiles. A pit is not a lost life: the block fills it and becomes floor. Space = undo is fine. Levels must be checked solvable by a small Python solver before they ship. |
| Ring Arena (366) | buildable as is | Numbers and table are sane (drones 3 to 11, speed 1.5 to 2.3, lives 3 to 1). Only add a bonus (wave clear 100 x level). One small round arena, no layout needed. Good fit for the xt3d bench. |
| Stair Hopper (931) | needs a change | Win/lose text is garbled ("before the water reaches the bottom"): you lose a life when the water reaches you. Uses cellmap heights (floors with gaps, blue = floating ledge), side view. Water speed 2 to 6 per the table is fine; drifting ledges count 1 to 5 is fine. |
| Glass Corridors (782) | needs a change | Spark inverted the idea: glass *does* block walking and is only see-through; there is no Space key. Score = steps, fewer is better, with a par per level. Speed column means nothing here: use maze size 7, 9, 11, 13, 15 cells and glass share 20% to 40%. |
| Bargain Hall (182) | needs a change, later | The game is the trade table (which stall wants which item and gives which), and Spark did not make one. Drop "a trade costs a life". The item names belong in LIB_GENERICA label files so the market can be rethemed. Ask Spark next for a trade chain per level, not a layout. |
| Wire Sentries (926) | buildable with a small change | No Space key: walking onto a core takes it. Being seen sends you to the last checkpoint pad (Spark made it a lost life; keep 3 lives for being caught three times). Table is good (cores 1 to 5, sentry speed 1.5 to 3). Sight lines along a grid row or column are easy on cellmap cells. |
| Falling Floor (603) | needs a change | The numbers are nonsense (wall_speed, exit_speed). The one number that matters is the fall delay: 1.0 s at level 1 down to 0.6 s at level 5. Rooms must be checked by a Python search that a route through every gem to the exit exists. |
| Tower Shift (751) | drop for now | Rooms that turn and doors that move need stacked maps, which cellmap v2 has not got yet (a Fable job, deferred). Keep the idea for after that. |
| Courier Run (539) | buildable with a small change | No Space key: parcels are picked up at the depot and given by walking into the numbered door. Speed column = the dogs' speed (1.0 to 3.0, fine). Add the clock: 60 s, minus 5 s a level. The city is a maze with wide streets, from the same maze tool. |

Suggested order if the owner wants these built: Two Key Doors (it is the heroes' own game), Wire
Sentries, Courier Run, Ring Arena; then the ones that need a level checker (Push Block Vault,
Falling Floor).

## Maze and rooms batch 2 (2026-11-15, 12 ideas, Claude's verdicts)

Run: 03:37 to 03:43, 24 requests, 181 s of model time, 52 to 70 tokens/s. One cut off: Bridge
Builder Room's level table ran into max_tokens (900) halfway through its layouts; its table is
complete, the layouts are not wanted anyway, so it is not re-run.

**Lesson for the next batch:** the header line "no Space key unless it is needed" was a comment
(`#`) in GAME_IDEAS.txt, so Spark never saw it: 12 of 12 drafts invented a Space key (Space to
ride lifts, Space to collect keys, Space to light beacons). Put such rules in each idea's own
text, or in `arcade_prompt.md` (proposed: "Movement and walking into things do the work; add an
action key only when the idea names one").

| Game | Verdict | What to change |
|---|---|---|
| Mirror Halls (734) | needs a change, **fits PROMPT & GLAZE** | Spark lost the rule that makes it a puzzle: a wall stops only the hero who hits it, the other still moves (Spark wrote "falls into walls, loses a life"). No lives: walls are safe. No Space: standing on both pads ends the level. Score = steps, par per level. Twin mazes from the maze tool with N cells changed: 2, 4, 6, 8, 10. |
| Switch Room (774) | needs a change | Walking onto a switch presses it (no Space). Walls are never deadly: a raised wall blocks, and a wall cannot rise under the player (the switch waits). Colours 2, 2, 3, 3, 4; a second exit from level 3. Needs a Python solver to set par presses. |
| Beacon Chain (787) | needs a change | Walking past a beacon lights it (no Space, no lives: nothing here can hurt you). Beacons 3, 4, 5, 6, 7 is fine; maze 7, 9, 11, 13, 15 cells. Good showcase for vector lines on the floor in Vibecode3D. |
| Pursuit Grid (781) | buildable with a small change | No Space: walking onto a key takes it. The rule is right (hunters move when you move). Level rule: every fourth turn one more hunter steps twice (Spark's "+2 speed" is wrong). Simple and strong; good first game for the grid. |
| Slide Ice Cave (400) | needs a change | No Space: falling into the exit hole ends the level. Drop lives (nothing can hurt you) and use a move par instead; "each life allows three completions" is nonsense. Rooms need a solver check (sliding puzzles are easy to make unsolvable). |
| Lift Shaft (233) | needs a change, later | Spark turned it into "reach the top floor". The game is the deliveries: a person waits with a floor number, you walk them to a lift, ride, walk them out. Lifts 1, 2, 2, 3, 3; people waiting 1 to 5. Side view with cellmap heights. |
| Bridge Builder Room (532) | needs a change | Pushing works by walking (no Space). "Reach the exit with all planks used" is wrong: spare planks are allowed. Chasm width 1, 2, 2, 3, 3; spare planks 2, 2, 1, 1, 0. Needs a solver check like Push Block Vault (the two could share one). |
| Sound Maze (338) | needs a change | Bumping a wall must not cost a life: bumping is how you see. No Space. Sound cues are not in the engines yet; use the wall flash and the corner map only. Second floor from level 3 needs stacked maps (deferred), so levels 1 to 2 only for now. |
| Guard Swap (415) | needs a change, **fits PROMPT & GLAZE** | Two actions on one Space key won't work: PROMPT's knockout is walking into a guard's back, GLAZE's talk is walking up to a guard's face (10 s door). Which hero you play (TAB) picks the trick. Guards 1 to 5; turn every 6 s down to 3 s. |
| Orbit Room (904) | buildable with a small change | Walking through the aligned gap is the exit (no Space). Rotation 0.5 to 0.9 and sparks 1 to 5 are fine; rings 1, 1, 2, 2, 3. One round room: xt3d bench or Vibecode3D. |
| Tile Painter (264) | needs a change | No Space and no timer-deaths: walking paints. "Leaving the room loses a life" cannot happen (walls). Rooms 4x4, 5x5, 6x6, 7x7, 8x8 with pillars; a Python check that each room can be painted (stepping twice un-paints, so not every room can). |
| Storm Rescue (994) | needs a change | Villagers follow you (no Space to climb). A flooded villager is swept back to the start of the level, not a lost life; you lose only when the hilltop floods. Uses cellmap floor heights directly (the sea rises one grey step every 30 s). |

Suggested order from both batches: Two Key Doors, Pursuit Grid, Mirror Halls, Guard Swap (the
three two-hero ones are PROMPT & GLAZE levels), then Wire Sentries, Courier Run, Ring Arena, Orbit
Room; the puzzle rooms (Push Block Vault, Bridge Builder, Switch Room, Slide Ice Cave, Tile
Painter, Falling Floor) after one shared Python solver/checker is written.

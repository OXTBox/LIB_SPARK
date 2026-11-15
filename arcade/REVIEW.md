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

Run: 03:37 to 03:43, 24 requests, 181 s of model time, 52 to 70 tokens/s. Two cut off: Bridge
Builder Room's and Storm Rescue's level outputs ran into max_tokens (900) in their layouts; both
tables are complete and the layouts are not wanted, so neither is re-run.

**Lesson for the next batch:** the header line "no Space key unless it is needed" was a comment
(`#`) in GAME_IDEAS.txt, so Spark never saw it (and batch 3 found the deeper cause: the prompt
said "CONTROLS: Only arrow keys and Space."; fixed after batch 3): 12 of 12 drafts invented a Space key (Space to
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

## Arenas and runs batch 3 (2026-11-15, 12 ideas, Claude's verdicts)

Run: 03:44 to 03:50, 24 requests, 232 s of model time, 28 to 68 tokens/s (slower spells while
the machine was busy). No cut-offs. The keys were written into every idea this time and 10 of 12
still added Space: `arcade_prompt.md` said "CONTROLS: one line. Only arrow keys and Space." and
asked "what costs a life", so every game got a Space key and lives. **Prompt fixed** (CONTROLS:
the keys the idea names, walking does the work; lives only if something can hurt you). Batch 4
tests the fix.

| Game | Verdict | What to change |
|---|---|---|
| Echo Chamber (301) | buildable as is | Keys right, numbers sane (targets 5 to 9, time falling from 1.5 s, lives 3 to 1). A turning-only first-person game: the cheapest to build in Vibecode3D. |
| Hold The Square (702) | buildable with a small change | Standing in the square fills the bar (no Space). Drones 4 to 6 and the square moving sooner (10 to 22) are fine. Small arena: xt3d bench or Vibecode3D. |
| Gate Runner (990) | buildable with a small change | Drop Space (left/right only, as the idea says). Gate speed 20 to 28 and gates 4 to 7 are fine. Same frame as Dodge Tunnel / Coast Road. |
| Lamp Lighter Run (387) | buildable with a small change | Walking past a lamp lights it (no Space). Lamps 5 to 9 fine; dawn = a clock of street length / speed + 30 s. |
| Night Garden (130) | needs a change | "Space to enter the gardener's light" is backwards (the light sends you to the gate). No lives: being seen costs time. Table flat: gardeners 1 to 4, flowers 6 to 14. Same sight rule as Wire Sentries (could share code). |
| Signal Relay (499) | needs a change, **fits PROMPT & GLAZE** | TAB swaps hero (Spark gave both Space and TAB). No lives. Pad pairs 3 to 6 fine; sight = a straight free corridor on the cellmap. |
| Cargo Crawler (541) | needs a change | Walking into a crate hooks it (no Space). The forklift costs a life; crossing the chain just blocks (snake rules). Crates 2 to 6. |
| Spire Climb (839) | needs a change | No Space. A ball knocks you back one turn of the ramp, no lives (the clock is the pressure). Ball speed 2.5 to 4.5 fine. Needs a spiral ramp mesh (hand-built is simpler than stacked cellmaps). |
| Count Room (816) | needs a change | Walking onto a tile chooses it (no Space). A wrong tile resets the count, no lives. Table flat: tiles 5, 7, 9, 12, 15; swaps from level 3. |
| Path Painter Duel (897) | needs a change | Walking paints (no Space); walls block, they do not cost lives. Spark made the rival GLAZE faster than you; equal at level 1, GLAZE +10% a level. Filling enclosed areas needs a flood fill (LIB_MAP has one). |
| Wire Ferry (323) | needs a change | Walking a crate on at the bank loads it; balance = crates left vs right of the middle. Crate weights 1 to 3; current 0, 0, 20, 30, 40. Side view. |
| Rescue Lift (411) | needs a change | Drop "Space to drop the cage" ("miner_speed 0" means nothing). Cage holds 3; a rock cracks it, 3 cracks = a life. Depth 4 to 8 ledges. |

Across the three batches, fourteen games are near enough to build; the owner picks.

## Batch 4 (2026-11-15, 12 ideas, the first run with the fixed prompt)

Run: 03:51 to 03:57, 24 requests, 232 s of model time, 28 to 71 tokens/s. One cut off at
max_tokens (Key Ring Maze's layouts; its table is complete).

**The prompt fix worked for keys:** 12 of 12 CONTROLS lines use exactly the keys the idea names
(Space only in Ring Toss Arena, which asks for it; F in Fold Map Room; TAB in the two hero games).
**Lives are still everywhere**, now attached to odd things ("accumulating dust costs a life",
"walking into a locked wall costs a life"), because the level table's columns are fixed as
`speed | count | lives | bonus` (`run_designs.sh`). Next fix, proposed, not made: let each idea
name its own level columns (e.g. `Title | what happens | columns: maze size, keys, par moves`).

| Game | Verdict | What to change |
|---|---|---|
| Pipe Flow Room (574) | buildable with a small change | Keys right, rule right. The overflow ends the attempt (retry), not a life; time 60 s falling 5 s a level; tiles 4 to 7 fine. Needs a check that each board can connect. |
| Tunnel Digger (623) | buildable with a small change | Keys right. "Tunnel blocked costs a life" drop: only a falling rock does. Gems 5 flat is dull: 4, 5, 6, 7, 8; rocks 3 to 8. A side-view grid game in the Dig/rock genre: needs only a cell grid. |
| Hover Polo (331) | buildable with a small change | Drop lives (a goal is the only score). Rival speed 90 to 130 and goal width shrinking 80 to 50 are good. Physics: puck bounces like Bat Duel's ball (reuse). |
| Shadow Tag (209) | needs a change | Tagged = back to the start, no lives. Coins 5 flat: 4 to 8. Pillar shadows from a circling light: angular check in Python first. |
| Key Ring Maze (654) | needs a change | Walking into a locked wall just blocks. Colours 2, 2, 3, 3, 4; locks 2 to 6. Needs a solver check (a key locked behind its own lock must not happen). |
| Lantern Pair (530) | needs a change, **fits PROMPT & GLAZE** | Spark misread TAB as handing the lantern over; TAB swaps the hero you play (the other holds the lantern and stays). Walls just block. Light radius 4, 4, 3, 3, 2 cells; maze 9 to 15. |
| Twin Lifts (469) | needs a change, **fits PROMPT & GLAZE** | NUMBERS empty and the table flat. Floors 3 to 7; doors needing both heroes 0, 1, 2, 3, 4. Falling only if a door opens on an empty shaft: back to the floor below, no lives. |
| Sky Stepping (422) | needs a change | A slab falls after three steps on it; falling = back to the last tower, lives 3. Slab gap 1 to 2 cells, drift from level 3. |
| Sweep Patrol (802) | needs a change | "Dust costs a life" is nonsense: touching a vacuum costs a life. Dust cells 20 to 40, vacuums 3 to 6 fine. |
| Market Run (949) | needs a change | Bumping a shopper costs time (pushed back), not a life. List 3, 4, 5, 6, 7 items (Spark kept 3). Item names in LIB_GENERICA labels (like Bargain Hall). |
| Fold Map Room (283) | needs a change, later | The idea is good but the fold rule needs designing by a person: which half shows, what "walls add up" means on cellmap heights. Spark kept 1 fold for all levels. |
| Ring Toss Arena (503) | needs a change | A ring that misses is just gone (rings are the clock), no lives. Rings 8, 7, 6, 5, 4; post speed 1.8 to 3.5 fine. |

## Batch 5 (2026-11-15, 12 ideas, each naming its own level columns)

Run: 03:58 to 04:05, 24 requests, 279 s of model time, 20 to 70 tokens/s. One cut off at
max_tokens (layouts again; the table is complete).

**The columns work:** 12 of 12 tables use exactly the columns asked for, and most rise sensibly
(sparks 5 to 13, gaps 2 to 6, plates 3 to 7, fires 1 to 3 with new fires every 60 s down to 15 s).
**Still wrong:** a column named "cells" gets screen pixels in 5 of 12 (maze size 120, hall length
900, room 900,600, pen 120, house width 120); Spark thinks in the 900 x 600 screen the prompt
describes. And the concept still gives every game lives (CONCEPT asks "what costs a life").
For the next batch: say "cells (5 to 20)" in the column name, and drop LAYOUTS from the LEVELS
prompt when an idea has its own columns (every cut-off so far was in LAYOUTS).

| Game | Verdict | What to change |
|---|---|---|
| Sentinel Ring (259) | buildable as is | Keys right, table good (pulse speed 1.5 to 2.2, pulses 1 to 5, turn 0.5 to 0.9). Pickups 5 flat is fine. |
| Lockstep Bridge (262) | buildable with a small change, **fits PROMPT & GLAZE** | Falling = both back to the bridge start, no lives. Table good (length 12 to 28 cells, gaps 2 to 6, moving gaps from level 4). |
| Herd The Sparks (783) | buildable with a small change | Pen size: 4, 4, 3, 3, 2 cells (not 120 to 200, and it should shrink). A spark on the fence is lost, not a life; lose when half are lost. |
| Bucket Line (970) | buildable with a small change | House width 8 to 16 cells, not 120. A fire left 30 s spreads to the next cell; lose when the house is all fire. Fire timing table is good. |
| Dark Elevator (345) | buildable with a small change | Blink seconds should fall (4, 3.5, 3, 2.5, 2), Spark kept 2. Floors 3 to 10 good. |
| Rolling Stone Hall (413) | needs a change | Hall 20 to 40 cells (not 900). A ball hit = back to the last alcove, lives 3. Balls 3 to 7 good. |
| Relay Doors (498) | needs a change, **fits PROMPT & GLAZE** | TAB swaps hero, not "plates". No lives (doors can't hurt). Table good: maze 12 to 16, plates 3 to 7, doors 1 to 5. Close to Two Key Doors: build one, make the other its later levels. |
| Lockstep, Relay, Two Key Doors, Mirror Halls, Guard Swap, Signal Relay, Lantern Pair, Twin Lifts | (note) | Eight two-hero ideas now: enough for a PROMPT & GLAZE "co-op" world. The owner chooses which three or four. |
| Mirror Shots (935) | needs a change | Spark lost "walking into a mirror turns it" (it kept Space, which the idea names, right). No lives: shots are counted against par. Table good. |
| Crystal Pairs (887) | needs a change | Table flat (6 pairs, room 12 all levels): pairs 4, 6, 8, 10, 12; room 4x4 to 6x6. No lives: steps against par. Spark added "pushes crystals and triggers switches" from the new prompt's wording: drop. |
| Pebble Trail (364) | needs a change | Spark invented a lose rule (you must pick up your pebbles). No lose: steps against par. Maze 7 to 15 cells. |
| Echo Steps (460) | needs a change | Ghost delay 0 steps makes it touch you at once: 10, 9, 8, 7, 6. Room 7x7 to 11x11 cells. |
| Dropping Rooms (660) | needs a change | Hole speed falls in Spark's table (should rise), smoke seconds 30 to 20 good. Rooms stacked straight down need stacked maps or one room reused: reuse one room for now. |

## Batch 6 (2026-11-15, 12 ideas, columns with ranges, no layout pictures)

Run: 04:06 to 04:10, 24 requests, 119 s of model time (half of batch 5, as the pictures are
gone), 60 to 70 tokens/s, no cut-offs. **Every table stays inside the ranges given and rises
level by level** (one, Conveyor Sort, wrote its table twice). This is now the way to ask:
`Title | what happens; keys: ... | columns: name (from to), ...`.
Left over: Spark still gives every game lives in the concept (most LOSE lines are "you run out of
lives" with no cause), and 2 of 12 added a key (Twin Keys Vault: Space; Star Weaver: Space).
Next prompt fix, proposed: CONCEPT asks "LOSE: what ends a try (or 'nothing: score is moves
against par')" instead of a lives rule.

| Game | Verdict | What to change |
|---|---|---|
| Fuse Runner (561) | buildable as is | Keys right, rule right (the fuse catching you ends the try), table good. Corridor runner frame like Dodge Tunnel. |
| Rope Swing Gap (539) | buildable as is | Keys right; missing a ledge drops you to the last one (as the idea says; lives 3 are fine). Table good. |
| Snow Plough Maze (641) | buildable with a small change | No lives: the try ends when snow cuts off a house for 10 s. Table good. Streets from the maze tool. |
| Glow Worm Cave (182) | buildable with a small change | "Moving outside the path" loses nothing: walls just block. No lives; time against par. Table good. |
| Ball Gate Arena (667) | buildable with a small change | Drop the stock "picks up / presses switches" text. Lives: none; a drone touching the ball resets it to the middle. Table good. |
| Hidden Floor (168) | buildable with a small change | Spark invented keys; drop them. A hole sends you back (no lives, steps against par). Table good: room 6 to 10, holes 4 to 16. Minesweeper-style numbers on a cellmap. |
| Sleepwalker Guide (234) | buildable with a small change | The stairs end the try (no lives). Table good. |
| Signal Flags (500) | buildable with a small change | A ship not waved in within 20 s sails away (a miss; 3 misses end the round). Table good (one row has 4 berths after 5: fix to 5). |
| Kite Field (873) | buildable with a small change | A bird hitting the kite or the kite touching ground costs a life (Spark gave no cause). Table good. |
| Conveyor Sort (114) | buildable with a small change | A wrong-bin box is a miss (5 misses end the shift), not a life. Table good. |
| Twin Keys Vault (433) | needs a change, **fits PROMPT & GLAZE** | TAB swaps hero (Spark: "swap the two locks"); no Space: standing on a lock turns it. A guard touching a hero sends both to the start. Table good. |
| Star Weaver (640) | needs a change | No Space: looking at a star for half a second links it. A wrong line just breaks the chain, no lives. Table good. |

Running count across six batches: 28 games near enough to build (as is or a small change: 3 + 3 + 4 + 3 + 5 + 10).

## Batch 7 (2026-11-15, 12 ideas, LOSE fix)

Run: 04:11 to 04:15, 24 requests, 120 s of model time, 54 to 69 tokens/s, no cut-offs, every
table in range. **LOSE now names a cause in 8 of 12** (was about 2 of 12): whirlwind reaches the
edge, two trains on one track, falling off a gear. Still "lose all lives" with no cause in 4
(Firefly Jar, Tide Pool Hop, Recycling Robot, Lighthouse Keeper). **New leak:** 3 drafts copy the
prompt's own example wording into CONTROLS ("walking into crates picks them up, pushes them and
presses switches"), even in Gravity Rooms where nothing is pushed. Prompt reworded so the example
is not a phrase to copy. Paper Plane Post added a Space key the idea does not have.

| Game | Verdict | What to change |
|---|---|---|
| Dust Devil Chase (264) | buildable as is | Keys right, LOSE right (a whirlwind leaving the map with a gem ends the try), table good. |
| Train Yard Switch (982) | buildable as is | Keys and rules right; drop "falls off the screen edge" (tracks end in buffers). Table good. |
| Clock Tower Climb (901) | buildable as is | Keys right, LOSE right, table good. Gears as rotating wire meshes: a fine Vibecode3D showcase. |
| Gravity Rooms (620) | buildable with a small change | Drop the leaked "picks up / pushes" text. Otherwise right: spikes end a try, table good. |
| Counterweight Room (518) | buildable with a small change | Drop "picks them up / presses switches" (crates are only pushed). Needs a solver check for par. |
| Cable Car Rescue (468) | buildable with a small change | Two cars meeting ends the try (no lives); hikers don't fall. Table good. |
| Lighthouse Keeper (879) | buildable with a small change | A ship on the rocks is a miss; 3 misses end the night. Table good. |
| Paper Plane Post (754) | buildable with a small change | No Space. Table good. |
| Firefly Jar (655) | needs a change | Nothing can hurt you: a timer per level (60 s) and a count to catch. Lit seconds go 3, 2, 1, 1: fine. |
| Tide Pool Hop (669) | needs a change | Being on a rock when it goes under sends you to the shore (no lives). Tide seconds 26 to 12 good. |
| Recycling Robot (978) | needs a change | No lose rule at all: litter piling over 20 pieces ends the try. Carry 3 to 2 good. |
| Patrol Swap (385) | needs a change, **fits PROMPT & GLAZE** | Walls block, they don't hurt. Caught = both back to the last checkpoint, no lives. Table good. |

Running count across seven batches: 36 games near enough to build (3 + 3 + 4 + 3 + 5 + 10 + 8).

## Batch 8 (2026-11-15, 12 ideas, after the first real rest)

Run: rest 04:16 to 04:31 (model unloaded), work 04:31 to 04:35, 24 requests, 118 s of model
time, 53 to 72 tokens/s, no cut-offs, tables in range. **CONTROLS right in 12 of 12, no invented
keys, no copied phrase** (the reworded prompt line works). LOSE names a cause in 10 of 12, and
Hedge Cutter answered "nothing: the score is moves against par" exactly as allowed. Spark still
bolts "lives" onto a cause now and then ("runs out of lives after a wrong bell"), which is easy
to strip.

| Game | Verdict | What to change |
|---|---|---|
| Hedge Cutter (877) | buildable as is | Keys, rule, LOSE and table all right (maze 11 to 15, regrow 50 s down to 20, par cuts 7 to 15). |
| Lift Bridge (833) | buildable as is | Up/down only, LOSE right, table good. |
| Echo Bats (163) | buildable as is | Arrow keys move you (Spark's "move the lantern" means the same); being caught ends the try; table good. |
| Lost Lambs (914) | buildable as is | A scared lamb ends the try; table good. |
| Bell Ringer (152) | buildable with a small change | A wrong bell restarts the tune (no lives). Table good. |
| Spotlight Stage (483) | buildable with a small change | A missed cue or a bump is a miss; 3 misses end the show. Table good. |
| Rain Barrel (778) | buildable with a small change | The barrel walks the street, it can't fall off a roof: a gutter overflowing on the ground is a miss. Table good. |
| Slow Comet (797) | buildable with a small change | The tail pushes, it doesn't hurt (that was the idea): missing the dock ends the try. Table good. |
| Puddle Jumper (990) | buildable with a small change | Wet points: 3 splashes end the try (Spark's own count, drop "lives"). Table good. |
| Sock Sorter (885) | buildable with a small change | The clock ends the round; no lives. Seconds 85 to 45 good. |
| Tunnel Lights (629) | needs a change | First-person needs all four arrows (turn and walk); a switch is turned on by walking into it, not by Up. |
| Two Hand Crane (278) | needs a change, **fits PROMPT & GLAZE** | TAB swaps hero (each has one job: PROMPT the arm, GLAZE the guide). A dropped crate is a miss. Table good. |

Running count across eight batches: 46 games near enough to build (3 + 3 + 4 + 3 + 5 + 10 + 8 + 10).
The format is now settled; further batches mostly add more of the same. Spark could next draft
something else the owner needs (see DAY_WORK_11_15).

## Batch 9 (2026-11-15, 12 ideas)

Run: 04:36 to 04:40 (the same work period as batch 8, which began 04:31: the next run rests
first), 24 requests, 111 s, 61 to 70 tokens/s, no cut-offs. Keys right in 12 of 12. Two misreads
of how the player acts (Chalk Line, Scarecrow Field) and one TAB misread (Draw Bridge Duel).

| Game | Verdict | What to change |
|---|---|---|
| Moth Lamp Maze (255) | buildable as is | Keys, LOSE (oil runs out) and table right. |
| Ice Block Tower (634) | buildable as is | Collapse ends the try; table good (height 7 to 14, melt 35 s down to 20). |
| Domino Run (331) | buildable with a small change | Nothing hurts: moves against par (Spark's "falling into a domino" is invented). Table good. |
| Bubble Lift (397) | buildable with a small change | An eel sends you to the last ledge (no lives). Table good. |
| Pinball Corridor (801) | buildable with a small change | A drain sends you back to the last star; 3 drains end the run. Table good. |
| Glass Bottle Shelf (994) | buildable with a small change | Cracks allowed is the lose rule (Spark's own column), not lives. Table good. |
| Treasure Map Steps (545) | buildable with a small change | Wrong steps allowed (3 to 1) is the lose rule; no lives. Table good. |
| Clock Hands Room (285) | needs a change | The numbers column came back as "1, 2, 3" every level: 4, 6, 8, 10, 12. A hand sends you to the middle. |
| Chalk Line (174) | needs a change | You walk and the chalk follows you (Spark made the arrows move the line). Nothing can fall off: the bell ends the round. |
| Scarecrow Field (807) | needs a change | You walk; walking into a scarecrow pushes it (Spark made arrows move it). A crow on a crop is a miss; 5 misses end the day. |
| Stepping Stones Duet (552) | needs a change, **fits PROMPT & GLAZE** | Falling in = both back to the bank, no lives. Table good. |
| Draw Bridge Duel (753) | needs a change, **fits PROMPT & GLAZE** | TAB swaps between PROMPT and GLAZE (not with the knight). Table is muddled: knights 1, 1, 2, 2, 3; crank 4 to 2 s; moat 2 to 5. |

Running count across nine batches: 53 games near enough to build (46 + 7).

## Batches 10 and 11 (2026-11-15, 24 ideas in one run)

Run: rest 04:45 to 05:00 (model unloaded; the work clock carried over from batch 9), work 05:00
to 05:08, 48 requests, 230 s of model time, 59 to 72 tokens/s, no cut-offs, every table in range.
Keys right in 24 of 24 (a few describe them oddly: "left moves the slide", "moves the boat").
Lives still creep into LOSE lines, but most now have a real cause.

| Game | Verdict | Change |
|---|---|---|
| Tower Signals (103) | as is | |
| Ring Road (186) | as is | |
| Penguin Slide (794) | as is | |
| Bakery Rush (733) | as is | |
| Snow Fort (437) | as is | |
| Junk Magnet (617) | small | overheating drops the load (it doesn't end the try); 3 overheats end it |
| Clean Sweep Chimney (563) | small | a puff pushes you up a ledge, it doesn't cost a life |
| Hatch Watch (529) | small | a chick out of the door is a miss; 3 misses end the night |
| Kitten Rescue (247) | small | a cracked branch drops you to the one below |
| Library Shelver (949) | small | a book not shelved when asked is a miss |
| Wire Walker (966) | small | drop "30 moves"; a fall ends the try |
| Ghost Train (817) | small | the signs are scenery: only tipping ends the ride |
| Mole Holes (650) | small | a missed mole is a miss, a filled hole just closes |
| Seed Sower (332) | small | eaten seeds are re-sown, not lives; the clock ends the day |
| Sun Dial Garden (474) | small | a heat meter fills in the sun and empties in shade |
| Tidy Robot (173) | small | the cat costs time, not lives; the clock ends the round |
| Satellite Dish (716) | small | the signal bar is the score; no lives |
| Water Slide (791) | small | the keys lean the rider (Spark: "move the slide") |
| Night Bus (358) | change | stopping needs a brake: add Down (the idea lacks it), or stops are taken by staying in the stop lane |
| Leaf Pile (796) | change | walking pushes leaves (Spark gave Up a job and made stepping on leaves deadly) |
| Lantern Festival (624) | change | you steer the lantern, not a boat; a lantern touching an arch is lost |
| Lock Pick Room (995) | change | walking onto a pin raises it (no Up); out of order drops all pins, no lives |
| Paint Bucket Relay (521) | change, PROMPT & GLAZE | TAB swaps hero; no lives |
| Rope Bridge Builder (747) | change, PROMPT & GLAZE | TAB swaps hero; a fall goes back to the bank |

Running count across eleven batches: 71 games near enough to build (53 + 18).

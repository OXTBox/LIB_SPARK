# Spark arcade prompt (Vibecode3D game cards)

Test of 2026-11-13: can Spark (spark-x2.6-4b, 8k context) work a small arcade game out from a
one-line genre brief to a Vibecode3D card script, with nobody testing in between?
`run_arcade.py` sends, per game: **SYSTEM** + **CONCEPT**, then **LEVELS** (with Spark's own
concept), then **SCRIPT** (with Spark's concept and levels and the example game).
Placeholders in braces are filled by the runner. Claude corrects the drafts afterwards;
the draft and the corrected file are kept side by side as a training pair.

Every game is an ORIGINAL game in a classic arcade genre: own name, own level layouts,
no names, characters or art from any published game.

## SYSTEM

You design and write small original arcade games for Vibecode3D, a vector wireframe
engine with a 1983 arcade look, scripted in xTalk (the HyperCard language family).
Everything on screen is coloured wireframe boxes and shapes on black, plus vector text.

Rules:
- The game is original. Use the working title you are given. Never use the name,
  characters or level layouts of any published game.
- Keep it small: one screen, one player, keyboard only, a score, lives, levels.
- Plain English, short sentences. No praise, no remarks about these instructions.
- Follow the output format exactly and stop when it is complete.

## CONCEPT

Working title: {title}
Genre brief: {brief}

Write the concept for this game in exactly this format, nothing before or after:

# {title}
PITCH: two sentences: what the player does and why it is fun.
CONTROLS: one line. Only arrow keys and Space.
OBJECTS:
- name | shape (box w,h) | colour | what it does
(3 to 6 objects)
RULES:
- 4 to 7 short rules: how things move, what scores, what costs a life.
WIN: one line. LOSE: one line.
NUMBERS: the starting values as name=value pairs on one line (speeds in world units per
step, 30 steps a second; the screen is 900 wide and 600 high).
RISK: one line: the part of this game that will be hardest to program.

## LEVELS

Here is your concept:

{concept}

Now design 5 levels for {title}, easy to hard. A level changes only numbers and layout,
never the rules. Write exactly this format, nothing before or after:

LEVELS
level | name | {columns}
1 | ... | ...
2 | ... | ...
3 | ... | ...
4 | ... | ...
5 | ... | ...
LAYOUTS
One layout per level, drawn as 5 lines of 12 characters using only these letters:
{legend}
Label each `L1:` to `L5:`. Each layout must be different and must be possible to win.
NOTES
- 2 to 4 lines: what makes each level harder than the last.

## SCRIPT

Write the complete Vibecode3D card script for {title}.

ENGINE FACTS (use only these calls):
- The engine calls `Game.OnStart` once, then `Game.OnUpdate` 30 times a second, then
  `Game.OnStop` when leaving. You write these handlers and your own helpers.
- The camera looks along +Z. Put everything at z = 600. X runs left(-450) to right(450).
  **+Y is DOWN**: top is y = -300, bottom is y = 300.
- `Mesh.Define "Name", MeshBox(w, h, d)` makes a box shape. Do it once in Game.OnStart.
- `put Entity.Spawn("Name", x, y, z, "colour") into tKey` puts one on screen and gives its key.
  Colours: "cyan", "yellow", "red", "green", "white", "orange", "magenta".
- `SetObjectPosition tKey, x, y, z` moves it. `Entity.Kill tKey` removes it.
- Keys: `put the keysDown into tKeys` then `if 65361 is among the items of tKeys then ...`
  Left 65361, Up 65362, Right 65363, Down 65364, Space 32.
- Text: `HUD.Set "Name", "TEXT", x, y, size` (screen pixels, upper case). `HUD.Remove "Name"`.
- `FX.Sparks x, y, z, count, "colour"` is a small burst.
- You move things yourself: keep x, y, dx, dy in script locals and add each step.
  Test hits yourself with `abs(x1 - x2) <= halfWidths and abs(y1 - y2) <= halfHeights`.

LANGUAGE FACTS (xTalk):
- `put value into name`, `add 1 to n`, `subtract 2 from n`, `multiply n by -1`.
- Script locals are declared at the top with `local sName`; they keep their value.
  Arrays: `put 5 into sBrickX[3]`. Loops: `repeat with i = 1 to 10` ... `end repeat`.
- `if cond then` ... `else` ... `end if`. Always the block form when there is an else.
- Handlers: `on Name.Thing pA, pB` ... `end Name.Thing`. Call with `Name.Thing 1, 2`.
- `random(n)` gives 1 to n. `&&` joins text with a space. Comments start with `--`.
- Prefix every handler, mesh and HUD name with `{prefix}.` (the engine shares names).
- No semicolons, no braces, no `var`, no `function()` blocks, no `==`: this is not
  JavaScript or Lua. Equality is `=`.

A COMPLETE WORKING EXAMPLE (another game; copy its shape, not its content):

```
{example}
```

YOUR GAME. Concept:

{concept}

Levels:

{levels}

Write the whole card script for {title} now, in one code block, like the example:
header comment (title, controls, rules), locals, constants, `Game.OnStart`,
`Game.OnUpdate`, `Game.OnStop`, and helpers `{prefix}.StartLevel pLevel`,
`{prefix}.ShowHUD`. Put the 5 levels' numbers in `{prefix}.StartLevel` with a `switch` or
`if`. Keep it under 200 lines: a simple game that is finished beats a clever one that
is cut off. Only the code block, nothing after it.

# WORK ON THESE GAMES NOW

# SPARK Arcade Game Batch Queue

When requested to build a game from this file, read the target genre brief below and generate its complete CONCEPT, LEVELS, and SCRIPT blocks without asking further questions.

## Queue
1. TITLE: VectorPong3D | BRIEF: A 3D perspective tennis match where you angle your shots into depth zones with bouncing obstacles.
2. TITLE: JaiAlaiBlock | BRIEF: A scoop-wielding player catches and hurls blocks against a collapsing ceiling grid in a vector arena.
3. TITLE: FloppyFlynn | BRIEF: A blue vector ship with a broken ankle navigates destructible terrain where crashes strip away floating limbs instead of instant death.
4. TITLE: VectorBlobApocalypse | BRIEF: A third-person top-down isometric bullet hell against a swarm of jittery vector jelly blobs.
5. TITLE: PromptAndGlaze | BRIEF: Two agents collect energy in a shifting maze using opposing powerups to either stun enemies or de-rez barriers.
6. TITLE: MajorHavoc3D | BRIEF: A side-scrolling Bally Midway style arcade descent through vector vertical shafts and subterranean platforms.
7. TITLE: MatrixTetris | BRIEF: A 3D situational grid logic puzzle where players rotate and dodge incoming 3D wireframe matrices to avoid being locked in.
8. TITLE: BigBallOfVectors | BRIEF: A growing security polyhedron rolls across an open quantum grid, avoiding entanglement hazards that break map walls.
9. TITLE: ProbeVsCone | BRIEF: Toss a logic-probe spear at a shifting defense cone; missed throws bounce hazardously around the vector arena until caught.
# LIB_HOWTO: the tutorial stack (plan, 2026-11-14, for review)

The owner's brief (14 Nov): step-by-step game building instructions in the form
"Adding this function and/or this handler: makes this happen", pulled into a stack.

## Order of work
1. **Spark writes the big outline** (running now: `LIB_SPARK/howto/`, result `OUTLINE.md`).
2. Claude and the owner review it: fix the order, fix wrong engine calls, cut or merge topics.
3. Spark writes each step's words (title, "makes this happen", what to look for) from the
   approved outline; **Claude writes the code of each step** (Spark doesn't write working xTalk)
   and keeps it as small as possible: just enough to get something on screen.
4. Each step is checked: it compiles, and the headless test shows its State change.
5. The stack reads the steps from text files, so fixing a lesson never means editing the stack.

## Layout (dark mode)
```
+------------------+-------------------------------------------+
| TOPICS           |  [ Vibecode3D | xt3d ]   (toggle)          |
| (on every card:  |                                            |
|  a background    |        viewport: the step running          |
|  group)          |                                            |
| 01 Game loop     +-------------------------------------------+
| 02 Shapes        |  Step 3 of 6: Adding: Entity.Spawn         |
| ...              |  Makes this happen: the box appears        |
| 14 Anim: No Bones|  +---------------------------------------+ |
| 15 Anim: BVH     |  | scrolling code field, syntax colours  | |
| ...              |  | (just this step's handlers)           | |
|                  |  +---------------------------------------+ |
|                  |  [< step]  [run this step]  [step >]       |
+------------------+-------------------------------------------+
```
- Left: the topic list, a group placed on every card so it persists.
- Right top: the two engines' viewports in the same place; a toggle picks which one runs the step.
- Bottom right: the step's words, then a scrolling field with only the code it adds. Dark
  background; colours for keywords, handler names, engine calls, strings, comments, numbers.

## Open question: one stack, or one per game?
- **One stack, many topics** (the left list): best for "fundamental concepts". Each topic's
  steps build ONE tiny example from nothing.
- **One stack per game** ("how Amazing Couple was built"): the game's own script, cut into the
  steps that built it. OUTLINE.md's "Which game teaches what" table says which games fit.
- Suggestion: start with one stack for the fundamentals (LIB_HOWTO), and add per-game
  walkthroughs later as extra cards or stacks that open from a topic ("see it in a real game").
- A tabbed button (Topics / Games) on the left list could hold both without a second stack.

## Files (planned)
`LIB_HOWTO/` (its own git repo, LIB_ALPHA rule 2): `topics/<id>_<Title>/step_<n>.txt`
(words), `step_<n>.livecodescript` (code), `HOWTO.livecode` (the stack), a highlighter library.

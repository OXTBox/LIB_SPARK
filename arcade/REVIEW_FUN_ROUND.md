# FUN round review (2026-11-16)

Your answers to the maze review (`LIB_LLMOUT/Read/LIB_SPARK/Spark_Maze_Game_Review_Notes_11_16_2026.txt`)
and the UFO idea went to Spark as 12 new briefs (`ideas_fun_round.txt`). These ran with a new
CONCEPT prompt that has a **FUN** block (TOY, CHOICE, SURPRISE, MOMENT, EXTRA) because you said
the designs read as mechanics, not fun. Drafts are in `out_fun/`, and the old drafts of the same
titles are still in `out/`, so you can compare them.

## What the FUN block did (the research result)

| | |
|---|---|
| Run | 24 requests, 10:38 to 10:42, about 4.5 min, 50 to 75 tokens/s, no cut-offs |
| Format | FUN filled in 12 of 12; level tables inside their ranges in 12 of 12 |
| Better than PITCH? | Yes where **the brief already had the fun**: Courier Run (tip vs time, pawn shop vs warehouse), Hollow Mountain (beam vs battery), One Cent Raise, Two Key Doors' MOMENT |
| Worse | TOY was "moving with the arrow keys" in 5 of 12. Spark flipped the story in 4: Ghost Light Mine (your lantern *guides* the ghost), UFO Low Pass (a farmer beaming the UFO), Echo Rescue (you play the survivor), UFO Wrong Cargo (garbled; CONTROLS left empty) |
| Banned words | "fun", "tense" and "engaging" are gone, but "relief" and "satisfying" took their place |

**Lesson (for LIB_OMEGA):** Spark can repeat fun that is in the brief, but it cannot come up with
fun itself. The fun has to come from you or Claude. Spark's job stays the same: tables, names
and variations. Next prompt to try (it fits what Spark does well, which is picking from lists):
give Spark 6 candidate toys and twists that Claude writes, and have Spark rank them and fill the
level table for the top two.

## The games, merged (your answer + the review facts), ready to build

**Ghost Light Mine** (was Lantern Crawl). First-person mine maze with wire walls that fade past 3 cells.
A stick-figure ghost drifts after you, trailing see-through copies of itself. Inside the lantern's
radius it stops and backs off. The lantern burns 60 steps at level 1 and 35 at level 5. Oil flasks
in dead ends add 15 each. If the lantern goes out, the ghost reaches you and you lose a life,
then restart at the level start with the tool you have found. Blockages: L1 iron gate and key,
L2 broken wall and pickaxe, L3 cave-in and dynamite; L4 and L5 have two blockages each. Ignore
Spark's draft (inverted) and use its table only.

**Two Key Doors** ("let's try it"). This is built as the review said: a door opens for its own
hero, plates hold doors open, timed doors from L3, white exit. Spark's table is right
(plates 1 to 4, timed 0 to 3). It fits Amazing Couple's code (TAB swap, follower). The levels
need a solver check. **Next build.**

**Echo Rescue** ("try it"). Your Scooby-Doo hallway gag is the point: every door is paired with
another door down the hall, and sentries and survivors go through them too, so things pop out
in the wrong place. A survivor touches you and follows. A sentry touching a survivor sends it
back where it was found. A sentry touching you costs a life. You play the rescuer (Spark
got this backwards). The table is right: sentry speed goes up 60 to 100, doors 4 to 12.

**One Cent Raise** (was Push Block Vault). Endless warehouse, scored, never "solved". This is
Sokoban-style pushing, not Pengo (Pengo crushes enemies with sliding ice). Rules:
delivery men drop towers in the way, colour rooms pause the clock and deliveries for 5 s when
cleared, truck-bay boxes go out one screen edge and you come back in on the other side, smashable
boxes, V I B E letter boxes, buried slow-time boxes, points divided by the clock, and
PAY RAISE 1 CENT! every 10 deliveries. Lose: the floor fills so you can't move (Spark said
"clock reaches zero", but the clock only divides the score). No solver needed because the board
is never fixed.

**Ring Arena**: as before, plus a wave bonus of 100 × level. Spark's FUN block added "pause to
charge", which goes against the core rule. Ignore it.

**Wire Sentries** (you asked "see what this is"). The fun is stealth: you watch a sentry's loop,
wait at a corner and slip behind its back the moment it turns, and you get close calls. Spark's
SURPRISE is a good one: a sentry turns back halfway through its loop. Keep that. Being seen sends
you back to the checkpoint, and the third time ends the run. Fix the table: cores should go
1 to 5 (Spark put 5 in every row).

**Dont Break The Walls** (was Glass Corridors). This is your version. Score starts at the number
of walls, and each crash takes 1 off. The outer walls are stone. Mushrooms: speed (harder to
stop, so you break more), slow, and big (breaks 2 walls at once). It is dark, so you see your
walls and one layer beyond. The stone is at the end. Spark got the mushrooms backwards and made
up key controls. Use its table only.

**Hollow Mountain** (was Falling Floor, your Mountain King memory). An original game in that genre
with its own name and look. Floors of lines with holes to drop through, a ghost that passes
through walls and that the flashlight scares off (battery 30 s down to 15 s), spiders on threads
in the holes, a diamond at the bottom, and then the climb back out. **Your glitch, done on
purpose:** dance left-right-left on the bottom floor for 5 s and you drop through into a glitch
world of garbled wire shapes worth strange points, with a way back. Spark made the glitch a way
to lose, which is wrong. Its CHOICE (beam vs battery) is the core of the game.

**Courier Run**: your extras are in: tips for fast delivery, tip coins in the street, "That's not
what I ordered. Send it back." for a few parcels, and you take those back to the warehouse (few
points) or the pawn shop (more points). Spark handled this one best of the batch, and its table
is fine.

**UFO**: three versions of one story (the UFO drops its abductees and says "Damn it, not again!",
then picks people, not cows, back up while the locals, then the police, then the army shoot at it):
- *UFO Wrong Cargo*: side-scrolling, Defender-style. Hover to beam (the beam takes ~1 s), a cow
  costs points, squad buggies come in to take the people back. This one is the easiest to build
  first: it shares the side view and buggy code with the Spark road-trip SquadBuggy.
- *UFO Low Pass*: third-person chase camera. Flying low lets the beam reach but brings you into
  gun range, and power lines and water towers are in the way. Spark inverted it (a farmer beams
  the UFO). Use the table only.
- *Fellout* (turn-based, AP): your "no idea how that works" answered. Each round the UFO gets 6
  AP at L1 down to 4 at L5. Move 1 cell = 1 AP, shield = 2 AP, beam = all remaining AP and the
  UFO must already be hovering over the person (so beaming leaves you in the open for a whole
  enemy turn: that is the gamble). Then each enemy moves and fires; cover (hay bales, trailers)
  blocks shots. Spark's draft is close (it invented an X key). The opening cartoon plays before
  turn 1 in all three versions.

**Dropped/held:** Bargain Hall (you: skip). Tower Shift (waits for stacked cellmaps).

## Your question about Stair Hopper ("Tomb Raider levels?")

No. Spark's Stair Hopper is a flat **side view**: floors with gaps, a few drifting ledges, and
water rising from below. You climb before the water reaches you. It is a climbing race, not a
maze, and "stairs" is only the name. A Tomb Raider-like version would be a different and bigger
game: 3D block rooms from cellmap v2 heights (ledges, a flooding chamber) with a third-person
camera. Default unless you say otherwise: keep it as the small 2D climb. The 3D flooding-tomb
idea goes on the list for after the LIB_EDITOR cellmap work.

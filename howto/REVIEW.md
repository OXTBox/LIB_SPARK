# LIB_HOWTO outline: Claude's review (2026-11-14)

Two passes, about 12 minutes of Spark in all. Version 1 (`out_v1/`): the format was kept, but
shapes were never placed in the scene, keys were read through the mouse handler, steps repeated
the same call, and every "Needs" said none. Version 2 (`OUTLINE.md`): Claude wrote topic 01 by
hand and Spark was shown it as the model answer, plus seven rules. Much better: every lesson
starts from the same spinning cube, and real sizes, colours and positions are named.

## Verdict per topic (version 2)
| Topic | Verdict | What is wrong |
|---|---|---|
| 01 Game card and loop | KEEP (written by Claude) | - |
| 02 Shapes: built-in | KEEP, small fixes | MeshSphere/Pyramid argument counts; grid should lie flat under the shapes |
| 03 Shapes: by hand | FIX | the vertex list is cut off; start with a triangle (3 vertices, 3 lines), not a cube |
| 04 Objects in the scene | FIX | Entity.Kill needs the key Entity.Spawn returned, not the shape's name; "Needs" lists itself |
| 05 Moving things | FIX | step 4 repeats step 2; velocity is set once, not added to every step |
| 06 Keyboard input | FIX | TestKeys through Game.OnClick again; one press vs held is wrong (it needs a "was down" flag) |
| 07 Mouse and picking | REWRITE | the projectile story is muddled; should be: click, RayCastScene, FX.Sparks on what was hit |
| 08 Camera | REWRITE | fixed / top-down / follow are mixed; should end with the third-person follow from Amazing Couple |
| 09 HUD and text | KEEP, small fixes | add a step that changes the score text from Game.OnUpdate |
| 10 Collisions | FIX | steps 5-6 are wrong (click, camera ray); should be: move the sphere into the cube, Collision.Hit flashes it |
| 11 Effects | FIX | FX.Sparks takes x,y,z,count,colour; FX.Destroy/Particles.Clear steps are filler |
| 12 Game state | FIX | Space read through Game.OnClick; HUD.Set argument order |
| 13 Levels and layouts | REWRITE | the same library call three times; should be: a level-table line, Bit.Maze, walls from Map.BlockEdges |
| 14 Animation: No Bones | KEEP, small fixes | Scene.SetBob arguments; add the mesh swap each frame (Big Ball of Vectors' polyhedron) |
| 15 Animation: BVH | REWRITE (Claude) | Spark doesn't know LIB_MOCAP; the real steps are in Amazing Couple's Couple.LoadClip / Couple.Animate |
| 16 Sound | FIX | Audio.Init on stop is wrong; it needs a sound file named in the step |
| 17 Pause, notes and tests | REWRITE (Claude) | invented hooks; the real ones are Game.OnPause/OnResume, the GameNotes front script, <Prefix>.TestKeys and <Prefix>.State |
| 18 One game, two engines | KEEP, needs a point | it repeats 01; should name what breaks in xt3d (engine globals, focus, fonts) |

Games map and "missing fundamentals": not usable (Spark picked topics 1-4 for nearly every game
and listed our own topics back). Claude will map games to topics by hand from their scripts.

## Proposed next step
Claude fixes and rewrites the outline (the table above) into `LIB_HOWTO/OUTLINE.md`; the owner
reviews that one. Then Spark writes each step's words (from the fixed outline, one step a request)
and Claude writes and headless-tests each step's code.

# LIB_HOWTO: the outline (finished, 2026-11-14)

Step-by-step game building for Vibecode3D (and the xt3d bench): every step adds one handler or
function, and its **Result** is something new on screen. Spark (local model) drafted it in two
passes; Claude corrected every engine call against the engine source and rewrote topics 07, 08,
13, 15 and 17. Spark's drafts: `out_v1/OUTLINE_v1.md`, `out_v1/OUTLINE_spark_v2_owner_result.md`.

Every lesson starts from the same place: a card script, one wire cube (topic 01). Facts used
throughout: +X right, **+Y down (up is minus Y)**, +Z away; about 30 updates a second; script-local
variables (`local sAngle` above the handlers) keep their values between updates.

## Topics (the left-side list)

01. Game card and loop
02. Shapes: built-in meshes
03. Shapes: by hand
04. Objects in the scene
05. Moving things
06. Keyboard input
07. Mouse and picking
08. Camera
09. HUD and text
10. Collisions
11. Effects
12. Game state
13. Levels and layouts
14. Animation: No Bones
15. Animation: BVH
16. Sound
17. Pause, notes and tests
18. One game, two engines

---

# 01 Game card and loop
Goal: one wire cube turns on screen, started and stopped by the engine.
Needs: none

1. An empty game card
   Adding: on Game.OnStart (with Engine.ResetCamera, Scene.ClearAll, HUD.Clear)
   Result: press Play: the viewport is empty and nothing goes wrong. The game runs.
   Engine calls: Game.OnStart, Engine.ResetCamera, Scene.ClearAll, HUD.Clear
2. A shape on screen
   Adding: Mesh.Define "Cube", MeshBox(40,40,40) and put Entity.Spawn("Cube",0,0,600,"cyan") into sCube (600 ahead of the camera), in Game.OnStart
   Result: a cyan wire cube sits in the middle of the view.
   Engine calls: Mesh.Define, MeshBox, Entity.Spawn
3. The loop: move it a little every step
   Adding: on Game.OnUpdate (add 0.05 to sAngle, SetObjectRotation sCube, 0, sAngle, 0)
   Result: the cube turns, about 30 small turns a second.
   Engine calls: Game.OnUpdate, SetObjectRotation
4. Words on screen
   Adding: HUD.Set "Title","SPINNING CUBE",20,120,14 in Game.OnStart
   Result: the title shows below the engine's top bars.
   Engine calls: HUD.Set
5. Clean up when the game stops
   Adding: on Game.OnStop (HUD.Clear)
   Result: press Stop, then Play another game: no old title is left over.
   Engine calls: Game.OnStop, HUD.Clear

Pitfalls:
- Mesh.Define only names a shape; nothing shows until Entity.Spawn puts it in the scene.
- Keep the angle in a script-local variable; a plain local in Game.OnUpdate starts at 0 every step.
- The camera sits at 0,0,0: a shape spawned at z 0 is inside it. Put it ahead (z 400-600).
- Entity.Spawn is a function: `put Entity.Spawn(...) into sKey` or `get Entity.Spawn(...)`, never a bare command.

Games that show it: Simple_Test1

---

# 02 Shapes: built-in meshes
Goal: a row of built-in shapes standing on a grid floor.
Needs: 01

1. A floor
   Adding: Mesh.Define "Floor", MeshGrid(10,10,40); Entity.Spawn("Floor",0,0,0,"#204020")
   Result: a dim green grid lies across the view: the ground.
   Engine calls: Mesh.Define, MeshGrid, Entity.Spawn
2. A box on the floor
   Adding: Mesh.Define "Box", MeshBox(40,40,40); Entity.Spawn("Box",-120,-20,0,"cyan")
   Result: a cyan cube stands on the floor, left of centre (y -20: half its height up).
   Engine calls: MeshBox, Entity.Spawn
3. A ball
   Adding: Mesh.Define "Ball", MeshSphere(22,6,10); Entity.Spawn("Ball",-40,-22,0,"orange")
   Result: an orange wire ball sits next to the cube.
   Engine calls: MeshSphere
4. A pyramid and a prism
   Adding: MeshPyramid(4,24,44) and MeshPrism(6,20,40), spawned at x 40 and 120
   Result: a four-sided pyramid and a six-sided prism complete the row.
   Engine calls: MeshPyramid, MeshPrism
5. Change the numbers
   Adding: MeshSphere(22,3,5) instead of (22,6,10)
   Result: the ball turns into a crude, faceted shape: fewer rings and sides, fewer lines.
   Engine calls: MeshSphere

Pitfalls:
- Up is minus Y: an object at y +20 sinks under the floor.
- The code (LIB_HOWTO/topics/02_*) puts the floor at y 120 and the row at z 420 so it is not seen edge-on.
- MeshSphere's arguments are radius, rings, sides; MeshPyramid and MeshPrism start with the sides.

Games that show it: BigBallOfVectors, VectorBlobApocalypse, ShaftDescent

---

# 03 Shapes: by hand
Goal: a wire shape built point by point: a triangle, then a little house.
Needs: 01, 02

1. A new, empty mesh
   Adding: put Mesh.New() into tM
   Result: nothing on screen yet: an empty shape to fill.
   Engine calls: Mesh.New
2. Three points
   Adding: Mesh.AddVertex tM, -30,0,0 / 30,0,0 / 0,-50,0 (each one's number comes back in the result)
   Result: still nothing: points alone draw nothing.
   Engine calls: Mesh.AddVertex
3. Three lines: a triangle
   Adding: Mesh.AddLine tM,1,2 / 2,3 / 3,1; Mesh.Define "Tri", tM; Entity.Spawn("Tri",0,0,0,"yellow")
   Result: a yellow wire triangle stands in the middle of the view.
   Engine calls: Mesh.AddLine, Mesh.Define, Entity.Spawn
4. A house: a square and a roof
   Adding: four more points for a square below the triangle and four lines around it
   Result: a wire house outline: the triangle is now its roof.
   Engine calls: Mesh.AddVertex, Mesh.AddLine
5. Make it solid-looking
   Adding: Mesh.AddFace tM, "4 5 6 7" (the square as one face)
   Result: the front of the house is drawn as a face, not just its edges.
   Engine calls: Mesh.AddFace

Pitfalls:
- Vertex numbers are the ones Mesh.AddVertex returned (1, 2, 3 ...); a line to a number that was never added draws nothing.
- Faces list their vertex numbers with spaces, in order around the edge.

Games that show it: Face, Thrmnlra, Amazing_Couple (its walls and beacon)

---

# 04 Objects in the scene
Goal: cubes appear where you want them and disappear on purpose.
Needs: 01

1. Keep the key
   Adding: put Entity.Spawn("Cube",0,0,600,"cyan") into sCube (600 ahead of the camera)
   Result: the cube shows, and sCube holds its key (like "Cube_1") to talk to it later.
   Engine calls: Entity.Spawn
2. Many of the same shape
   Adding: a repeat that spawns five cubes at x -160, -80, 0, 80, 160, keys kept in sCubes[n]
   Result: a row of five cubes from one shape definition.
   Engine calls: Entity.Spawn
3. Colours
   Adding: a different colour for each ("red", "#40FF40", ...)
   Result: five colours: the colour belongs to the object, not the shape.
   Engine calls: Entity.Spawn
4. Remove one
   Adding: Entity.Kill sCubes[3] after 60 updates (count sTicks in Game.OnUpdate)
   Result: two seconds in, the middle cube vanishes.
   Engine calls: Entity.Kill
5. Count them
   Adding: HUD.Set "Count", Entity.Count("Cube"), 20,120,14
   Result: the HUD shows 5, then 4.
   Engine calls: Entity.Count, HUD.Set

Pitfalls:
- Entity.Kill needs the key Entity.Spawn returned, not the shape's name.
- Scene.ClearAll at the start of Game.OnStart, so a second Play doesn't add a second row.

Games that show it: SkyRaiders, WallBreaker, DotMaze

---

# 05 Moving things
Goal: a cube that moves by itself, three different ways.
Needs: 01, 04

1. Move it by hand every step
   Adding: add 2 to sX in Game.OnUpdate; SetObjectPosition sCube, sX, 0, 0
   Result: the cube slides to the right.
   Engine calls: SetObjectPosition
2. Bounce at the edges
   Adding: if abs(sX) > 200 then put -sVX into sVX (move by sVX instead of 2)
   Result: the cube slides back and forth.
   Engine calls: SetObjectPosition
3. Let the engine spin it
   Adding: SetObjectRotationSpeed sCube, 0, 0.05, 0 (once, in Game.OnStart)
   Result: it turns while it slides, with no rotation code in the loop.
   Engine calls: SetObjectRotationSpeed
4. Let the engine move it
   Adding: a second cube with SetObjectVelocity tKey, 0, 0, 2 (once)
   Result: the second cube drifts away from you on its own.
   Engine calls: SetObjectVelocity
5. Read where it is
   Adding: HUD.Set "Pos", round(GetObjectPosition(tKey,"Z")), 20,120,14
   Result: the HUD counts up as the second cube drifts.
   Engine calls: GetObjectPosition, HUD.Set

Pitfalls:
- Velocity and rotation speed are set once; setting them every step is not needed.
- Moving by hand (step 1) and by velocity (step 4) on the same object fight each other.

Games that show it: Simple_Test2, demo, Canyon

---

# 06 Keyboard input
Goal: drive the cube with WASD or the arrow keys.
Needs: 01, 05

1. Whose keys are they
   Adding: focus on nothing in Game.OnStart, and an empty "on arrowKey / end arrowKey"
   Result: arrow keys no longer open menus or move field cursors: they belong to the game.
   Engine calls: Game.OnStart
2. Read the keys held down
   Adding: put the keysDown into tKeys in Game.OnUpdate; if 100 or 65363 is among the items of tKeys then add 3 to sX
   Result: hold D (or right arrow) and the cube moves right.
   Engine calls: the keysDown, SetObjectPosition
3. All four directions
   Adding: A 97 / left 65361, W 119 / up 65362 (minus Z: away), S 115 / down 65364
   Result: the cube goes wherever you steer it.
   Engine calls: the keysDown
4. One press, not held
   Adding: Space (32) with a sKeyWas["space"] flag: act only when it goes down
   Result: each tap of Space changes the cube's colour once, however long it's held.
   Engine calls: the keysDown
5. A test hook
   Adding: Cube.Keys() returns sTestKeys when a test set it, else the keysDown; Cube.TestKeys pKeys
   Result: a test (topic 17) can drive the cube without a keyboard.
   Engine calls: the keysDown

Pitfalls:
- Game.OnClick is the mouse; keys are read in Game.OnUpdate.
- Upper and lower case have different codes (w 119, W 87): accept both.

Games that show it: BigBallOfVectors, Amazing_Couple, VectorPong3D

---

# 07 Mouse and picking
Goal: click a rock to blast it.
Needs: 01, 04, 11

1. Something to click
   Adding: five rocks (MeshSphere(20,3,5)) spawned at random places, each with hit points: put 2 into gObjectTransforms[tKey]["hp"] (global gObjectTransforms)
   Result: rough grey rocks are scattered around, each able to take two hits.
   Engine calls: MeshSphere, Entity.Spawn, gObjectTransforms
2. Hear the click
   Adding: on Game.OnClick pX, pY (HUD.Set "Click", pX & "," & pY, 20,120,14)
   Result: every click shows its screen position.
   Engine calls: Game.OnClick, HUD.Set
3. Fire at it
   Adding: Weapon.FireAt pX, pY inside Game.OnClick
   Result: a laser fires from the click; a hit rock sparks white, and the second hit de-rezzes it.
   Engine calls: Weapon.FireAt
4. Know what was hit
   Adding: on Game.OnKill pKey, pX, pY, pZ (add 1 to sScore; FX.Sparks pX,pY,pZ,12,"orange")
   Result: sparks at the rock and the score goes up.
   Engine calls: Game.OnKill, FX.Sparks
5. (deeper) Pick without firing
   Adding: ScreenToCameraRay and RayCastScene(gSceneObjects, ...) to find the object under the mouse
   Result: the rock under the mouse turns yellow before you fire.
   Engine calls: ScreenToCameraRay, RayCastScene

Pitfalls:
- Weapon.FireAt does the hit test for you; ScreenToCameraRay is only needed for picking without shooting.
- Only objects with "hp" can be destroyed; Game.OnKill arrives only when one is (Hunter's rocks work this way).

Games that show it: demo, Hunter, Simple_Test2

---

# 08 Camera
Goal: the same scene seen from a fixed view, from above, and from behind a moving hero.
Needs: 01, 05, 06

1. Where the camera is
   Adding: Engine.SetCam 0, 120, 400 in Game.OnStart (the engine takes the scene's position negated: +Y here lifts the camera)
   Result: the cube grid is seen from in front and a little above.
   Engine calls: Engine.SetCam
2. Where it looks
   Adding: put -atan2(120, 400) into gCameraPitch
   Result: the view tilts down to the middle of the scene.
   Engine calls: gCameraPitch
3. From above
   Adding: Engine.SetCam 0, 420, 300 and put -atan2(420, 340) into gCameraPitch (Big Ball of Vectors)
   Result: a steep top-down view of the whole floor.
   Engine calls: Engine.SetCam, gCameraPitch
4. Turn around the scene
   Adding: add 0.01 to gCameraYaw every update
   Result: the view swings slowly around the scene.
   Engine calls: gCameraYaw
5. Follow the hero
   Adding: every update put the camera behind the steered cube: x - sin(heading)*105, height 88, z - cos(heading)*105; aim with atan2 (Amazing Couple's Couple.Camera)
   Result: a third-person view: the camera stays behind the cube as you steer it.
   Engine calls: Engine.SetCam, gCameraYaw, gCameraPitch
6. Smooth it
   Adding: move the camera only 0.22 of the way to its target each update
   Result: the camera glides after the hero instead of snapping.
   Engine calls: Engine.SetCam

Pitfalls:
- Engine.SetCam takes the scene position negated; Amazing Couple passes -sCamX, -sCamY, -sCamZ.
- Engine.ResetCamera at the start of Game.OnStart, or the last game's camera stays.

Games that show it: Amazing_Couple, BigBallOfVectors, TrenchRun

---

# 09 HUD and text
Goal: a score that counts, a message that comes and goes, help text that stays.
Needs: 01

1. A line of text
   Adding: HUD.Set "Score","SCORE 0", gViewLeft + 20, 120, 14
   Result: SCORE 0 shows below the engine's top bars.
   Engine calls: HUD.Set
2. Make it count
   Adding: add 1 to sScore every 30 updates; HUD.Set "Score","SCORE" && sScore, ...
   Result: the score goes up once a second; setting the same name replaces the text.
   Engine calls: HUD.Set
3. Help at the bottom
   Adding: HUD.Set "Help","ARROWS MOVE   SPACE JUMP", gViewLeft + 20, gViewBottom - 30, 11
   Result: small help text sits at the bottom of the view.
   Engine calls: HUD.Set
4. A message that goes away
   Adding: HUD.Set "Msg","GET READY",200,300,24 at the start; HUD.Remove "Msg" after 60 updates
   Result: GET READY flashes up for two seconds.
   Engine calls: HUD.Set, HUD.Remove
5. Only redraw when it changed
   Adding: keep the last text in sHUDWas; skip HUD.Set when nothing changed
   Result: the same screen, less work every update (Big Ball of Vectors' Ball.ShowHUD).
   Engine calls: HUD.Set

Pitfalls:
- y below about 112, or the text hides under the engine's top bars and the ... menu.
- HUD.Clear in Game.OnStop, or the text follows you into the next game.

Games that show it: BigBallOfVectors, Amazing_Couple, WallBreaker

---

# 10 Collisions
Goal: a ball rolls into a cube and the cube reacts.
Needs: 04, 05, 11

1. Two things on a collision course
   Adding: a cube at x 150 and a ball at x -150 with SetObjectVelocity ball, 2, 0, 0
   Result: the ball rolls towards the cube and passes straight through it.
   Engine calls: Entity.Spawn, SetObjectVelocity
2. Put them in groups
   Adding: Collision.SetGroup sBall,"ball",22 and Collision.SetGroup sCube,"block",28
   Result: nothing changes yet: groups alone don't collide.
   Engine calls: Collision.SetGroup
3. A rule
   Adding: Collision.AddRule "ball","block" (and Collision.ClearRules at the start)
   Result: the engine now checks those two groups every update.
   Engine calls: Collision.AddRule, Collision.ClearRules
4. React to the hit
   Adding: on Collision.Hit pA, pB (FX.Sparks at the cube; SetObjectVelocity sBall, -2, 0, 0)
   Result: sparks fly and the ball bounces back.
   Engine calls: Collision.Hit, FX.Sparks
5. The simple way
   Adding: in Game.OnUpdate, if the distance between ball and cube < 50 then ... (no groups)
   Result: the same bounce from a distance check: often enough for small games.
   Engine calls: GetObjectPosition

Pitfalls:
- The radius in Collision.SetGroup decides how close counts as touching.
- Collision.Hit can arrive several updates in a row while they overlap: move them apart at once.

Games that show it: demo, Hunter, Canyon (rules); BigBallOfVectors, WallBreaker (distance)

---

# 11 Effects
Goal: something happens and you can see it happen.
Needs: 01, 04

1. Sparks
   Adding: FX.Sparks 0, -20, 0, 16, "orange" in Game.OnStart
   Result: a burst of orange sparks at the start.
   Engine calls: FX.Sparks
2. Sparks on a key
   Adding: Space (topic 06) fires FX.Sparks at the cube's position
   Result: every tap of Space bursts sparks from the cube.
   Engine calls: FX.Sparks, GetObjectPosition
3. Destroy it
   Adding: FX.Destroy sCube on Return
   Result: the cube de-rezzes (Tron-style dashes that grow, thin out and fade) and is gone.
   Engine calls: FX.Destroy
4. Debris instead
   Adding: View.Set "explode", "debris" before FX.Destroy (FX.Derez always de-rezzes)
   Result: the next cube bursts into flying edge pieces instead.
   Engine calls: View.Set, FX.Destroy, FX.Derez
5. A clean start
   Adding: Particles.Clear in Game.OnStart
   Result: Play again: no sparks are left over from last time.
   Engine calls: Particles.Clear

Pitfalls:
- FX.Sparks takes x, y, z, count, colour: remember up is minus Y.
- Lots of sparks every update slows everything: burst them on events.

Games that show it: BigBallOfVectors, WallBreaker, CityShield

---

# 12 Game state
Goal: score, lives, levels, a win, a loss, and Space to play again.
Needs: 06, 09, 10

1. The numbers
   Adding: put 0 into sScore, 3 into sLives, 1 into sLevel in Game.OnStart; show them with HUD.Set
   Result: SCORE 0  LIVES 3  LEVEL 1 at the top.
   Engine calls: HUD.Set
2. Change them in play
   Adding: catching something adds to sScore; a hazard takes a life
   Result: the numbers move while you play.
   Engine calls: HUD.Set
3. Over: won or lost
   Adding: sOver and sWon flags; when sLives is 0 or the last level is cleared, stop the play code
   Result: the game freezes with YOU WIN or GAME OVER.
   Engine calls: HUD.Set
4. Play again
   Adding: when sOver and Space (32) is down (and at least 30 updates passed), call Game.OnStart
   Result: Space starts a fresh game; the short wait stops a held Space from skipping the message.
   Engine calls: the keysDown, Game.OnStart
5. One line that says it all
   Adding: function Game.State: return sLevel & "|" & sScore & "|" & sLives & "|" & sOver
   Result: game notes and tests (topic 17) can read the game's state.
   Engine calls: none (your own function)

Pitfalls:
- Read Space in Game.OnUpdate (topic 06), not Game.OnClick.
- Reset every number in Game.OnStart, or Play again keeps the old score.

Games that show it: BigBallOfVectors, WallBreaker, SkyRaiders

---

# 13 Levels and layouts
Goal: levels from a table, and a maze that is the same every time for the same seed.
Needs: 02, 12

1. A level table
   Adding: one line a level: "4,3,1,5" = agents, speed, hazards, quota; put line sLevel of kLevels into tRow
   Result: level 1 uses the first line's numbers; change the numbers, change the level.
   Engine calls: none
2. Next level
   Adding: when the quota is met, Ball.StartLevel sLevel + 1 (clear the scene, read the next line)
   Result: the game gets harder level by level.
   Engine calls: Scene.ClearAll
3. A maze from a seed
   Adding: start using LIB_BIT; put Bit.Maze(6,6,sSeed) into sGrid
   Result: nothing on screen yet: a 13 x 13 grid of 1s (walls) and 0s (floor) in a variable.
   Engine calls: Bit.Maze (LIB_BIT)
4. The maze on screen
   Adding: LIB_MAP's Map.BlockEdges(sGrid, 76, 58, false) -> wall segments -> a wire mesh (Amazing Couple's Couple.SegmentsToMesh)
   Result: a blue wire maze stands on the floor.
   Engine calls: Map.BlockEdges (LIB_MAP), Mesh.New, Mesh.AddVertex, Mesh.AddLine, Entity.Spawn
5. The same maze every time
   Adding: add 1 to sSeed when a maze is cleared
   Result: seed 1 is always the same maze, here and in xt3d and Python; the next seed is a new one.
   Engine calls: Bit.Maze
6. (next) A map drawn by hand
   Adding: CellMap.Read a .cellmap made in LIB_BIT's BitEditor; walls where the tag is "#"
   Result: your own painted level, with doors, traps and heights.
   Engine calls: CellMap.Read (LIB_BIT/editor)

Pitfalls:
- A maze grid is 2 x rooms + 1 wide: 6 rooms make 13 cells.
- Random without a seed gives a different level every run, so a tester can't report "level 3 is too hard".

Games that show it: Amazing_Couple, BigBallOfVectors, DotMaze

---

# 14 Animation: No Bones
Goal: things that look alive with no skeleton: spin, bob, grow, change shape.
Needs: 01, 04, 05

1. Spin
   Adding: SetObjectRotationSpeed sGem, 0, 0.05, 0
   Result: a gem turns slowly forever.
   Engine calls: SetObjectRotationSpeed
2. Bob
   Adding: Scene.SetBob sBuoy, 6, 0.1, 0.05 (height, roll, speed)
   Result: a buoy rises, falls and rocks gently.
   Engine calls: Scene.SetBob
3. Grow
   Adding: every 30 updates: Mesh.Define a bigger MeshSphere, Entity.Kill the old ball, Entity.Spawn the new one
   Result: the ball grows a step at a time.
   Engine calls: Mesh.Define, MeshSphere, Entity.Kill, Entity.Spawn
4. Change shape
   Adding: more sides each time (MeshSphere(r, sides div 2, sides)): Big Ball of Vectors' Ball.Reshape
   Result: a crude polyhedron becomes rounder as it grows (or, in Amazing Couple, loses a side at every bounce).
   Engine calls: MeshSphere
5. A flip-book
   Adding: define 8 meshes at the start ("Wing.1" ... "Wing.8"); each update show the next one (a mesh swap, like Amazing Couple's Couple.SetMesh)
   Result: a wing flaps: frame animation with no bones.
   Engine calls: Mesh.Define

Pitfalls:
- Scene.SetBob bobs around the height the object had when it was called: place it first.
- Redefining a mesh every update is slow: change shape on events or every few updates.

Games that show it: BigBallOfVectors, demo, Amazing_Couple (the ball)

---

# 15 Animation: BVH
Goal: a stick figure that walks and stands still, from motion capture, with feet that don't skate.
Needs: 03, 06, 14

1. The clip file
   Adding: read LIB_MOCAP/library/<clip>/<clip>_stick.txt: the "fps", "travel", "cycle", "joints" and "edges" lines, then one line of numbers a frame (x,y,z a joint)
   Result: nothing on screen yet: the clip is in a variable (a BVH capture, already turned into stick text by LIB_MOCAP).
   Engine calls: none (reading a text file)
2. One pose
   Adding: frame 1 as a mesh: Mesh.AddVertex for each joint (times 30 units a metre, Y negated: up is minus Y), Mesh.AddLine for each edge
   Result: a stick figure stands in the scene.
   Engine calls: Mesh.New, Mesh.AddVertex, Mesh.AddLine, Mesh.Define, Entity.Spawn
3. Every pose
   Adding: one mesh a frame at the start ("Clip.1", "Clip.2" ...), only the frames of its walk cycle
   Result: still one figure, but every pose is ready to show.
   Engine calls: Mesh.Define
4. Play it
   Adding: each update move fps x step time through the frames and swap the figure's mesh (Couple.SetMesh)
   Result: the figure walks on the spot.
   Engine calls: SetObjectPosition
5. Walk forward without skating
   Adding: move forward by the clip's "travel" speed, and play frames at the speed it really moved
   Result: it walks across the floor and its feet stay planted.
   Engine calls: SetObjectPosition, SetObjectRotation
6. Walk and stand
   Adding: a second clip (idle); show idle when the speed is 0, walk when moving (W key)
   Result: it stands and fidgets, then walks when you press W.
   Engine calls: the keysDown

Pitfalls:
- Only the clip's cycle frames loop cleanly; the whole capture jumps at the end.
- Feet skate when the figure moves faster or slower than the clip's "travel": tie the frame rate to the real speed.

Games that show it: Amazing_Couple, GeneticAnomaly

---

# 16 Sound
Goal: a sound when something happens.
Needs: 07 or 10

1. Sound files where the engine looks
   Adding: a folder per sound type in the engine's sounds folder (SoundDirectory()), e.g. "zap" with zap1.wav, zap2.wav
   Result: nothing yet: the engine knows the sounds by their folder names.
   Engine calls: none
2. Load them
   Adding: Audio.Init in Game.OnStart (Game.Play calls it the first time anyway)
   Result: a short LOADING SOUNDS, once.
   Engine calls: Audio.Init
3. Play one on an event
   Adding: Sound.Play "zap" in Game.OnKill (topic 07) or Collision.Hit (topic 10)
   Result: each hit makes a sound; with several files in the folder they take turns.
   Engine calls: Sound.Play
4. No files, no crash
   Adding: nothing: Sound.Play on a type with no files does nothing
   Result: the game runs silently on a machine without the sound folder.
   Engine calls: Sound.Play

Pitfalls:
- The type is the folder name ("zap"), not a file name.
- A sound every update is noise: play on events.

Games that show it: Hunter, Canyon

---

# 17 Pause, notes and tests
Goal: a game that pauses cleanly, takes notes while you play, and can be tested with no window.
Needs: 06, 12

1. Pause
   Adding: on Game.OnPause (HUD.Set "Paused","PAUSED",...) and on Game.OnResume (HUD.Remove "Paused")
   Result: Escape stops the game and shows PAUSED; resuming takes it away.
   Engine calls: Game.OnPause, Game.OnResume, HUD.Set, HUD.Remove
2. A State function
   Adding: function <Prefix>.State returning the game's numbers in one line (topic 12)
   Result: anyone can ask the game what is happening.
   Engine calls: none
3. Notes while you play
   Adding: nothing in the game: press ` or F2 (LIB_GAMES' GameNotes front script)
   Result: a note box opens; your note is saved with the game's State line in LIB_LLMIN/LIB_GAMES/GAME_NOTES.txt.
   Engine calls: none (GameNotes)
4. A test hook
   Adding: <Prefix>.TestKeys pKeys and <Prefix>.Keys() (topic 06)
   Result: a script can hold keys down for the game.
   Engine calls: the keysDown
5. A headless test
   Adding: tools/headless_play.sh <Game> <Prefix> "32:2 65363:60 0:300"
   Result: the game runs with no window, holding keys for so many steps, and prints the State after each: errors show at once.
   Engine calls: none (tools/engine_stubs)

Pitfalls:
- Read keys only through <Prefix>.Keys(), or the tests can't drive the game.
- Keep State short and on one line: it goes into every note and test log.

Games that show it: Amazing_Couple, BigBallOfVectors, Thrmnlra

---

# 18 One game, two engines
Goal: the spinning cube of topic 01 running unchanged in the xt3d bench.
Needs: 01

1. Only engine calls
   Adding: nothing new: use only the calls in these lessons (no buttons or fields of your own on the card)
   Result: the card script has nothing the xt3d bench doesn't also have.
   Engine calls: (all of the above)
2. Positions from the view
   Adding: HUD positions from gViewLeft, gViewTop, gViewRight, gViewBottom instead of fixed numbers
   Result: the HUD lands in the right place in both windows.
   Engine calls: gViewLeft, gViewBottom
3. Keys belong to the game
   Adding: focus on nothing and the empty arrowKey handler (topic 06)
   Result: in both engines the arrows steer the game, not a menu.
   Engine calls: the keysDown
4. Run it in the xt3d bench
   Adding: install the game with LIB_TEST's installer; open it from the bench
   Result: the same cube turns in xt3d; check the speed and that the labels line up.
   Engine calls: none
5. Keep the speed the same
   Adding: Engine.Info("stepMS") for step time instead of assuming 33 ms
   Result: animation and movement run at the same speed in both engines.
   Engine calls: Engine.Info

Pitfalls:
- A control you made by hand on the Vibecode3D card doesn't exist in xt3d.
- Test in both before calling a lesson done.

Games that show it: Thrmnlra, TrenchRun, ProbeVsCone

---

## Games by topic (checked in the scripts)

- 01 Game card and loop: Simple_Test1
- 02 Shapes: built-in meshes: BigBallOfVectors, VectorBlobApocalypse, ShaftDescent
- 03 Shapes: by hand: Face, Thrmnlra, Amazing_Couple
- 04 Objects in the scene: SkyRaiders, WallBreaker, DotMaze
- 05 Moving things: Simple_Test2, demo, Canyon
- 06 Keyboard input: BigBallOfVectors, Amazing_Couple, VectorPong3D
- 07 Mouse and picking: demo, Hunter, Simple_Test2
- 08 Camera: Amazing_Couple, BigBallOfVectors, TrenchRun
- 09 HUD and text: BigBallOfVectors, Amazing_Couple, WallBreaker
- 10 Collisions: demo, Hunter, Canyon; BigBallOfVectors, WallBreaker
- 11 Effects: BigBallOfVectors, WallBreaker, CityShield
- 12 Game state: BigBallOfVectors, WallBreaker, SkyRaiders
- 13 Levels and layouts: Amazing_Couple, BigBallOfVectors, DotMaze
- 14 Animation: No Bones: BigBallOfVectors, demo, Amazing_Couple
- 15 Animation: BVH: Amazing_Couple, GeneticAnomaly
- 16 Sound: Hunter, Canyon
- 17 Pause, notes and tests: Amazing_Couple, BigBallOfVectors, Thrmnlra
- 18 One game, two engines: Thrmnlra, TrenchRun, ProbeVsCone

## Next
1. Owner reviews this outline (order, missing topics, too much or too little in a step).
2. Each step becomes two files in LIB_HOWTO: the words (Spark can expand them) and the code
   (Claude writes it, as small as possible, and checks it compiles and runs headless).
3. The LIB_HOWTO stack shows them: topics on the left, the step's words and code on the right.

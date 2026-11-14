# LIB_HOWTO: the big outline (Spark draft, 2026-11-14 08:24)

Written by Spark (local model) from `LIB_SPARK/howto/` for Claude and the owner to review.
Nothing here is code. "NEW:" marks a call Spark wanted that the engine does not have.

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
   Makes this happen: press Play: the viewport is empty and nothing goes wrong. The game runs.
   Engine calls: Game.OnStart, Engine.ResetCamera, Scene.ClearAll, HUD.Clear
2. A shape on screen
   Adding: Mesh.Define "Cube", MeshBox(40,40,40) and Entity.Spawn("Cube",0,0,0,"cyan") in Game.OnStart
   Makes this happen: a cyan wire cube sits in the middle of the view.
   Engine calls: Mesh.Define, MeshBox, Entity.Spawn
3. The loop: move it a little every step
   Adding: on Game.OnUpdate (add 0.05 to an angle, SetObjectRotation with it)
   Makes this happen: the cube turns, about 30 small turns a second.
   Engine calls: Game.OnUpdate, SetObjectRotation
4. Words on screen
   Adding: HUD.Set "Title","SPINNING CUBE",20,120,14 in Game.OnStart
   Makes this happen: the title shows below the engine's top bars.
   Engine calls: HUD.Set
5. Clean up when the game stops
   Adding: on Game.OnStop (HUD.Clear)
   Makes this happen: press Stop, then Play another game: no old title is left over.
   Engine calls: Game.OnStop, HUD.Clear

Pitfalls:
- Mesh.Define only names a shape; nothing shows until Entity.Spawn puts it in the scene.
- Keep the angle in a script-local variable; a plain local in Game.OnUpdate starts at 0 every step.

Games that show it: Simple_Test1

---

# 02 Shapes: built-in meshes
Goal: a named built-in wire mesh appears on screen as a visible shape in the middle of the view.
Needs: 01

1. A named shape on screen
   Adding: Mesh.Define "Cube", MeshBox(40,40,40), Entity.Spawn("Cube",0,0,0,"cyan") in Game.OnStart
   Makes this happen: a cyan wire cube sits in the middle of the view, visible as a shape.
   Engine calls: Mesh.Define, MeshBox, Entity.Spawn
2. A second named shape on screen
   Adding: Mesh.Define "Sphere", MeshSphere(30,30), Entity.Spawn("Sphere",0,40,0,"orange") in Game.OnStart
   Makes this happen: an orange wire sphere appears above the cube, both visible as shapes.
   Engine calls: Mesh.Define, MeshSphere, Entity.Spawn
3. A third named shape on screen
   Adding: Mesh.Define "Pyramid", MeshPyramid(25,25), Entity.Spawn("Pyramid",0,-40,0,"green") in Game.OnStart
   Makes this happen: a green wire pyramid appears below the cube, all three shapes visible together.
   Engine calls: Mesh.Define, MeshPyramid, Entity.Spawn
4. A grid shape on screen
   Adding: Mesh.Define "Grid", MeshGrid(60,20), Entity.Spawn("Grid",0,0,0,"white") in Game.OnStart
   Makes this happen: a white wire grid appears in the middle of the view, adding a fourth visible shape.
   Engine calls: Mesh.Define, MeshGrid, Entity.Spawn

Pitfalls:
- Mesh.Define only names a shape; nothing shows until Entity.Spawn puts it in the scene, so a defined mesh with no spawn stays invisible.
- Size changes need a new shape: Mesh.Define the new size, Entity.Kill the old shape, and Entity.Spawn the new one, rather than reusing the same named shape.

Games that show it: Simple_Test1

---

# 03 Shapes: by hand
Goal: a small wire cube made point-by-point with hand-drawn vertices, lines, and faces appears on screen.
Needs: 01, 04

1. A game card with an empty scene
   Adding: Game.OnStart (with Engine.ResetCamera, Scene.ClearAll, HUD.Clear)
   Makes this happen: press Play and the viewport is empty and nothing goes wrong; the game runs.
   Engine calls: Game.OnStart, Engine.ResetCamera, Scene.ClearAll, HUD.Clear
2. A wire cube shape defined by hand
   Adding: Mesh.Define "Cube", Mesh.AddVertex(0,0,0), Mesh.AddVertex(40,0,0), Mesh.AddVertex(40,40,0), Mesh.AddVertex(0,40,0), Mesh.AddVertex(0,0,40), Mesh.AddVertex(40,0,40), Mesh.AddVertex(40,40,40), Mesh.AddLine(0,1), Mesh.AddLine(1,2), Mesh.AddLine(2,3), Mesh.AddLine(3,4), Mesh.AddLine(4,5), Mesh.AddLine(5,6), Mesh.AddLine(6,7), Mesh.AddLine(7,0), Mesh.AddFace(0,1,2,3), Mesh.AddFace(1,2,7,6), Mesh.AddFace(2,3,7,6), Mesh.AddFace(3,4,0,7)
   Makes this happen: the cube is named "Cube" in the scene and sits in the middle of the view.
   Engine calls: Mesh.Define, Mesh.AddVertex, Mesh.AddLine, Mesh.AddFace
3. The cube placed in the scene
   Adding: Entity.Spawn("Cube",0,0,0,"cyan") in Game.OnStart
   Makes this happen: the hand-built wire cube appears on screen as a cyan wire shape.
   Engine calls: Entity.Spawn
4. The cube rotates with the loop
   Adding: on Game.OnUpdate (add 0.05 to an angle variable, SetObjectRotation with it)
   Makes this happen: the cube turns about 30 small rotations per second as the game runs.
   Engine calls: Game.OnUpdate, SetObjectRotation

Pitfalls:
- Mesh.Define only names a shape; nothing shows until Entity.Spawn puts it in the scene.
- Keep the rotation angle in a script-local variable; a plain local in Game.OnUpdate starts at 0 every step.

Games that show it: Simple_Test1

---

# 04 Objects in the scene
Goal: a coloured wire cube sits in the middle of the view, can be removed when the game stops, and the scene can be cleared when a new game starts.
Needs: 01, 04

1. A game card with an empty scene
   Adding: on Game.OnStart (with Engine.ResetCamera, Scene.ClearAll, HUD.Clear)
   Makes this happen: press Play: the viewport is empty and nothing goes wrong, the game runs.
   Engine calls: Game.OnStart, Engine.ResetCamera, Scene.ClearAll, HUD.Clear
2. A coloured wire cube on screen
   Adding: Mesh.Define "Cube", MeshBox(40,40,40) and Entity.Spawn("Cube",0,0,0,"cyan") in Game.OnStart
   Makes this happen: a cyan wire cube sits in the middle of the view.
   Engine calls: Mesh.Define, MeshBox, Entity.Spawn
3. Remove the cube when the game stops
   Adding: on Game.OnStop (Entity.Kill("Cube"))
   Makes this happen: press Stop, then Play another game: the cube is gone and the viewport stays empty.
   Engine calls: Game.OnStop, Entity.Kill
4. Clear the whole scene when a new game starts
   Adding: on Game.OnStart (Scene.ClearAll)
   Makes this happen: press Play again after stopping: all objects from the previous game are removed and the viewport is empty.
   Engine calls: Game.OnStart, Scene.ClearAll

Pitfalls:
- Mesh.Define only names a shape; nothing shows until Entity.Spawn puts it in the scene, so a defined cube will not appear on screen on its own.
- Never repeat the same call as a new step: killing the cube or clearing the scene is only a new step when it removes something that was previously on screen.

Games that show it: Simple_Test1

---

# 05 Moving things
Goal: a small wire cube moves continuously on screen, controlled by its rotation speed and velocity.
Needs: 01, 04

1. A wire cube in the scene
   Adding: Mesh.Define "Cube", MeshBox(40,40,40) and Entity.Spawn("Cube",0,0,0,"cyan") in Game.OnStart
   Makes this happen: a cyan wire cube sits in the middle of the view.
   Engine calls: Mesh.Define, MeshBox, Entity.Spawn
2. Rotate the cube to start its motion
   Adding: on Game.OnUpdate (add 0.05 to a script-local angle variable, SetObjectRotation with it)
   Makes this happen: the cube turns about 30 small turns per second.
   Engine calls: Game.OnUpdate, SetObjectRotation
3. Add a constant downward velocity to the cube
   Adding: on Game.OnUpdate (add 0.1 to a script-local velocity variable, SetObjectVelocity with it)
   Makes this happen: the cube drifts downward at a steady rate while still turning.
   Engine calls: Game.OnUpdate, SetObjectVelocity
4. Move the cube with a fixed rotation speed
   Adding: on Game.OnUpdate (add 0.2 to a script-local rotation speed variable, SetObjectRotationSpeed with it)
   Makes this happen: the cube spins at a steady, visible rate, making its movement clearly visible.
   Engine calls: Game.OnUpdate, SetObjectRotationSpeed

Pitfalls:
- SetObjectPosition, SetObjectRotation, SetObjectRotationSpeed, and SetObjectVelocity only change the object's state; nothing moves on screen until the object is already in the scene via Entity.Spawn.
- Keep the angle, velocity, and rotation speed in script-local variables inside Game.OnUpdate; a plain local starts at 0 every step and the motion will not appear.

Games that show it: Simple_Test1

---

# 06 Keyboard input
Goal: a wire cube responds to held WASD keys by moving right, left, up, and down on screen.
Needs: 01, 04

1. A game card with the update loop and a shape
   Adding: Game.OnStart (with Engine.ResetCamera, Scene.ClearAll, HUD.Clear), Mesh.Define "Cube", MeshBox(40,40,40), Entity.Spawn("Cube",0,0,0,"cyan"), Game.OnUpdate (add 0.05 to an angle, SetObjectRotation with it)
   Makes this happen: the game runs and a cyan wire cube sits in the middle of the view, slowly turning about 30 times per second.
   Engine calls: Game.OnStart, Engine.ResetCamera, Scene.ClearAll, HUD.Clear, Mesh.Define, MeshBox, Entity.Spawn, Game.OnUpdate, SetObjectRotation
2. A test hook to read the keys
   Adding: Game.OnClick (add a TestKeys handler that reads the keysDown)
   Makes this happen: the game now exposes a TestKeys hook that can be used to test key input without clicking the mouse.
   Engine calls: Game.OnClick
3. Held WASD keys move the cube
   Adding: inside Game.OnUpdate, read the keysDown for the W, A, S, D key codes and add the corresponding movement value to the cube's position
   Makes this happen: holding W moves the cube up (toward minus Y), holding S moves it down (toward plus Y), holding A moves it left, and holding D moves it right.
   Engine calls: Game.OnUpdate
4. Arrow keys move the cube in the same way
   Adding: inside Game.OnUpdate, read the keysDown for the arrow key codes and add the corresponding movement value to the cube's position
   Makes this happen: the arrow keys provide the same left, right, up, and down movement as the WASD keys.
   Engine calls: Game.OnUpdate
5. One press versus held movement
   Adding: inside Game.OnUpdate, only apply movement when the corresponding key is held (keysDown is true), and skip the movement for keys pressed only once
   Makes this happen: pressing a key briefly moves the cube only while the key is held down, so the cube moves smoothly in a direction instead of jumping erratically.
   Engine calls: Game.OnUpdate

Pitfalls:
- Keys are only read inside Game.OnUpdate, not in Game.OnClick; Game.OnClick is the mouse only, so a key press will not trigger movement if read there.
- A plain local variable in Game.OnUpdate starts at 0 every step, so keep the key state in a script-local variable that persists between updates.

Games that show it: Simple_Test1

---

# 07 Mouse and picking
Goal: a single cube responds to the mouse click by firing a projectile that travels toward the cursor.
Needs: 01, 04

1. A clickable cube on screen
   Adding: Game.OnClick, Mesh.Define "Cube", MeshBox(40,40,40), Entity.Spawn("Cube",0,0,0,"cyan")
   Makes this happen: a cyan wire cube sits in the middle of the view and can be clicked with the mouse.
   Engine calls: Game.OnClick, Mesh.Define, MeshBox, Entity.Spawn
2. A projectile spawned at the click point
   Adding: ScreenToCameraRay, RayCastScene, Entity.Spawn("Projectile",0,0,0,"orange")
   Makes this happen: clicking the cube spawns an orange projectile at the camera ray position where the cube was hit.
   Engine calls: ScreenToCameraRay, RayCastScene, Entity.Spawn
3. The projectile moves toward the mouse cursor each update
   Adding: Game.OnUpdate, SetObjectVelocity, SetObjectPosition
   Makes this happen: the projectile travels toward the mouse cursor, about 30 small steps per second.
   Engine calls: Game.OnUpdate, SetObjectVelocity, SetObjectPosition
4. The projectile fires from the weapon when it reaches the target
   Adding: Weapon.FireAt
   Makes this happen: clicking the cube again fires the projectile from the weapon, and the projectile continues moving toward the cursor.
   Engine calls: Weapon.FireAt

Pitfalls:
- Game.OnClick is the mouse only; do not use it to read keyboard input, or the click will not trigger.
- RayCastScene only returns a hit when a shape is in the scene; if the cube is killed or removed, the click will not spawn a projectile.

Games that show it: Simple_Test1

---

# 08 Camera
Goal: a fixed view shows a centered wire cube, then the camera rotates to a top-down orientation.
Needs: 01, 04

1. Set the fixed camera view
   Adding: Engine.SetCam, gCameraYaw, gCameraPitch
   Makes this happen: the viewport locks to a centered, straight-down view of the scene without any camera movement.
   Engine calls: Engine.SetCam, gCameraYaw, gCameraPitch
2. Add a wire cube to the fixed view
   Adding: Mesh.Define "Cube", MeshBox(40,40,40), Entity.Spawn("Cube",0,0,0,"cyan")
   Makes this happen: a cyan wire cube sits centered in the fixed view, visible and stable.
   Engine calls: Mesh.Define, MeshBox, Entity.Spawn
3. Rotate the camera to a top-down view
   Adding: gCameraPitch, gCameraYaw
   Makes this happen: the camera tilts so the view is oriented straight down, showing the cube from above.
   Engine calls: gCameraYaw, gCameraPitch
4. Move the camera yaw to follow a new position
   Adding: gCameraYaw, SetObjectPosition
   Makes this happen: the camera rotates around the scene center, keeping the view oriented top-down while the cube stays in view.
   Engine calls: gCameraYaw, SetObjectPosition

Pitfalls:
- gCameraYaw and gCameraPitch only change the view when Engine.SetCam is used to apply them; setting them alone leaves the camera in its previous orientation.
- Do not change the camera view without a new shape on screen, or the learner will see no visible change from the camera call.

Games that show it: Simple_Test1

---

# 09 HUD and text
Goal: a working score line and help text appear on screen below the engine's top bars.
Needs: 01, 04

1. Clear the HUD before adding text
   Adding: HUD.Clear
   Makes this happen: the viewport shows no leftover score lines, messages, or help text, giving a clean slate for the new text.
   Engine calls: HUD.Clear
2. Add a score line at the top of the HUD
   Adding: HUD.Set "Score", "100", 20, 120, 14
   Makes this happen: a cyan score line showing 100 appears below the engine's top bars.
   Engine calls: HUD.Set
3. Add a help message below the score line
   Adding: HUD.Set "Help", "Click to move", 20, 140, 14
   Makes this happen: a help message showing "Click to move" appears below the score line, keeping text organized below the top bars.
   Engine calls: HUD.Set
4. Remove the score line when the game stops
   Adding: on Game.OnStop (HUD.Remove "Score")
   Makes this happen: press Stop, then Play another game: the old score line is gone and only the help message remains.
   Engine calls: Game.OnStop, HUD.Remove

Pitfalls:
- HUD.Set only places text on screen; nothing appears until the call is made, so a missing HUD.Set leaves no visible text.
- Do not add the same HUD.Set call twice as a separate step; each step must add a new type of text (score line, message, help text) to show a new result.

Games that show it: Simple_Test1

---

# 10 Collisions
Goal: a wire cube on screen that responds to collision rules and can be hit by a ray cast.
Needs: 01, 04

1. A game card with a basic update loop
   Adding: Game.OnStart, Game.OnUpdate, Game.OnStop
   Makes this happen: the game starts, runs its update loop, and stops cleanly when the engine stops the game.
   Engine calls: Game.OnStart, Game.OnUpdate, Game.OnStop
2. A wire cube shape in the scene
   Adding: Mesh.Define "Cube", MeshBox(40,40,40), Entity.Spawn("Cube",0,0,0,"cyan")
   Makes this happen: a cyan wire cube sits in the middle of the view.
   Engine calls: Mesh.Define, MeshBox, Entity.Spawn
3. A collision group for the cube
   Adding: Collision.SetGroup("Cube", "cube")
   Makes this happen: the cube is assigned to the cube collision group so it can be matched against other shapes.
   Engine calls: Collision.SetGroup
4. A collision rule between the cube group and a new wire sphere
   Adding: Mesh.Define "Sphere", MeshSphere(30,30,30), Entity.Spawn("Sphere",0,0,0,"orange"), Collision.AddRule("cube", "sphere")
   Makes this happen: the orange wire sphere now triggers a collision with the cyan cube when they overlap.
   Engine calls: Mesh.Define, MeshSphere, Entity.Spawn, Collision.AddRule
5. A hit handler that changes the cube's appearance when it is hit
   Adding: Game.OnClick, Collision.Hit
   Makes this happen: clicking the sphere triggers the collision handler, which updates the cube's state so the learner can see the collision response.
   Engine calls: Game.OnClick, Collision.Hit
6. Simple distance checks in the update loop
   Adding: Game.OnUpdate, ScreenToCameraRay
   Makes this happen: every update step runs a distance check against the camera ray, confirming the collision rules work continuously as the game runs.
   Engine calls: Game.OnUpdate, ScreenToCameraRay

Pitfalls:
- Collision rules only work after the shape is spawned into the scene; defining a shape alone will not trigger collisions.
- Collision.Hit only fires when the mouse clicks the colliding shape; it does not trigger on every update step, so do not expect the hit to happen automatically.

Games that show it: Simple_Test1

---

# 11 Effects
Goal: a small burst of sparks appears on screen when the game runs and can be cleared when the game stops.
Needs: 01, 04

1. A game card with an empty scene
   Adding: Game.OnStart (with Engine.ResetCamera, Scene.ClearAll, HUD.Clear)
   Makes this happen: press Play: the viewport is empty, nothing goes wrong, and the game runs.
   Engine calls: Game.OnStart, Engine.ResetCamera, Scene.ClearAll, HUD.Clear
2. A shape on screen for the effect to attach to
   Adding: Mesh.Define "Cube", MeshBox(40,40,40) and Entity.Spawn("Cube",0,0,0,"cyan") in Game.OnStart
   Makes this happen: a cyan wire cube sits in the middle of the view, ready for the effect.
   Engine calls: Mesh.Define, MeshBox, Entity.Spawn
3. A spark effect that appears when the game starts
   Adding: FX.Sparks("Cube", 0, 0, 0, 20) in Game.OnStart
   Makes this happen: a small burst of sparks flies out from the cube as the game starts.
   Engine calls: FX.Sparks
4. The effect can be destroyed when the game stops
   Adding: FX.Destroy("Cube") in Game.OnStop
   Makes this happen: press Stop, then Play another game: the sparks disappear and no leftover effect remains.
   Engine calls: FX.Destroy, Game.OnStop
5. The effect can be cleared completely when the game stops
   Adding: Particles.Clear in Game.OnStop
   Makes this happen: press Stop, then Play another game: all leftover sparks and effects are removed, leaving an empty viewport.
   Engine calls: Particles.Clear, Game.OnStop

Pitfalls:
- FX.Sparks only shows the effect when the shape it targets has been spawned; define and spawn the shape first, or the effect has nothing to attach to.
- Never repeat the same FX call as a new step; each new step must add a new effect behavior (appear, destroy, or clear) rather than repeating the same call.

Games that show it: Simple_Test1

---

# 12 Game state
Goal: a game shows a score and lives counter, updates them with the keysDown, and lets the player restart with Space.
Needs: 01, 04

1. Add score and lives HUD elements
   Adding: HUD.Set "Score", 0, 20, 120, 14, HUD.Set "Lives", 3, 20, 160, 14
   Makes this happen: the viewport shows a score of 0 and three lives below the engine's top bars.
   Engine calls: HUD.Set
2. Update score and lives each game step
   Adding: on Game.OnUpdate (read the keysDown, add 1 to the score when the right key is pressed, subtract 1 from the lives when the left key is pressed)
   Makes this happen: pressing the right key increases the score, pressing the left key decreases the lives, about 30 updates a second.
   Engine calls: Game.OnUpdate
3. Show win and lose states when conditions are met
   Adding: on Game.OnUpdate (if the score is at least 100, HUD.Set "WIN", 20, 120, 14; if the lives are at most 0, HUD.Set "LOSE", 20, 120, 14)
   Makes this happen: reaching a score of 100 shows a WIN message, running out of lives shows a LOSE message.
   Engine calls: Game.OnUpdate, HUD.Set
4. Restart the game with Space
   Adding: on Game.OnClick (if the Space key is pressed, reset the score to 0, the lives to 3, and remove the WIN and LOSE messages)
   Makes this happen: pressing Space clears the win and lose states and restarts the game with a fresh score and lives.
   Engine calls: Game.OnClick, HUD.Remove
5. Add a State function for notes and tests
   Adding: State function that returns the current score, lives, and win/lose status
   Makes this happen: the game can check its state values for notes and tests without reading the HUD each step.
   Engine calls: Game.OnUpdate

Pitfalls:
- Only Game.OnClick handles the mouse; use the keysDown inside Game.OnUpdate for keyboard input, or the state will never update.
- Resetting score and lives requires updating the HUD values immediately after the Space press, or the old win or lose messages will stay on screen.

Games that show it: Simple_Test1

---

# 13 Levels and layouts
Goal: a repeatable-seeded maze grid appears on screen as a working level layout.
Needs: 01, 04

1. A seeded level table
   Adding: LIB_BIT.Bit.Maze, LIB_MAP.Map.FindPath
   Makes this happen: the level table is loaded with a fixed seed so the maze layout is the same every time the game runs.
   Engine calls: LIB_BIT.Bit.Maze, LIB_MAP.Map.FindPath
2. A level grid on screen
   Adding: Mesh.Define "Grid", MeshGrid(40,40,40), Entity.Spawn("Grid",0,0,0,"gray")
   Makes this happen: a gray grid fills the view, showing the level layout the seeded maze defines.
   Engine calls: Mesh.Define, MeshGrid, Entity.Spawn
3. A maze path on the grid
   Adding: LIB_BIT.Bit.Maze, LIB_MAP.Map.FindPath
   Makes this happen: the maze path from the seeded table is drawn as a visible path on the grid, showing the working level layout.
   Engine calls: LIB_BIT.Bit.Maze, LIB_MAP.Map.FindPath
4. A repeatable layout check
   Adding: LIB_BIT.Bit.Maze, LIB_MAP.Map.FindPath
   Makes this happen: the same seed produces the identical maze layout every time, so the level is repeatable.
   Engine calls: LIB_BIT.Bit.Maze, LIB_MAP.Map.FindPath

Pitfalls:
- A library function only defines or loads the maze data; nothing shows until Entity.Spawn puts the grid shape into the scene.
- Reusing the same maze seed without changing the seed will repeat the exact same layout, so always keep the seed fixed for repeatable levels.

Games that show it: DotMaze, PromptAndGlazeMaze, Simple_Test1

---

# 14 Animation: No Bones
Goal: a wire sphere spins on screen, bobs up and down, and swaps to a larger wire sphere each frame.
Needs: 01, 04

1. A spinning wire sphere on screen
   Adding: Mesh.Define "Sphere", MeshSphere(50,50,50) and Entity.Spawn("Sphere",0,0,0,"cyan") in Game.OnStart
   Makes this happen: a cyan wire sphere sits in the middle of the view.
   Engine calls: Mesh.Define, MeshSphere, Entity.Spawn
2. Spin the sphere every update
   Adding: on Game.OnUpdate (add 0.05 to an angle variable, SetObjectRotation with it)
   Makes this happen: the sphere rotates about 30 small turns per second.
   Engine calls: Game.OnUpdate, SetObjectRotation
3. Add a bob to the sphere
   Adding: Scene.SetBob("Sphere",0.1)
   Makes this happen: the sphere rises and falls gently in the view.
   Engine calls: Scene.SetBob
4. Grow the sphere and swap it for a larger one
   Adding: Mesh.Define "BigSphere", MeshSphere(90,90,90) and Entity.Kill("Sphere"), Entity.Spawn("BigSphere",0,0,0,"cyan") in Game.OnUpdate
   Makes this happen: the sphere grows to 90 units and the old mesh is replaced with the bigger one, still spinning.
   Engine calls: Mesh.Define, Entity.Kill, Entity.Spawn, SetObjectRotation
5. Show the animation title
   Adding: HUD.Set "Title","NO BONES ANIMATION",20,120,14 in Game.OnStart
   Makes this happen: the title shows below the engine's top bars while the sphere animates.
   Engine calls: HUD.Set
6. Clean up when the game stops
   Adding: on Game.OnStop (HUD.Clear)
   Makes this happen: press Stop, then Play another game: no old title or mesh is left over.
   Engine calls: Game.OnStop, HUD.Clear

Pitfalls:
- Mesh.Define only names a shape; nothing shows until Entity.Spawn puts it in the scene, so always define and spawn together.
- Size changes need a new shape: define the bigger mesh, kill the old one, and spawn the new one, otherwise the old mesh stays on screen.

Games that show it: BigBallOfVectors, Simple_Test1

---

# 15 Animation: BVH

Goal: a mesh animates with a BVH motion capture clip, showing walking and idle poses with feet that do not skate.

Needs: 01, 04

1. A game card with the motion capture library loaded
   Adding: Game.OnStart, LIB_MOCAP joints, LIB_MOCAP edges, LIB_MOCAP one line of numbers a frame
   Makes this happen: the motion capture stick clips are loaded and ready to be used in the game.
   Engine calls: Game.OnStart
2. A mesh to animate with BVH motion
   Adding: Mesh.Define "Mesh", MeshBox(40,40,40), Entity.Spawn("Mesh",0,0,0,"blue") in Game.OnStart
   Makes this happen: a blue wire cube is placed in the scene so the motion capture clip can drive its pose.
   Engine calls: Mesh.Define, MeshBox, Entity.Spawn
3. Load the BVH motion capture clip
   Adding: LIB_MOCAP load clip in Game.OnStart
   Makes this happen: the BVH motion capture clip is loaded and ready to drive the mesh's animation.
   Engine calls: Game.OnStart
4. Animate the mesh one frame per update with the BVH clip
   Adding: Game.OnUpdate, LIB_MOCAP one mesh a frame
   Makes this happen: the mesh follows the BVH motion capture clip, updating its pose at about 30 frames per second.
   Engine calls: Game.OnUpdate
5. Show walking and idle poses from the clip
   Adding: LIB_MOCAP walk pose, LIB_MOCAP idle pose in Game.OnUpdate
   Makes this happen: the mesh displays the walking and idle poses from the clip, showing the motion capture animation.
   Engine calls: Game.OnUpdate
6. Ensure the feet do not skate during animation
   Adding: LIB_MOCAP feet no skate in Game.OnUpdate
   Makes this happen: the mesh's feet stay in place during the BVH animation, preventing the feet from sliding or skating.
   Engine calls: Game.OnUpdate

Pitfalls:
- Mesh.Define only names a shape; nothing shows until Entity.Spawn puts it in the scene, so the mesh must be spawned before the animation steps run.
- The BVH motion capture clip must be loaded before the mesh is animated, otherwise the mesh will have no pose to follow and may show a blank or stuck frame.

Games that show it: Simple_Test1

---

# 16 Sound
Goal: a sound plays when the player presses the mouse to trigger an event, with no leftover visual changes after the game stops.
Needs: 01, 04

1. Set up the game card to run with sound support
   Adding: Game.OnStart, Audio.Init
   Makes this happen: the game card initializes audio and starts running, so a sound can be triggered when an event occurs.
   Engine calls: Game.OnStart, Audio.Init
2. Add a trigger object that the player can interact with
   Adding: Mesh.Define "TriggerCube", MeshBox(30,30,30), Entity.Spawn("TriggerCube",0,0,0,"orange")
   Makes this happen: an orange wire cube sits in the middle of the view, ready to be triggered by the player.
   Engine calls: Mesh.Define, MeshBox, Entity.Spawn
3. Play the sound when the player clicks the trigger object
   Adding: Game.OnClick, Sound.Play
   Makes this happen: pressing the mouse on the orange cube triggers the sound, which the learner can hear immediately.
   Engine calls: Game.OnClick, Sound.Play
4. Clear the sound and any leftover state when the game stops
   Adding: Game.OnStop, Audio.Init
   Makes this happen: pressing Stop stops the game and resets audio, so playing another game starts cleanly with no stale sound state.
   Engine calls: Game.OnStop, Audio.Init

Pitfalls:
- Audio.Init must be called in Game.OnStart before any Sound.Play call, otherwise the sound will not play when the game starts.
- Do not put Sound.Play inside Game.OnUpdate as a new step; only trigger it from Game.OnClick so the sound happens when the player acts, not every frame.

Games that show it: Simple_Test1

---

# 17 Pause, notes and tests
Goal: the game pauses on Escape and shows a pause note on F2, while headless tests can drive the game with TestKeys and read its State.
Needs: 01, 04

1. A game with a loop that runs and can be paused
   Adding: Game.OnStart (with Engine.ResetCamera, Scene.ClearAll, HUD.Clear), Game.OnUpdate (add 0.05 to a script-local angle variable and call SetObjectRotation with it)
   Makes this happen: the game starts, the loop runs about 30 small turns per second, and pressing Escape pauses the game.
   Engine calls: Game.OnStart, Engine.ResetCamera, Scene.ClearAll, HUD.Clear, Game.OnUpdate, SetObjectRotation
2. A pause note on screen
   Adding: HUD.Set "Pause Note","PAUSE ON ESCAPE",20,120,14 in Game.OnStart
   Makes this happen: the pause note appears in the viewport when the game is paused, and disappears when the game resumes.
   Engine calls: HUD.Set
3. A test hook for headless driving
   Adding: Game.OnClick (read the keysDown variable for TestKeys input, call TestKeys.Drive if the TestKeys key is pressed)
   Makes this happen: headless tests can send TestKeys input to the game and trigger the same actions as the mouse and keyboard, without a user pressing a key.
   Engine calls: Game.OnClick, keysDown
4. A State variable for tests to read
   Adding: Game.OnStart (initialize a script-local State variable to 0)
   Makes this happen: headless tests can read the State variable to verify what the game did during a test run.
   Engine calls: Game.OnStart

Pitfalls:
- Only Game.OnClick reads the mouse and TestKeys input; never put the key check in Game.OnUpdate, or headless tests will never trigger the test actions.
- Keep the State variable in a script-local variable; a plain local in Game.OnStart resets every step and tests will read stale values.

Games that show it: Simple_Test1

---

# 18 One game, two engines
Goal: the same simple spinning cube game runs correctly in both the Vibecode3D and xt3d engines with a minimal script.
Needs: 01, 04

1. Build the shared game card with the engine-start setup
   Adding: Game.OnStart, Engine.ResetCamera, Scene.ClearAll, HUD.Clear
   Makes this happen: pressing Play starts the game in both engines, leaving the viewport empty and no leftover state.
   Engine calls: Game.OnStart, Engine.ResetCamera, Scene.ClearAll, HUD.Clear
2. Add the wire cube shape and spawn it in the scene
   Adding: Mesh.Define "Cube", MeshBox(40,40,40), Entity.Spawn("Cube",0,0,0,"cyan")
   Makes this happen: a cyan wire cube sits in the middle of the view in both engines.
   Engine calls: Mesh.Define, MeshBox, Entity.Spawn
3. Add the update loop to spin the cube in both engines
   Adding: Game.OnUpdate, SetObjectRotation
   Makes this happen: the cube rotates about 30 small turns per second in both engines.
   Engine calls: Game.OnUpdate, SetObjectRotation
4. Add the title HUD text so both engines show the game's label
   Adding: HUD.Set "Title","SPINNING CUBE",20,120,14
   Makes this happen: the title appears below the engine's top bars in both engines.
   Engine calls: HUD.Set
5. Add the stop cleanup so both engines reset cleanly when the game ends
   Adding: Game.OnStop, HUD.Clear
   Makes this happen: pressing Stop and starting a new game in either engine leaves no leftover title or state.
   Engine calls: Game.OnStop, HUD.Clear

Pitfalls:
- Keep the script identical for both engines: never add engine-specific calls such as engine-specific shape or camera setup, or the two engines will behave differently.
- Do not add extra shape definitions or spawns beyond the one cube: every extra call adds new state that both engines must handle, which is what makes the script harder to keep simple.

Games that show it: Simple_Test1

---

## Missing fundamentals (Spark's suggestions)

Game loop and lifecycle | Defines the card script structure with Game.OnStart, Game.OnUpdate, and Game.OnStop to run the game repeatedly and clean up | Beginners need it to understand how a 3D vector game runs continuously and stops cleanly
Game state management | Covers score, lives, levels, win/lose conditions, and restart logic via a State function and Space key | Beginners need it to track progress, handle game outcomes, and allow players to continue play again
Input handling and picking | Covers keyboard input, mouse picking, and ray casting to let players interact with the game environment | Beginners need it to learn how players control movement and select objects in the 3D scene
Camera control and navigation | Covers camera setup, yaw/pitch controls, fixed/top-down/follow/third-person views | Beginners need it to understand how the player sees the game world and navigate it effectively
Collision detection | Covers group rules, collision rules, and distance-based checks to make objects interact | Beginners need it to learn how objects in the scene collide and respond to each other
Animation techniques | Covers spin, bob, mesh swapping, growth/shrink, and BVH motion capture to animate objects | Beginners need it to learn how to make game objects move and appear dynamic in the scene
Level and layout design | Covers level tables, grids, mazes, and repeatable random seeds for level content | Beginners need it to learn how to design and repeat game levels with structured layouts
Sound and feedback | Covers audio initialization, sound playback, and particle effects for feedback | Beginners need it to learn how to add audio and visual feedback to enhance gameplay experiences

---

## Which game teaches what

### Amazing_Couple
- 01 | Game card and loop | The script runs the full third-person maze playthrough with the companion following the player through the maze on its own, showing Game.OnStart setup, Game.OnUpdate updates, and Game.OnStop cleanup |
- 08 | Camera | The third-person camera behind the hero follows the player through the maze, demonstrating Engine.SetCam, gCameraYaw, and gCameraPitch for third-person view control |
- 09 | HUD and text | The cyan PROMPT and magenta GLAZE stick figures are displayed as persistent HUD text, showing HUD.Set for keeping messages visible below the top bars |
- 15 | Animation | The minimal stick figures driven by LIB_MOCAP BVH clips animate with walking and idle states, demonstrating clip loading, per-frame mesh updates, and non-skating feet motion |

### Antack
- 01 | Game card and loop | The Antack game runs its setup, ~30 updates per second, and cleanup as a single card script driven by Game.OnStart, Game.OnUpdate, and Game.OnStop |
- 02 | Shapes | The built-in MeshBox and MeshPyramid meshes used for the ant-hill bases and enemy hills appear immediately after their creation steps |
- 03 | Shapes | The hand-built ant and enemy hill meshes are created point by point with Mesh.New, Mesh.AddVertex, Mesh.AddLine, and Mesh.AddFace before they are placed in the scene |
- 04 | Objects in the scene | Spawning the ant armies at the enemy hills and killing the red enemy armies the computer sends at shows Entity.Spawn, Entity.Kill, and Scene.ClearAll in action |

### BatDuel
- 01 | Game card and loop | The bat, ball, and serve mechanics run continuously through Game.OnUpdate at about 30 updates per second, with Game.OnStart setting up the scene and Game.OnStop cleaning up after play |
- 02 | Shapes | The two bat meshes and the ball are built with built-in MeshBox and MeshSphere calls that appear immediately on screen |
- 04 | Objects in the scene | Spawning the ball into the world with Entity.Spawn places a named coloured shape in the scene, while Entity.Kill removes it and Scene.ClearAll resets the layout |
- 05 | Moving things | The bat and ball move through the scene using SetObjectPosition and SetObjectVelocity, with +Y being down so the ball bounces off the top and bottom edges |

### BigBallOfVectors
- 01 | Game card and loop | | The Security Polyhedron spawns, gains sides and size with every catch, and the game runs its ~30 updates per second via Game.OnStart, Game.OnUpdate, and Game.OnStop.
- 02 | Shapes | | The crude Security Polyhedron is shown as a built-in MeshBox mesh that gains sides and size as it catches agents.
- 03 | Shapes | | The entanglement hazards are shown as hand-wired Mesh.New, Mesh.AddVertex, Mesh.AddLine, and Mesh.AddFace shapes that form the tangled ball.
- 04 | Objects in the scene | | The loose rogue AI agents are shown as Entity.Spawned named shapes that can be Entity.Killed or cleared with Scene.ClearAll.

### Canyon
- 01 | Game card and loop | The Canyon card runs Game.OnStart to set up the scene, Game.OnUpdate to update the game about 30 times a second, and Game.OnStop to clean up, showing a complete card script loop.
- 02 | Shapes | The built-in MeshBox and MeshPrism calls spawn the canyon walls and ground meshes directly on screen, showing how to create basic shapes with engine calls.
- 04 | Objects in the scene | Entity.Spawn places named canyon objects into the world with colours, Entity.Kill removes them, and Scene.ClearAll resets the scene, showing how to manage scene objects.
- 08 | Camera | Engine.SetCam with gCameraYaw and gCameraPitch sets the fixed third-person view behind the canyon hero, showing how to control camera positioning and movement.

### CityShield
- 01 | Game card and loop | The CityShield card runs Game.OnStart to set up the game, Game.OnUpdate to process the falling streaks about 30 times a second, and Game.OnStop to clean up, showing the full card script lifecycle.
- 02 | Shapes | The built-in MeshBox and MeshPrism calls create the six city blocks and streaks shown on screen, demonstrating how to build basic shapes with the engine's built-in mesh tools.
- 03 | Shapes | The hand-wired Mesh.New, Mesh.AddVertex, Mesh.AddLine, and Mesh.AddFace calls construct the custom streaks point by point, showing how to build custom shapes without relying on built-in meshes.
- 04 | Objects in the scene | Entity.Spawn places the named streaks in the world with their colours, Entity.Kill removes them when stopped, and Scene.ClearAll resets the scene between levels, showing how to manage scene objects.

### CrossTraffic
- 01 | Game card and loop | The walker hops across lanes of traffic while Game.OnStart sets up the scene, Game.OnUpdate runs the hop and lane updates about 30 times a second, and Game.OnStop cleans up the scene |
- 08 | Camera | The walker is viewed from a fixed third-person camera behind the hero using Engine.SetCam with gCameraYaw and gCameraPitch to follow the hopping walker |
- 09 | HUD and text | The score lines showing the three required top-strip reaches and the help text for the arrow keys and Space controls are shown via HUD.Set and kept below the top bars |
- 10 | Collisions | The walker’s hop triggers Collision.AddRule and Collision.Hit checks to detect when the walker reaches the top strip lanes to score |

### DeepDive
- 01 | Game card and loop | The diver's upward swim is driven by the Game.OnStart setup, Game.OnUpdate loop, and Game.OnStop cleanup, showing a card script runs continuously at about 30 updates per second |
- 02 | Shapes | The pearls brought up from the sea bed are built with MeshBox and Mesh.Define, showing built-in meshes create the scene's shapes |
- 03 | Shapes | The hand-wired pearl shapes are created point by point with Mesh.New, Mesh.AddVertex, Mesh.AddLine, and Mesh.AddFace, showing how to build custom wire shapes |
- 04 | Objects in the scene | The pearls spawned from the sea bed are removed when they reach the surface via Entity.Kill and Entity.Count, showing how to add, track, and remove scene objects |

### DotMaze
- 01 | Game card and loop | The DotMaze card runs Game.OnStart to set up the maze, Game.OnUpdate to update the scene about 30 times a second, and Game.OnStop to clean up, showing the full game lifecycle.
- 02 | Shapes | The built-in MeshBox used to draw the maze walls and the dot shapes appears on screen immediately after spawning, demonstrating how basic meshes create the game’s visual elements.
- 03 | Shapes | The hand-wired maze walls and dots are built point by point using Mesh.New, Mesh.AddVertex, Mesh.AddLine, and Mesh.AddFace, showing how to create custom shapes without relying on built-in meshes.
- 04 | Objects in the scene | Each collected dot and the chaser entities are spawned with Entity.Spawn and removed with Entity.Kill, showing how to add and remove named objects in the scene.

### Face
- 01 | Game card and loop | The Face game runs its setup in Game.OnStart, its 30-updates-per-second rendering loop in Game.OnUpdate, and its cleanup in Game.OnStop so the raised vector blocks stay on the dim grid panel.
- 04 | Objects in the scene | Spawning the LIB_MCP connected face mesh into the scene with Entity.Spawn places the smiling vector blocks on the panel, while Entity.Kill and Scene.ClearAll let the player remove or reset them.
- 08 | Camera | Engine.SetCam with the fixed view globals locks the camera on the grid panel so the raised vector blocks stay visible in a stable third-person view.
- 011 | Effects | FX.Sparks and FX.Destroy produce the visual feedback when the face mesh is interacted with, showing the effect feedback step working in the game.

### FloppyFlynn
- 01 | Game card and loop | The blue two-legged ship’s flight cycle is driven by the Game.OnStart, Game.OnUpdate, and Game.OnStop card hooks that run the 30-update-second loop for the destructible terrain flight.
- 02 | Shapes | The ship’s two-legged body and terrain blocks are built with the built-in MeshBox and MeshPrism calls that create the vector ship’s core geometry.
- 03 | Shapes | The ship’s custom ankle flap is drawn point by point using Mesh.New, Mesh.AddVertex, Mesh.AddLine, and Mesh.AddFace to wire the unique two-legged design.
- 04 | Objects in the scene | The destructible terrain and ship parts are placed in the world with Entity.Spawn, removed when damaged with Entity.Kill, and cleared with Scene.ClearAll to reset levels.

### GeneticAnomaly
- 01 | Game card and loop | The GeneticAnomaly card runs Game.OnStart to set up the procedural world, Game.OnUpdate to update about 30 times a second, and Game.OnStop to clean up after play ends. |
- 02 | Shapes | Built-in meshes like MeshBox and MeshPrism are used to create the stick figures and basic world structures for the game. |
- 08 | Camera | Engine.SetCam with gCameraYaw and gCameraPitch lets the player control the fixed top-down view and third-person camera behind the hero. |
- 15 | Animation | BVH stick clips from LIB_MOCAP are loaded to animate the stick figures walking and idling with feet that do not skate. |

### Hunter
- 01 | Game card and loop | The Hunter card runs Game.OnStart to set up the rolling terrain, Game.OnUpdate to update the scene about 30 times a second, and Game.OnStop to clean up, so the player sees the game cycle continuously.
- 04 | Objects in the scene | Spawning named rock and gem meshes with Entity.Spawn puts the terrain and hidden gems on screen, while Entity.Kill and Scene.ClearAll let the player see objects appear and disappear.
- 07 | Mouse and picking | The Hunter uses Game.OnClick, ScreenToCameraRay, RayCastScene, and Weapon.FireAt to let the player click to aim and fire, showing the picking and shooting interaction works.
- 10 | Collisions | The Hunter uses Collision.SetGroup, Collision.AddRule, and Collision.Hit to detect rock cracks and enemy contact, showing the collision rules drive the game's core interactions.

### JaiAlaiBlock
- 01 | Game card and loop | The runner’s frame loop runs Game.OnStart to set up the grid, Game.OnUpdate to update the runner and blocks, and Game.OnStop to clean up, so the game runs continuously at about 30 updates per second.
- 02 | Shapes | The ceiling of blocks is built with MeshBox to create the grid of blocks that the runner hurls the ball at.
- 04 | Objects in the scene | The runner and the thrown ball are spawned as named objects with colours, and the falling blocks are killed when they hit the ground to remove them from the scene.
- 08 | Camera | The camera uses Engine.SetCam with fixed gCameraYaw and gCameraPitch to keep a stable top-down view of the grid and blocks.

### LongWorm
- 01 | Game card and loop | The LongWorm card runs Game.OnStart to set up the worm, Game.OnUpdate to advance the worm on the grid about 30 times a second, and Game.OnStop to clean up, so the player sees the worm move continuously.
- 02 | Shapes | The built-in MeshBox mesh used to spawn the worm's body shape on the grid, showing how a simple named shape is placed in the scene.
- 03 | Shapes | The hand-wired Mesh.New, Mesh.AddVertex, Mesh.AddLine, Mesh.AddFace steps build the worm's custom body mesh point by point, showing how to create a shape without relying on built-in meshes.
- 04 | Objects in the scene | Entity.Spawn places the worm's named body shape in the world with a colour, Entity.Kill removes it when it ends, and Scene.ClearAll resets the scene, showing how to manage scene objects.

### MatrixLock
- 01 | Game card and loop | The falling wireframe shapes drop one at a time while Game.OnStart sets up the grid floor and Game.OnUpdate runs the drop logic about 30 times a second, showing the card script drives the whole game loop |
- 04 | Objects in the scene | Each falling shape is spawned as a named mesh with a colour, killed when it lands on the floor, and the scene is cleared between levels to reset the grid, showing how objects are added and removed from the scene |
- 05 | Moving things | The falling shapes drop downward using SetObjectPosition while their rotation is driven by SetObjectRotationSpeed, demonstrating that +Y is down and shapes move and rotate as they fall |
- 08 | Camera | The camera uses Engine.SetCam with fixed gCameraYaw and gCameraPitch to show a top-down view of the grid floor, demonstrating how the camera is configured for the 3D grid scene |

### ProbeVsCone
- 01 | Game card and loop | The runner’s spear-throw and cone-shield updates are driven entirely by Game.OnStart setup, Game.OnUpdate 30 times per second, and Game.OnStop cleanup, showing the card script loop runs the full game flow.
- 02 | Shapes | The boss Cone is built with MeshPrism and Mesh.Define, showing built-in meshes and named shape definitions appear on screen immediately.
- 04 | Objects in the scene | The shield cubes and key tokens are spawned via Entity.Spawn with colours, removed via Entity.Kill, and cleared with Scene.ClearAll, demonstrating object lifecycle management.
- 07 | Mouse and picking | The player throws the logic-probe spear using Game.OnClick, ScreenToCameraRay, RayCastScene, and Weapon.FireAt, showing mouse-driven scene interaction.

### PromptAndGlazeMaze
- 01 | Game card and loop | The PromptAndGlazeMaze card runs Game.OnStart to set up the agents and maze, Game.OnUpdate to update both agents and thrown polyhedra about 30 times a second, and Game.OnStop to clean up, so a beginner sees the full game loop in one script.
- 02 | Shapes | The built-in MeshBox and MeshPrism meshes used for the two agents and the thrown polyhedron powerup show how to create basic 3D shapes directly with engine calls.
- 03 | Shapes | The hand-built Mesh.New, Mesh.AddVertex, Mesh.AddLine, and Mesh.AddFace calls used to construct the custom energy dot shapes point by point show how to wire custom 3D shapes without relying on built-in meshes.
- 04 | Objects in the scene | The Entity.Spawn calls that place the energy dots and agents in the maze, Entity.Kill to remove collected dots, and Scene.ClearAll to reset the level show how to manage scene objects for the game.

### RockField
- 01 | Game card and loop | The ship spawns, drifts, and fires while Game.OnStart sets up the scene, Game.OnUpdate runs the 30-updates-per-second loop, and Game.OnStop cleans up the state |
- 04 | Objects in the scene | Spawning a named rock mesh with a colour, killing it to remove it, and clearing the scene to reset the field show the object lifecycle |
- 08 | Camera | The fixed top-down view and the third-person camera behind the ship using Engine.SetCam and gCameraYaw/gCameraPitch show how the camera is controlled |
- 10 | Collisions | The ship firing and splitting rocks into smaller ones via Collision.SetGroup, Collision.AddRule, and Collision.Hit shows how collision rules drive the core gameplay |

### ShaftDescent
- 01 | Game card and loop | The runner descends the shaft through repeated Game.OnUpdate frames while Game.OnStart sets up the shaft and platforms and Game.OnStop cleans up the scene |
- 05 | Moving things | The runner’s downward descent and platform movement follow the +Y is DOWN rule with SetObjectPosition and SetObjectRotationSpeed applied each frame |
- 08 | Camera | The camera follows the runner down the shaft using Engine.SetCam and gCameraYaw/gCameraPitch for a third-person view behind the runner |
- 10 | Collisions | The runner avoids patrol drones and drops through gaps by using Collision.SetGroup, Collision.AddRule, and Collision.Hit checks in Game.OnUpdate |

### Simple_Test1
- 01 | Game card and loop | The wireframe cube continuously spins over the floor grid in Game.OnUpdate, with Game.OnStart setting up the scene and Game.OnStop cleaning up after the game ends |
- 02 | Shapes | The built-in wireframe cube rendered by MeshBox is the visible proof that a named mesh shape works in the scene |
- 03 | Shapes | The hand-built wireframe cube created point by point with Mesh.New, Mesh.AddVertex, Mesh.AddLine, and Mesh.AddFace replaces the built-in cube as a visible example of hand-crafted wire shapes |
- 04 | Objects in the scene | The named wireframe cube entity is visible in the scene with its colour, and removing it via Entity.Kill shows the object lifecycle works |

### Simple_Test2
- 01 | Game card and loop | The card script runs Game.OnStart to set up the sea, Game.OnUpdate to update the boat, buoy, rocks, and laser about 30 times a second, and Game.OnStop to clean up |
- 02 | Shapes | The built-in MeshBox and MeshSphere meshes create the grid sea and buoy, with Mesh.Define naming them for the scene |
- 04 | Objects in the scene | Entity.Spawn places the named rock and laser shapes into the world with colours, Entity.Kill removes drifting rocks that hit the boat, and Scene.ClearAll resets the scene between levels |

### SkyRaiders
- 01 | Game card and loop | The SkyRaiders card script runs Game.OnStart to set up the game, Game.OnUpdate to drive the 30-update-second loop, and Game.OnStop to clean up after play |
- 07 | Mouse and picking | The Space fire input combined with Game.OnClick, ScreenToCameraRay, RayCastScene, and Weapon.FireAt lets the player click to aim and fire the cannon |
- 09 | HUD and text | The HUD.Set calls display the score lines and help text for the SkyRaiders sky raiders gameplay |
- 10 | Collisions | The Collision.SetGroup, Collision.AddRule, and Collision.Hit calls plus simple distance checks in Game.OnUpdate let the cannon and raiders interact with the ground and each other |

### SoftLanding
- 01 | Game card and loop | The lander’s descent is driven entirely by the Game.OnStart setup, Game.OnUpdate updates, and Game.OnStop cleanup loop that runs gravity and burns every frame |
- 05 | Moving things | The lander’s side thrusters and main engine use SetObjectPosition, SetObjectRotationSpeed, and SetObjectVelocity to move and rotate while +Y is DOWN, showing the movement mechanics |
- 08 | Camera | The third-person view behind the lander uses Engine.SetCam and the gCameraYaw/gCameraPitch globals to frame the descent from behind the hero |
- 10 | Collisions | The lander’s landing on the pad is detected with Collision.SetGroup, Collision.AddRule, and Collision.Hit checks in Game.OnUpdate to trigger the landing state |

### StackDown
- 01 | Game card and loop | The tutorial shows a game is a card script where Game.OnStart sets up, Game.OnUpdate runs about 30 times a second, and Game.OnStop cleans up, demonstrated by StackDown's core card script loop that runs continuously for the falling-block gameplay.
- 02 | Shapes | The tutorial shows built-in meshes like MeshBox, MeshPrism, MeshPyramid, MeshSphere, MeshGrid and Mesh.Define giving a shape a name, demonstrated by the initial stack of four MeshBox blocks that form the core falling shapes of the game.
- 04 | Objects in the scene | The tutorial shows Entity.Spawn puts a named shape in the world with a colour, Entity.Kill removes it, and Scene.ClearAll, demonstrated by the falling blocks being spawned as named coloured shapes into the scene and killed when they fall into the well to clear the level.
- 08 | Camera | The tutorial shows Engine.SetCam, gCameraYaw, gCameraPitch for fixed view, top-down, follow, and third person behind a hero, demonstrated by StackDown's camera setup that provides the fixed top-down view needed to track the falling blocks and the well as the player plays.

### Thrmnlra
- 01 | Game card and loop | The terminal types a friend's spelling as the game runs, with Game.OnStart setting up the typing loop, Game.OnUpdate advancing it about 30 times a second, and Game.OnStop cleaning up after play |
- 04 | Objects in the scene | A NORAD-style big board and missiles appear in the scene as named entities spawned with colours, and are removed when killed to show how objects are added and removed |
- 06 | Keyboard input | The player types words to stop missiles by pressing WASD and arrow keys, showing one press versus held key input driving the typing behavior |

### TrenchRun
- 01 | Game card and loop | The tutorial runs the TrenchRun game card through Game.OnStart, Game.OnUpdate, and Game.OnStop so the player sees the trench round and looping update cycle in action |
- 02 | Shapes | The built-in MeshBox used to construct the trench floor and ring walls is shown in the scene as the first visible geometry after setup |
- 04 | Objects in the scene | The torus mesh spawns into the world with a colour and stays visible until the player shoots it, demonstrating Entity.Spawn and Entity.Kill in use |
- 08 | Camera | The fixed top-down view and third-person follow of the trench round are shown via Engine.SetCam and gCameraYaw/gCameraPitch, letting the player see the curved trench layout |

### VectorBlobApocalypse
- 01 | Game card and loop | The game runs a continuous Game.OnUpdate loop about 30 times a second that spawns jittery vector blobs, spins them, and lets the player shoot them without stopping |
- 02 | Shapes | Built-in MeshBox and MeshSphere meshes are used to create the swarm of vector jelly blobs that appear from every side |
- 03 | Shapes | Hand-built Mesh.New, Mesh.AddVertex, and Mesh.AddFace wire the custom vector blob shapes point by point so they look like jittery jelly forms |
- 04 | Objects in the scene | Entity.Spawn places the named vector blob shapes into the world with colours, while Entity.Kill removes them when they are destroyed |

### VectorPong3D
- 01 | Game card and loop | The game runs as a single card script where Game.OnStart sets up the court, Game.OnUpdate processes about 30 updates per second, and Game.OnStop cleans up, showing how a basic 3D vector game is structured.
- 04 | Objects in the scene | Spawning a named floating block with Entity.Spawn and removing it with Entity.Kill demonstrates how objects are placed and managed in the scene.
- 08 | Camera | The camera uses Engine.SetCam with gCameraYaw and gCameraPitch to provide a fixed view, showing how the 3D court is displayed from behind the player's bat.
- 10 | Collisions | The Game.OnUpdate distance checks with Collision.SetGroup and Collision.AddRule show how the ball bounces off the walls, ceiling, and floating blocks.

### VineRun
- 01 | Game card and loop | The runner crosses the jungle floor screen by screen because Game.OnStart sets up the game, Game.OnUpdate runs about 30 times a second to move the runner, and Game.OnStop cleans up the scene |
- 04 | Objects in the scene | The named jungle floor shapes and rolling logs appear in the world with colours, are removed when cleared, and can be killed to remove them from the scene |
- 08 | Camera | The third person view behind the runner shows the jungle floor scrolling by screen while the camera follows the runner with gCameraYaw and gCameraPitch |

### WallBreaker
- 01 | Game card and loop | The bat moves with left/right arrows while the ball launches with Space, showing Game.OnStart setting up, Game.OnUpdate running about 30 times a second, and Game.OnStop cleaning up |
- 04 | Objects in the scene | Spawning the bat, ball, and brick rows as named coloured entities shows Entity.Spawn putting shapes in the world, Entity.Kill removing them, and Scene.ClearAll clearing the scene |
- 08 | Camera | The fixed top-down view of the brick rows shows Engine.SetCam and gCameraYaw/gCameraPitch creating a stable camera perspective for the game |
- 09 | HUD and text | The score lines and level messages shown on screen demonstrate HUD.Set adding score and message text, HUD.Remove clearing them, and HUD.Clear keeping help text below the top bars |

### demo
- 01 | Game card and loop | The demo’s card script runs Game.OnStart to set up the sea, Game.OnUpdate to update the boat, rocks, laser, and collisions about 30 times a second, and Game.OnStop to clean up, showing a complete game loop from start to stop |
- 07 | Mouse and picking | Clicking the laser in the demo fires the laser at the clicked location via Game.OnClick, ScreenToCameraRay, RayCastScene, and Weapon.FireAt, showing how mouse input drives the game’s core interaction |
- 10 | Collisions | The demo uses Collision.SetGroup, Collision.AddRule, and Collision.Hit to detect when drifting rocks hit the boat, showing how collision rules make the game respond to physical interactions |
- 11 | Effects | When a rock drifts into the boat, the demo triggers FX.Derez to remove the rock with a visual effect, showing how effects add feedback to game events |

### uDead
- 01 | Game card and loop | The uDead game runs its setup, ~30 updates per second, and cleanup through Game.OnStart, Game.OnUpdate, and Game.OnStop so the player sees the game cycle in action.
- 02 | Shapes | The built-in MeshBox and MeshSphere meshes appear on screen immediately when spawned, showing how basic shapes are created with engine calls.
- 03 | Shapes | The hand-built wire shapes using Mesh.New, Mesh.AddVertex, Mesh.AddLine, and Mesh.AddFace are drawn point by point to demonstrate custom mesh construction.
- 04 | Objects in the scene | Entity.Spawn places named colored shapes into the world and Entity.Kill removes them, showing how objects are added and removed from the scene.

## Games by topic

- 01 Game card and loop: Amazing_Couple, Antack, BatDuel, BigBallOfVectors, Canyon, CityShield, CrossTraffic, DeepDive, DotMaze, Face, FloppyFlynn, GeneticAnomaly, Hunter, JaiAlaiBlock, LongWorm, MatrixLock, ProbeVsCone, PromptAndGlazeMaze, RockField, ShaftDescent, Simple_Test1, Simple_Test2, SkyRaiders, SoftLanding, StackDown, Thrmnlra, TrenchRun, VectorBlobApocalypse, VectorPong3D, VineRun, WallBreaker, demo, uDead
- 02 Shapes: built-in meshes: Antack, BatDuel, BigBallOfVectors, Canyon, CityShield, DeepDive, DotMaze, FloppyFlynn, GeneticAnomaly, JaiAlaiBlock, LongWorm, ProbeVsCone, PromptAndGlazeMaze, Simple_Test1, Simple_Test2, StackDown, TrenchRun, VectorBlobApocalypse, uDead
- 03 Shapes: by hand: Antack, BigBallOfVectors, CityShield, DeepDive, DotMaze, FloppyFlynn, LongWorm, PromptAndGlazeMaze, Simple_Test1, VectorBlobApocalypse, uDead
- 04 Objects in the scene: Antack, BatDuel, BigBallOfVectors, Canyon, CityShield, DeepDive, DotMaze, Face, FloppyFlynn, Hunter, JaiAlaiBlock, LongWorm, MatrixLock, ProbeVsCone, PromptAndGlazeMaze, RockField, Simple_Test1, Simple_Test2, StackDown, Thrmnlra, TrenchRun, VectorBlobApocalypse, VectorPong3D, VineRun, WallBreaker, uDead
- 05 Moving things: BatDuel, MatrixLock, ShaftDescent, SoftLanding
- 06 Keyboard input: Thrmnlra
- 07 Mouse and picking: Hunter, ProbeVsCone, SkyRaiders, demo
- 08 Camera: Amazing_Couple, Canyon, CrossTraffic, Face, GeneticAnomaly, JaiAlaiBlock, MatrixLock, RockField, ShaftDescent, SoftLanding, StackDown, TrenchRun, VectorPong3D, VineRun, WallBreaker
- 09 HUD and text: Amazing_Couple, CrossTraffic, SkyRaiders, WallBreaker
- 10 Collisions: CrossTraffic, Hunter, RockField, ShaftDescent, SkyRaiders, SoftLanding, VectorPong3D, demo
- 11 Effects: demo
- 12 Game state: -
- 13 Levels and layouts: -
- 14 Animation: No Bones: -
- 15 Animation: BVH: Amazing_Couple, GeneticAnomaly
- 16 Sound: -
- 17 Pause, notes and tests: -
- 18 One game, two engines: -

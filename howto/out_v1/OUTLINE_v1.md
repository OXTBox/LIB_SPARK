# LIB_HOWTO: the big outline (Spark draft, 2026-11-14 08:18)

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
Goal: A small 3D vector game runs on a card script with a working start, update, and stop loop that displays a simple animated 3D shape.
Needs: none

1. Create the game card script with the Game.OnStart, Game.OnUpdate, and Game.OnStop handlers
   Adding: Game.OnStart, Game.OnUpdate, Game.OnStop
   Makes this happen: The card script is set up so it can run the game loop, but nothing is displayed yet.
   Engine calls: Game.OnStart, Game.OnUpdate, Game.OnStop

2. Initialize the game scene and camera in Game.OnStart
   Adding: Engine.ResetCamera, Scene.ClearAll
   Makes this happen: The 3D scene is cleared and the camera is reset to a default position, preparing the game for rendering.
   Engine calls: Engine.ResetCamera, Scene.ClearAll

3. Create a simple 3D shape in Game.OnStart
   Adding: Mesh.New, MeshBox
   Makes this happen: A small box mesh is added to the scene and appears on screen as the first visible element of the game.
   Engine calls: Mesh.New, MeshBox

4. Run the game loop in Game.OnUpdate to animate the shape
   Adding: Game.OnUpdate
   Makes this happen: The shape updates about 30 times per second, showing the working loop that drives the game.
   Engine calls: Game.OnUpdate

5. Clean up the scene in Game.OnStop
   Adding: Game.OnStop
   Makes this happen: When the game stops, the scene is cleared and the game loop ends, leaving a clean state for the next run.
   Engine calls: Game.OnStop

Pitfalls:
- Forgetting to define all three handlers (Game.OnStart, Game.OnUpdate, Game.OnStop) will cause the game loop to fail to start or stop properly, and the shape will not animate.
- Adding too many engine calls in a single step will make the change too large and hide the result of each individual step, so keep each step to the smallest change needed.

Games that show it: Simple_Test1, demo, VectorBlobApocalypse

---

# 02 Shapes: built-in meshes
Goal: A named 3D shape is displayed on screen as a visible working mesh.
Needs: none

1. Creating the first mesh shape
   Adding: Mesh.New, Mesh.Define
   Makes this happen: A new named mesh is added to the scene and appears as a visible 3D shape on screen.
   Engine calls: Mesh.New, Mesh.Define

2. Adding a box shape to the scene
   Adding: MeshBox
   Makes this happen: A box mesh is created and added to the scene, displaying a new rectangular 3D shape on screen.
   Engine calls: MeshBox

3. Adding a prism shape to the scene
   Adding: MeshPrism
   Makes this happen: A prism mesh is created and added to the scene, displaying a new triangular prism 3D shape on screen.
   Engine calls: MeshPrism

4. Adding a pyramid shape to the scene
   Adding: MeshPyramid
   Makes this happen: A pyramid mesh is created and added to the scene, displaying a new triangular pyramid 3D shape on screen.
   Engine calls: MeshPyramid

5. Adding a sphere shape to the scene
   Adding: MeshSphere
   Makes this happen: A sphere mesh is created and added to the scene, displaying a new round 3D shape on screen.
   Engine calls: MeshSphere

6. Adding a grid shape to the scene
   Adding: MeshGrid
   Makes this happen: A grid mesh is created and added to the scene, displaying a new grid 3D shape on screen.
   Engine calls: MeshGrid

Pitfalls:
- Forgetting to call Mesh.Define before adding a shape may cause the mesh to appear blank or not render, so always name the shape first before adding it to the scene.
- Adding multiple shapes without clearing the scene first can cause overlapping shapes to hide earlier shapes, so ensure the scene is cleared before adding each new shape.

Games that show it: Simple_Test1, demo, VectorBlobApocalypse

---

# 03 Shapes: by hand
Goal: a small wire 3D shape made point by point from the Vibecode3D engine
Needs: none

1. Creating the base mesh
   Adding: Mesh.New
   Makes this happen: a new empty 3D mesh is created and ready to hold vertices, lines, and faces.
   Engine calls: Mesh.New

2. Adding the first vertex to the mesh
   Adding: Mesh.AddVertex
   Makes this happen: the first point of the shape is added to the mesh, giving it a starting position on screen.
   Engine calls: Mesh.AddVertex

3. Adding the first line to the mesh
   Adding: Mesh.AddLine
   Makes this happen: a line is drawn between the first vertex and a second point, showing the first edge of the shape.
   Engine calls: Mesh.AddLine

4. Adding the first face to the mesh
   Adding: Mesh.AddFace
   Makes this happen: a triangle face is added using the existing vertices, completing the first small working shape on screen.
   Engine calls: Mesh.AddFace

5. Adding more vertices to extend the shape
   Adding: Mesh.AddVertex
   Makes this happen: additional vertices are added around the shape, growing it into a larger wire figure.
   Engine calls: Mesh.AddVertex

6. Adding more lines and faces to finish the shape
   Adding: Mesh.AddLine, Mesh.AddFace
   Makes this happen: more edges and faces are added to connect the extended vertices, producing a complete small wire 3D shape.
   Engine calls: Mesh.AddLine, Mesh.AddFace

Pitfalls:
- Adding vertices out of order: vertices must be added in sequence so the lines and faces have valid connections, or the shape will appear broken or missing parts.
- Forgetting to connect vertices with lines: adding only vertices and faces without lines will leave the shape as disconnected points and faces with no visible edges.
- Adding faces with incorrect vertex references: faces must reference existing vertices that were added earlier, or the mesh will fail to render the face correctly.

Games that show it: Face, Simple_Test1, Simple_Test2:

---

# 04 Objects in the scene
Goal: A small named 3D shape appears in the scene with a colour, and can be removed or cleared from the scene.
Needs: none

1. Adding a coloured shape to the scene
   Adding: Entity.Spawn
   Makes this happen: A new named shape is placed in the world and appears on screen in its assigned colour.
   Engine calls: Entity.Spawn
2. Removing the added shape from the scene
   Adding: Entity.Kill
   Makes this happen: The previously added named shape is removed and disappears from the scene.
   Engine calls: Entity.Kill
3. Clearing all objects from the scene
   Adding: Scene.ClearAll
   Makes this happen: Every object currently in the scene is removed, leaving nothing on screen except the base scene.
   Engine calls: Scene.ClearAll

Pitfalls:
- Forgetting to assign a colour when spawning the shape will leave it with the default scene colour, so check the visible colour matches your intended colour before moving on.
- Spawning the shape without naming it will prevent you from targeting it later with Entity.Kill, so always include the name in the spawn call.
- Calling Scene.ClearAll before spawning the shape will remove the shape immediately, so perform the clear step only after the shape has been added.

Games that show it: Simple_Test1, demo, VectorBlobApocalypse

---

# 05 Moving things
Goal: A small 3D object moves smoothly across the scene while its rotation and velocity change over time.
Needs: none

1. Spawning a movable 3D object
   Adding: Entity.Spawn
   Makes this happen: A small 3D object appears in the center of the scene and is ready to be moved.
   Engine calls: Entity.Spawn

2. Setting the object's initial position
   Adding: SetObjectPosition
   Makes this happen: The newly spawned object is placed at a fixed starting position in the scene.
   Engine calls: SetObjectPosition

3. Starting the object's rotation
   Adding: SetObjectRotation
   Makes this happen: The object begins rotating around its vertical axis, showing its orientation change.
   Engine calls: SetObjectRotation

4. Adding rotation speed to the object
   Adding: SetObjectRotationSpeed
   Makes this happen: The object's rotation speed increases, so its rotation becomes faster over time.
   Engine calls: SetObjectRotationSpeed

5. Adding movement velocity to the object
   Adding: SetObjectVelocity
   Makes this happen: The object starts moving across the scene in a straight line, with its position changing continuously.
   Engine calls: SetObjectVelocity

Pitfalls:
- Forgetting to set the object's starting position before adding velocity will cause the object to move from an undefined location, making the movement hard to see.
- Setting rotation speed or velocity too high will make the object move or rotate too quickly, hiding the movement effect and making it hard for beginners to track.

Games that show it: VectorBlobApocalypse, VectorPong3D, demo

---

# 06 Keyboard input
Goal: A small working 3D game that responds to held and pressed keyboard keys with visible movement.
Needs: none

1. Setting up the keyboard input hook
   Adding: Game.OnClick, keysDown
   Makes this happen: The game registers its keyboard input handler so key presses and key holds are tracked for later use.
   Engine calls: Game.OnClick

2. Adding the TestKeys hook for keyboard testing
   Adding: Game.OnClick
   Makes this happen: A TestKeys handler is added to the game so tests can trigger and inspect keyboard input directly.
   Engine calls: Game.OnClick

3. Adding key code handling for WASD and arrow keys
   Adding: keysDown
   Makes this happen: The keyboard handler maps WASD and arrow key codes to movement inputs, enabling directional movement when keys are pressed or held.
   Engine calls: keysDown

4. Adding movement logic for held keys
   Adding: keysDown
   Makes this happen: The handler applies movement based on held keys, showing the player moving in the selected direction as keys are held down.
   Engine calls: keysDown

5. Adding one press versus held key detection
   Adding: keysDown
   Makes this happen: The handler distinguishes between a single key press and a key held down, so the game can react to both types of input correctly.
   Engine calls: keysDown

Pitfalls:
- Forgetting to map arrow keys to movement directions will leave the game unresponsive to arrow key input, so always verify the key code mappings in the handler.
- Confusing a key press with a key hold will cause the game to move erratically or stop moving, so track key state separately for pressed and held keys.

Games that show it: Simple_Test1, Simple_Test2, VectorPong3D:

---

# 07 Mouse and picking
Goal: A small 3D scene where clicking with the mouse selects and fires a projectile at the clicked object.
Needs: none

1. Set up the 3D scene and camera
   Adding: Game.OnStart
   Makes this happen: The Vibecode3D engine starts the game and prepares the 3D scene for mouse interactions.
   Engine calls: Game.OnStart

2. Add the mouse picking handlers
   Adding: Game.OnClick, ScreenToCameraRay, RayCastScene
   Makes this happen: The game now responds to mouse clicks by converting the click position into a 3D ray and casting it against the scene.
   Engine calls: Game.OnClick, ScreenToCameraRay, RayCastScene

3. Add the weapon firing handler
   Adding: Weapon.FireAt
   Makes this happen: Clicking on an object in the scene now fires the projectile at the clicked 3D position.
   Engine calls: Weapon.FireAt

Pitfalls:
- Forgetting to set up the camera before casting rays will cause the ray to miss all objects, so the scene appears empty even though the click handlers are added.
- Casting the ray without clearing the scene first can leave stale collision or object data, making the click fire at the wrong target.

Games that show it: Simple_Test1, VectorPong3D, demo

---

# 08 Camera
Goal: a small working 3D scene with a fixed view, a top-down view, and a third-person camera following a hero on screen
Needs: none

1. Setting up the fixed view
   Adding: Game.OnStart
   Makes this happen: the game starts and the camera is positioned to show a fixed view of the scene
   Engine calls: Engine.ResetCamera, Engine.SetCam

2. Changing the camera yaw to rotate the fixed view
   Adding: Game.OnUpdate
   Makes this happen: the fixed view rotates as the camera yaw changes, showing a new orientation of the same scene
   Engine calls: gCameraYaw

3. Adjusting the camera pitch to tilt the fixed view
   Adding: Game.OnUpdate
   Makes this happen: the fixed view tilts upward or downward as the camera pitch changes, showing a new angle of the scene
   Engine calls: gCameraPitch

4. Switching to a top-down view
   Adding: Game.OnClick
   Makes this happen: the camera rotates to a top-down orientation, showing the scene from directly above
   Engine calls: gCameraYaw, gCameraPitch

5. Creating a hero and setting up third-person follow
   Adding: Entity.Spawn, SetObjectPosition, SetObjectRotation, SetObjectRotationSpeed, SetObjectVelocity
   Makes this happen: a hero entity is spawned in the scene and the camera begins following the hero from behind
   Engine calls: Entity.Spawn, SetObjectPosition, SetObjectRotation, SetObjectRotationSpeed, SetObjectVelocity

6. Adjusting the third-person camera position to follow the hero
   Adding: Game.OnUpdate
   Makes this happen: the camera continuously moves to stay behind and above the hero as the hero moves, showing a third-person view of the scene
   Engine calls: gCameraYaw, gCameraPitch, GetObjectPosition, SetObjectPosition

Pitfalls:
- Forgetting to reset the camera before changing its orientation will leave the camera in an invalid state, so always call Engine.ResetCamera first when starting a new view.
- Changing the camera yaw or pitch without updating the view globals will cause the camera to jump or show a blank view, so always pair camera global changes with the view globals when switching views.

Games that show it: DeepDive, Hunter, VectorBlobApocalypse:

---

# 09 HUD and text
Goal: A working HUD with a score line, a message, and help text displayed below the top bars on screen.
Needs: none

1. Setting up the HUD base layer
   Adding: HUD.Set
   Makes this happen: A blank HUD layer is created and placed below the top bars so it can hold score lines, messages, and help text.
   Engine calls: HUD.Set

2. Adding the score line
   Adding: HUD.Set
   Makes this happen: A score line is added to the HUD layer and appears at the top of the display area.
   Engine calls: HUD.Set

3. Adding the message text
   Adding: HUD.Set
   Makes this happen: A message text is added to the HUD layer and appears below the score line.
   Engine calls: HUD.Set

4. Adding the help text
   Adding: HUD.Set
   Makes this happen: Help text is added to the HUD layer and appears below the message text, keeping all HUD content below the top bars.
   Engine calls: HUD.Set

5. Clearing the HUD layer to reset it
   Adding: HUD.Clear
   Makes this happen: The HUD layer is cleared so all previously added score lines, messages, and help text are removed, leaving a clean HUD ready for new content.
   Engine calls: HUD.Clear

Pitfalls:
- Adding HUD content above the top bars: This places text in the wrong area and makes the score line, message, or help text overlap with the top bars instead of staying below them.
- Forgetting to clear the HUD layer after adding content: This leaves stale score lines, messages, or help text from earlier steps visible, confusing the learner about what the current game state shows.

Games that show it: Simple_Test1, demo, VectorBlobApocalypse

---

# 10 Collisions
Goal: A small 3D scene where two collidable shapes interact with each other and respond to collision detection.
Needs: none

1. Setting up collision groups and rules
   Adding: Collision.SetGroup, Collision.AddRule
   Makes this happen: Two distinct shapes are assigned collision groups and a collision rule is added so the engine can detect when they overlap.
   Engine calls: Collision.SetGroup, Collision.AddRule
2. Creating the collidable shapes
   Adding: Mesh.New, MeshBox
   Makes this happen: Two simple 3D boxes are created and placed in the scene so they can be tested against the collision rules.
   Engine calls: Mesh.New, MeshBox
3. Adding collision detection to the game update loop
   Adding: Game.OnUpdate, Collision.Hit
   Makes this happen: The game update loop is hooked to run collision checks each frame so overlapping shapes trigger the collision response.
   Engine calls: Game.OnUpdate, Collision.Hit
4. Handling collision overlap in the update loop
   Adding: Game.OnUpdate
   Makes this happen: When the shapes overlap, the update loop resolves the collision by moving the shapes apart so they no longer intersect.
   Engine calls: Game.OnUpdate

Pitfalls:
- Forgetting to add a collision rule between the two shapes will leave the engine unable to detect overlaps, so the shapes will never trigger the collision response.
- Adding the collision check to the wrong handler (such as Game.OnStart or Game.OnStop) will cause the collision to only run once at startup or when the game stops, instead of every frame during gameplay.

Games that show it: ProbeVsCone, WallBreaker, demo:

---

# 11 Effects
Goal: A visible particle effect appears on screen after a trigger event, showing feedback from an action.
Needs: none

1. Initializing the effects system and clearing existing particles
   Adding: FX.Sparks, Particles.Clear
   Makes this happen: All existing particles on the screen are removed, leaving a clean scene for the new effect.
   Engine calls: FX.Sparks, Particles.Clear
2. Spawning a small particle effect to demonstrate feedback
   Adding: FX.Sparks
   Makes this happen: A small burst of particles appears on the screen, showing the effects system is active.
   Engine calls: FX.Sparks
3. Triggering the particle effect with a simple event to confirm it responds to input
   Adding: Game.OnClick
   Makes this happen: Clicking the scene causes the particle effect to activate, showing feedback when an action happens.
   Engine calls: Game.OnClick
4. Removing the particle effect after the feedback is shown to keep the scene clean
   Adding: FX.Derez
   Makes this happen: The particle effect disappears once the feedback is displayed, returning the scene to a clean state.
   Engine calls: FX.Derez

Pitfalls:
- Forgetting to clear existing particles before spawning a new effect can cause overlapping or cluttered particle displays that make the effect hard to see.
- Triggering the effect without a corresponding input event means the feedback never appears, so the learner cannot see the effect working.

Games that show it: VectorBlobApocalypse, WallBreaker, demo

---

# 12 Game state
Goal: A small 3D vector game shows a working score, lives, level indicator, and win/lose state with Space to restart.
Needs: none

1. Adding score and lives display
   Adding: Game.OnStart, HUD.Set
   Makes this happen: The game starts and shows a score value and lives count on the screen.
   Engine calls: Game.OnStart, HUD.Set

2. Adding level tracking
   Adding: Game.OnUpdate, HUD.Set
   Makes this happen: Each game update updates the level indicator on screen to reflect the current level.
   Engine calls: Game.OnUpdate, HUD.Set

3. Adding win and lose state detection
   Adding: Game.OnUpdate, HUD.Set
   Makes this happen: When the game reaches a win condition or lose condition, the screen updates to show the win or lose state.
   Engine calls: Game.OnUpdate, HUD.Set

4. Adding Space to restart play again
   Adding: Game.OnClick, HUD.Set
   Makes this happen: Pressing Space restarts the game and clears the current state display to show the initial game state.
   Engine calls: Game.OnClick, HUD.Set

5. Adding State function for notes and tests
   Adding: Game.OnStart, Game.OnUpdate, HUD.Set
   Makes this happen: The State function initializes the game state for notes and tests, updating the screen to show the correct state for the current test or note.
   Engine calls: Game.OnStart, Game.OnUpdate, HUD.Set

Pitfalls:
- Forgetting to clear the previous state display when restarting with Space will leave stale win or lose text on screen after a restart.
- Updating the State function only once at game start will not reflect changes to score, lives, or level during gameplay.

Games that show it: Simple_Test1, Simple_Test2, demo

---

# 13 Levels and layouts
Goal: A repeatable, seeded level table displaying a small grid maze on screen.
Needs: none

1. Setting up the level table
   Adding: Game.OnStart
   Makes this happen: The game starts and a blank level table is initialized on screen with no levels loaded yet.
   Engine calls: Game.OnStart

2. Adding the first level to the table
   Adding: Game.OnStart
   Makes this happen: The first level is added to the level table so the table now contains one level entry.
   Engine calls: Game.OnStart

3. Creating a seeded random level layout
   Adding: LIB_BIT, LIB_MAP
   Makes this happen: A repeatable random seed is used to generate a small grid maze layout that is added to the level table.
   Engine calls: LIB_BIT, LIB_MAP

4. Loading the generated layout into the scene
   Adding: Scene.ClearAll, MeshGrid
   Makes this happen: The generated maze layout is cleared from the scene and a new grid maze shape is added to the scene so the maze appears on screen.
   Engine calls: Scene.ClearAll, MeshGrid

5. Applying the level layout to the current scene
   Adding: Game.OnUpdate
   Makes this happen: The level layout is applied to the current scene so the grid maze remains visible and updates correctly as the game runs.
   Engine calls: Game.OnUpdate

Pitfalls:
- Using a random seed without a fixed value each time will cause the maze layout to change every run, so always pair the seed with a repeatable seed setup to keep the layout consistent.
- Adding a level to the table without generating its layout first will leave the table with an empty entry, so generate the layout before adding it to the table.

Games that show it: DotMaze, PromptAndGlazeMaze, demo

---

# 14 Animation: No Bones
Goal: a small 3D vector game with a spinning, bobbing, growing and shrinking mesh that changes shape each frame on screen.
Needs: none

1. Set up the base scene and camera
   Adding: Game.OnStart, Engine.ResetCamera, Scene.ClearAll
   Makes this happen: the card script starts running and a clean empty 3D scene with a reset camera is shown on screen.
   Engine calls: Game.OnStart, Engine.ResetCamera, Scene.ClearAll

2. Create the animated mesh
   Adding: Mesh.New, Mesh.Define
   Makes this happen: a new 3D mesh is added to the scene so there is a visible shape to animate.
   Engine calls: Mesh.New, Mesh.Define

3. Spin the mesh
   Adding: SetObjectRotation, SetObjectRotationSpeed
   Makes this happen: the mesh starts rotating around its vertical axis so it visibly spins on screen.
   Engine calls: SetObjectRotation, SetObjectRotationSpeed

4. Add bobbing motion to the mesh
   Adding: Scene.SetBob
   Makes this happen: the mesh bobs up and down as it spins, giving it a gentle vertical movement.
   Engine calls: Scene.SetBob

5. Add growth and shrink motion to the mesh
   Adding: SetObjectVelocity
   Makes this happen: the mesh grows and shrinks continuously, changing its size over time.
   Engine calls: SetObjectVelocity

6. Change the mesh shape each frame
   Adding: Game.OnUpdate, Mesh.AddFace
   Makes this happen: the mesh updates its face geometry every frame so the shape changes as the animation runs.
   Engine calls: Game.OnUpdate, Mesh.AddFace

Pitfalls:
- Forgetting to call Game.OnStart before setting up the scene will leave the scene empty and no animation running, so check that the first step starts the card script.
- Adding too many engine calls in a single step will make the change too large and hide the result, so keep each step to the smallest change that produces a visible new effect.

Games that show it: BigBallOfVectors, VectorBlobApocalypse, VectorPong3D

---

# 15 Animation: BVH
Goal: A single mesh that animates frame-by-frame using a loaded BVH motion capture stick clip with walking and idle poses and stable non-skating feet.
Needs: none

1. Load the BVH motion capture stick clip
   Adding: LIB_MOCAP
   Makes this happen: The motion capture library is attached so the stick clip can be loaded into the scene for animation.
   Engine calls: LIB_MOCAP

2. Load the BVH stick clip into the scene
   Adding: LIB_MOCAP
   Makes this happen: The motion capture stick clip is loaded from the text file, making the animation data available for frame-based mesh updates.
   Engine calls: LIB_MOCAP

3. Create the mesh to animate
   Adding: Mesh.New
   Makes this happen: A new mesh is added to the scene so the motion capture data can be applied to it for animation.
   Engine calls: Mesh.New

4. Apply the BVH clip to the mesh for frame-based animation
   Adding: LIB_MOCAP
   Makes this happen: The loaded BVH motion capture clip is bound to the mesh, enabling one mesh to update its pose with each animation frame.
   Engine calls: LIB_MOCAP

5. Configure the mesh to walk and idle with stable feet
   Adding: Scene.SetBob
   Makes this happen: The mesh's animation behavior is set to walk and idle poses, with the feet configured so they do not skate during motion.
   Engine calls: Scene.SetBob

6. Update the mesh each frame to apply the BVH animation
   Adding: Game.OnUpdate
   Makes this happen: The scene runs each update cycle, applying the loaded BVH clip to the mesh so the walking and idle animation plays continuously.
   Engine calls: Game.OnUpdate

Pitfalls:
- Forgetting to load the LIB_MOCAP library before loading the clip will cause the clip to fail to load, leaving the mesh with no animation.
- Applying the clip to the mesh without setting the walk and idle pose behavior will result in the mesh only playing a single default pose instead of walking and idle states.
- Allowing the feet to use default skating motion will cause the feet to slide during the animation, so the feet must be explicitly configured to avoid skating.

Games that show it: demo:

---

# 16 Sound
Goal: A small working 3D vector game that plays a sound when an event occurs on screen.
Needs: none

1. Initialize audio for the game
   Adding: Audio.Init
   Makes this happen: Audio is ready to play sounds for the game.
   Engine calls: Audio.Init
2. Add a clickable object to the scene
   Adding: Entity.Spawn
   Makes this happen: A new object appears in the 3D scene that can be clicked.
   Engine calls: Entity.Spawn
3. Create a sound event handler for clicks
   Adding: Game.OnClick
   Makes this happen: The game now responds to clicks on the scene object.
   Engine calls: Game.OnClick
4. Play a sound when the object is clicked
   Adding: Sound.Play
   Makes this happen: A sound plays each time the scene object is clicked, showing the sound event works.
   Engine calls: Game.OnClick, Sound.Play

Pitfalls:
- Forgetting to initialize Audio before playing sounds will cause the sound to fail to play, so always add the Audio.Init step first.
- Adding Sound.Play without a click handler will not trigger the sound when an event occurs, so ensure a Game.OnClick handler is in place before playing the sound.

Games that show it: Simple_Test1, demo, VectorPong3D

---

# 17 Pause, notes and tests
Goal: A small 3D vector game that pauses with Escape, shows notes with F2, and runs headless tests that drive the game with TestKeys and read State.
Needs: none

1. Set up the game script foundation with pause, notes, and test hooks
   Adding: Game.OnStart, Game.OnUpdate, Game.OnClick, Game.OnKill, Game.OnPause, Game.OnNotes, TestKeys, State
   Makes this happen: The game script loads with handlers for starting, updating, clicking, killing, pausing, showing notes, and test key driving, so the game can pause, display notes, and run headless tests.
   Engine calls: Game.OnStart, Game.OnUpdate, Game.OnClick, Game.OnKill, Game.OnPause, Game.OnNotes, TestKeys, State

2. Implement the Escape pause handler to stop game updates
   Adding: Game.OnPause
   Makes this happen: Pressing Escape triggers the pause handler, which halts the game's normal updates so the scene freezes while the player can still interact with the pause state.
   Engine calls: Game.OnPause

3. Implement the F2 notes handler to display game notes on screen
   Adding: Game.OnNotes
   Makes this happen: Pressing F2 triggers the notes handler, which shows the game notes in the on-screen HUD so the learner can read the instructions and state information.
   Engine calls: Game.OnNotes, HUD.Set

4. Add the headless test driver that feeds TestKeys and reads State
   Adding: TestKeys, State
   Makes this happen: The test driver registers the TestKeys input source and State reader, enabling automated headless tests that drive the game with test keys and read the game's current state.
   Engine calls: TestKeys, State

5. Verify the pause, notes, and test functionality works end to end
   Adding: Game.OnStart, Game.OnUpdate, Game.OnClick, Game.OnKill, Game.OnPause, Game.OnNotes, TestKeys, State
   Makes this happen: Running the game with the test driver confirms that Escape pauses the game, F2 shows the notes, and TestKeys correctly drive the game while State reflects the current state.
   Engine calls: Game.OnStart, Game.OnUpdate, Game.OnClick, Game.OnKill, Game.OnPause, Game.OnNotes, TestKeys, State

Pitfalls:
- Forgetting to register the TestKeys input source will cause headless tests to have no input to drive the game, so tests will not progress even though the game runs normally.
- Adding the pause or notes handler without the corresponding Game.OnPause or Game.OnNotes hook will cause the handlers to be ignored, so Escape and F2 will have no effect.
- Using the wrong State reader or not reading it after driving the game with TestKeys will leave the test results empty, so the learner cannot verify the game's state changes.

Games that show it: Simple_Test1, Simple_Test2, demo

---

# 18 One game, two engines
Goal: a single small 3D vector game that runs identically and works in both the Vibecode3D and xt3d engines
Needs: none

1. Create a minimal working 3D vector game card script
   Adding: Game.OnStart, Scene.ClearAll, Mesh.New, MeshBox, Entity.Spawn, SetObjectPosition
   Makes this happen: a simple 3D vector shape appears on screen with a single positioned object in the scene
   Engine calls: Game.OnStart, Scene.ClearAll, Mesh.New, MeshBox, Entity.Spawn, SetObjectPosition
2. Add a simple update loop to animate the object
   Adding: Game.OnUpdate
   Makes this happen: the object moves along a simple path, showing the game runs continuously in both engines
   Engine calls: Game.OnUpdate
3. Add a click handler to interact with the object
   Adding: Game.OnClick, ScreenToCameraRay, RayCastScene
   Makes this happen: clicking the object triggers a visible interaction effect in both engines
   Engine calls: Game.OnClick, ScreenToCameraRay, RayCastScene
4. Add a collision rule to make the interaction respond to contact
   Adding: Collision.SetGroup, Collision.AddRule
   Makes this happen: the object now reacts to collisions, completing the small working result
   Engine calls: Collision.SetGroup, Collision.AddRule
5. Verify the script runs in both engines with the same simple setup
   Adding: Engine.ResetCamera, Engine.Info
   Makes this happen: the same card script runs successfully in the Vibecode3D and xt3d engines without engine-specific changes
   Engine calls: Engine.ResetCamera, Engine.Info

Pitfalls:
- Adding engine-specific calls or engine-only features in the script: this breaks the requirement that the same script runs in both engines, so remove any engine-specific calls and keep only engine-agnostic setup
- Adding multiple complex features in one step: beginners will not see a clear result after each step, so only add the smallest change needed to complete the current step

Games that show it: Simple_Test1, demo, VectorPong3D

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

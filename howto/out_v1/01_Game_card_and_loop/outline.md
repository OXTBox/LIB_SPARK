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

Wait, let me check the format exactly. The user said "Use EXACTLY this format and nothing else". Let me make sure the structure matches.

Wait, step 1: the format is:
1. <step title>
   Adding: <handler or function names, comma separated>
   Makes this happen: <one sentence: what you see or what changes>
   Engine calls: <names from the list, comma separated>

Let me adjust to make sure each step has exactly those four lines after the number.

Let me redo it properly:

# 01 Game card and loop
Goal: A small 3D vector game runs on a card script with a working start, update, and stop loop that displays an animated 3D shape.
Needs: none

1. Create the game card script with the Game.OnStart, Game.OnUpdate, and Game.OnStop handlers
   Adding: Game.OnStart, Game.OnUpdate, Game.OnStop
   Makes this happen: The card script is set up with the game loop handlers, but nothing is displayed yet.
   Engine calls: Game.OnStart, Game.OnUpdate, Game.OnStop

2. Initialize the 3D scene and camera in Game.OnStart
   Adding: Engine.ResetCamera, Scene.ClearAll
   Makes this happen: The scene is cleared and the camera is reset to a default position, preparing the game for rendering.
   Engine calls: Engine.ResetCamera, Scene.ClearAll

3. Create a simple 3D box shape in Game.OnStart
   Adding: Mesh.New, MeshBox
   Makes this happen: A small box mesh is added to the scene and appears on screen as the first visible element of the game.
   Engine calls: Mesh.New, MeshBox

4. Run the game loop in Game.OnUpdate to animate the shape
   Adding: Game.OnUpdate
   Makes this happen: The shape updates about 30 times per second, showing the working loop that drives the

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

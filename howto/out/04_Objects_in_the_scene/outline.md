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

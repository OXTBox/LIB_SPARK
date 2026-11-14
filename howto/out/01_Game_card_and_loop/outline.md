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

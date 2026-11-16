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

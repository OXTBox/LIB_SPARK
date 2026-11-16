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

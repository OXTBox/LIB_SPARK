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

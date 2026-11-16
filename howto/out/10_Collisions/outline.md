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

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

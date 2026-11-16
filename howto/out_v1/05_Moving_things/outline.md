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

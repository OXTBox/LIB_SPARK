# 08 Camera
Goal: a small working 3D scene with a fixed view, a top-down view, and a third-person camera following a hero on screen
Needs: none

1. Setting up the fixed view
   Adding: Game.OnStart
   Makes this happen: the game starts and the camera is positioned to show a fixed view of the scene
   Engine calls: Engine.ResetCamera, Engine.SetCam

2. Changing the camera yaw to rotate the fixed view
   Adding: Game.OnUpdate
   Makes this happen: the fixed view rotates as the camera yaw changes, showing a new orientation of the same scene
   Engine calls: gCameraYaw

3. Adjusting the camera pitch to tilt the fixed view
   Adding: Game.OnUpdate
   Makes this happen: the fixed view tilts upward or downward as the camera pitch changes, showing a new angle of the scene
   Engine calls: gCameraPitch

4. Switching to a top-down view
   Adding: Game.OnClick
   Makes this happen: the camera rotates to a top-down orientation, showing the scene from directly above
   Engine calls: gCameraYaw, gCameraPitch

5. Creating a hero and setting up third-person follow
   Adding: Entity.Spawn, SetObjectPosition, SetObjectRotation, SetObjectRotationSpeed, SetObjectVelocity
   Makes this happen: a hero entity is spawned in the scene and the camera begins following the hero from behind
   Engine calls: Entity.Spawn, SetObjectPosition, SetObjectRotation, SetObjectRotationSpeed, SetObjectVelocity

6. Adjusting the third-person camera position to follow the hero
   Adding: Game.OnUpdate
   Makes this happen: the camera continuously moves to stay behind and above the hero as the hero moves, showing a third-person view of the scene
   Engine calls: gCameraYaw, gCameraPitch, GetObjectPosition, SetObjectPosition

Pitfalls:
- Forgetting to reset the camera before changing its orientation will leave the camera in an invalid state, so always call Engine.ResetCamera first when starting a new view.
- Changing the camera yaw or pitch without updating the view globals will cause the camera to jump or show a blank view, so always pair camera global changes with the view globals when switching views.

Games that show it: DeepDive, Hunter, VectorBlobApocalypse:

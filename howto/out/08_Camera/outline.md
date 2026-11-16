# 08 Camera
Goal: a fixed view shows a centered wire cube, then the camera rotates to a top-down orientation.
Needs: 01, 04

1. Set the fixed camera view
   Adding: Engine.SetCam, gCameraYaw, gCameraPitch
   Makes this happen: the viewport locks to a centered, straight-down view of the scene without any camera movement.
   Engine calls: Engine.SetCam, gCameraYaw, gCameraPitch
2. Add a wire cube to the fixed view
   Adding: Mesh.Define "Cube", MeshBox(40,40,40), Entity.Spawn("Cube",0,0,0,"cyan")
   Makes this happen: a cyan wire cube sits centered in the fixed view, visible and stable.
   Engine calls: Mesh.Define, MeshBox, Entity.Spawn
3. Rotate the camera to a top-down view
   Adding: gCameraPitch, gCameraYaw
   Makes this happen: the camera tilts so the view is oriented straight down, showing the cube from above.
   Engine calls: gCameraYaw, gCameraPitch
4. Move the camera yaw to follow a new position
   Adding: gCameraYaw, SetObjectPosition
   Makes this happen: the camera rotates around the scene center, keeping the view oriented top-down while the cube stays in view.
   Engine calls: gCameraYaw, SetObjectPosition

Pitfalls:
- gCameraYaw and gCameraPitch only change the view when Engine.SetCam is used to apply them; setting them alone leaves the camera in its previous orientation.
- Do not change the camera view without a new shape on screen, or the learner will see no visible change from the camera call.

Games that show it: Simple_Test1

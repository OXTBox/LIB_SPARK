01 | Game card and loop | The runner descends the shaft through repeated Game.OnUpdate frames while Game.OnStart sets up the shaft and platforms and Game.OnStop cleans up the scene |
05 | Moving things | The runner’s downward descent and platform movement follow the +Y is DOWN rule with SetObjectPosition and SetObjectRotationSpeed applied each frame |
08 | Camera | The camera follows the runner down the shaft using Engine.SetCam and gCameraYaw/gCameraPitch for a third-person view behind the runner |
10 | Collisions | The runner avoids patrol drones and drops through gaps by using Collision.SetGroup, Collision.AddRule, and Collision.Hit checks in Game.OnUpdate |

01 | Game card and loop | The ship spawns, drifts, and fires while Game.OnStart sets up the scene, Game.OnUpdate runs the 30-updates-per-second loop, and Game.OnStop cleans up the state |
04 | Objects in the scene | Spawning a named rock mesh with a colour, killing it to remove it, and clearing the scene to reset the field show the object lifecycle |
08 | Camera | The fixed top-down view and the third-person camera behind the ship using Engine.SetCam and gCameraYaw/gCameraPitch show how the camera is controlled |
10 | Collisions | The ship firing and splitting rocks into smaller ones via Collision.SetGroup, Collision.AddRule, and Collision.Hit shows how collision rules drive the core gameplay |

01 | Game card and loop | The lander’s descent is driven entirely by the Game.OnStart setup, Game.OnUpdate updates, and Game.OnStop cleanup loop that runs gravity and burns every frame |
05 | Moving things | The lander’s side thrusters and main engine use SetObjectPosition, SetObjectRotationSpeed, and SetObjectVelocity to move and rotate while +Y is DOWN, showing the movement mechanics |
08 | Camera | The third-person view behind the lander uses Engine.SetCam and the gCameraYaw/gCameraPitch globals to frame the descent from behind the hero |
10 | Collisions | The lander’s landing on the pad is detected with Collision.SetGroup, Collision.AddRule, and Collision.Hit checks in Game.OnUpdate to trigger the landing state |

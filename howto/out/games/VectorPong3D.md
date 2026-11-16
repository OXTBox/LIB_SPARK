01 | Game card and loop | The game runs as a single card script where Game.OnStart sets up the court, Game.OnUpdate processes about 30 updates per second, and Game.OnStop cleans up, showing how a basic 3D vector game is structured.
04 | Objects in the scene | Spawning a named floating block with Entity.Spawn and removing it with Entity.Kill demonstrates how objects are placed and managed in the scene.
08 | Camera | The camera uses Engine.SetCam with gCameraYaw and gCameraPitch to provide a fixed view, showing how the 3D court is displayed from behind the player's bat.
10 | Collisions | The Game.OnUpdate distance checks with Collision.SetGroup and Collision.AddRule show how the ball bounces off the walls, ceiling, and floating blocks.

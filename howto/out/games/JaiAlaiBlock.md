01 | Game card and loop | The runner’s frame loop runs Game.OnStart to set up the grid, Game.OnUpdate to update the runner and blocks, and Game.OnStop to clean up, so the game runs continuously at about 30 updates per second.
02 | Shapes | The ceiling of blocks is built with MeshBox to create the grid of blocks that the runner hurls the ball at.
04 | Objects in the scene | The runner and the thrown ball are spawned as named objects with colours, and the falling blocks are killed when they hit the ground to remove them from the scene.
08 | Camera | The camera uses Engine.SetCam with fixed gCameraYaw and gCameraPitch to keep a stable top-down view of the grid and blocks.

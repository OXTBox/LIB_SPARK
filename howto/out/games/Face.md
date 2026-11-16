01 | Game card and loop | The Face game runs its setup in Game.OnStart, its 30-updates-per-second rendering loop in Game.OnUpdate, and its cleanup in Game.OnStop so the raised vector blocks stay on the dim grid panel.
04 | Objects in the scene | Spawning the LIB_MCP connected face mesh into the scene with Entity.Spawn places the smiling vector blocks on the panel, while Entity.Kill and Scene.ClearAll let the player remove or reset them.
08 | Camera | Engine.SetCam with the fixed view globals locks the camera on the grid panel so the raised vector blocks stay visible in a stable third-person view.
011 | Effects | FX.Sparks and FX.Destroy produce the visual feedback when the face mesh is interacted with, showing the effect feedback step working in the game.

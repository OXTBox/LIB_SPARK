01 | Game card and loop | The walker hops across lanes of traffic while Game.OnStart sets up the scene, Game.OnUpdate runs the hop and lane updates about 30 times a second, and Game.OnStop cleans up the scene |
08 | Camera | The walker is viewed from a fixed third-person camera behind the hero using Engine.SetCam with gCameraYaw and gCameraPitch to follow the hopping walker |
09 | HUD and text | The score lines showing the three required top-strip reaches and the help text for the arrow keys and Space controls are shown via HUD.Set and kept below the top bars |
10 | Collisions | The walker’s hop triggers Collision.AddRule and Collision.Hit checks to detect when the walker reaches the top strip lanes to score |

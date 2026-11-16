01 | Game card and loop | The SkyRaiders card script runs Game.OnStart to set up the game, Game.OnUpdate to drive the 30-update-second loop, and Game.OnStop to clean up after play |
07 | Mouse and picking | The Space fire input combined with Game.OnClick, ScreenToCameraRay, RayCastScene, and Weapon.FireAt lets the player click to aim and fire the cannon |
09 | HUD and text | The HUD.Set calls display the score lines and help text for the SkyRaiders sky raiders gameplay |
10 | Collisions | The Collision.SetGroup, Collision.AddRule, and Collision.Hit calls plus simple distance checks in Game.OnUpdate let the cannon and raiders interact with the ground and each other |

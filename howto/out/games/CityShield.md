01 | Game card and loop | The CityShield card runs Game.OnStart to set up the game, Game.OnUpdate to process the falling streaks about 30 times a second, and Game.OnStop to clean up, showing the full card script lifecycle.
02 | Shapes | The built-in MeshBox and MeshPrism calls create the six city blocks and streaks shown on screen, demonstrating how to build basic shapes with the engine's built-in mesh tools.
03 | Shapes | The hand-wired Mesh.New, Mesh.AddVertex, Mesh.AddLine, and Mesh.AddFace calls construct the custom streaks point by point, showing how to build custom shapes without relying on built-in meshes.
04 | Objects in the scene | Entity.Spawn places the named streaks in the world with their colours, Entity.Kill removes them when stopped, and Scene.ClearAll resets the scene between levels, showing how to manage scene objects.
05 | Moving things | SetObjectPosition, SetObjectRotation, SetObjectRotationSpeed, and SetObjectVelocity animate the city blocks and streaks moving with +Y as down, demonstrating how to make objects move in the scene.
06 | Keyboard input | The arrow keys move the aiming cross and Space fires bursts, showing how to use held keys for movement and one press for actions like firing.
07 | Mouse and picking | Game.OnClick, ScreenToCameraRay,

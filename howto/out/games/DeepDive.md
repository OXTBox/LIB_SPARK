01 | Game card and loop | The diver's upward swim is driven by the Game.OnStart setup, Game.OnUpdate loop, and Game.OnStop cleanup, showing a card script runs continuously at about 30 updates per second |
02 | Shapes | The pearls brought up from the sea bed are built with MeshBox and Mesh.Define, showing built-in meshes create the scene's shapes |
03 | Shapes | The hand-wired pearl shapes are created point by point with Mesh.New, Mesh.AddVertex, Mesh.AddLine, and Mesh.AddFace, showing how to build custom wire shapes |
04 | Objects in the scene | The pearls spawned from the sea bed are removed when they reach the surface via Entity.Kill and Entity.Count, showing how to add, track, and remove scene objects |
05 | Moving things | The diver's upward swim and rotation use SetObjectPosition, SetObjectRotation, and SetObjectRotationSpeed, showing how to move and rotate objects with the correct +Y down direction |
06 | Keyboard input | The swim control using arrow keys and Space for play again is driven by the keysDown input, showing how to read held and single key presses to drive game actions |
07 | Mouse and picking | Clicking to aim the diver's upward path uses Game.OnClick, ScreenToCameraRay, RayCastScene, and Weapon.FireAt, showing how to use mouse

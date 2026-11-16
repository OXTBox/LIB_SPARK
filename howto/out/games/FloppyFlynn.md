01 | Game card and loop | The blue two-legged ship’s flight cycle is driven by the Game.OnStart, Game.OnUpdate, and Game.OnStop card hooks that run the 30-update-second loop for the destructible terrain flight.
02 | Shapes | The ship’s two-legged body and terrain blocks are built with the built-in MeshBox and MeshPrism calls that create the vector ship’s core geometry.
03 | Shapes | The ship’s custom ankle flap is drawn point by point using Mesh.New, Mesh.AddVertex, Mesh.AddLine, and Mesh.AddFace to wire the unique two-legged design.
04 | Objects in the scene | The destructible terrain and ship parts are placed in the world with Entity.Spawn, removed when damaged with Entity.Kill, and cleared with Scene.ClearAll to reset levels.
05 | Moving things | The ship’s forward and vertical movement is demonstrated by SetObjectPosition, SetObjectRotation, SetObjectRotationSpeed, and SetObjectVelocity calls that move the ship through the scrolling terrain with +Y as down.
06 | Keyboard input | Player flight control is shown by the WASD and arrow key input handling in the keysDown hook, demonstrating one press versus held movement for the ship.
07 | Mouse and picking | The ship’s collision interaction with terrain is demonstrated by Game.OnClick, ScreenToCameraRay,

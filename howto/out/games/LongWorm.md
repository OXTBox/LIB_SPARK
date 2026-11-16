01 | Game card and loop | The LongWorm card runs Game.OnStart to set up the worm, Game.OnUpdate to advance the worm on the grid about 30 times a second, and Game.OnStop to clean up, so the player sees the worm move continuously.
02 | Shapes | The built-in MeshBox mesh used to spawn the worm's body shape on the grid, showing how a simple named shape is placed in the scene.
03 | Shapes | The hand-wired Mesh.New, Mesh.AddVertex, Mesh.AddLine, Mesh.AddFace steps build the worm's custom body mesh point by point, showing how to create a shape without relying on built-in meshes.
04 | Objects in the scene | Entity.Spawn places the worm's named body shape in the world with a colour, Entity.Kill removes it when it ends, and Scene.ClearAll resets the scene, showing how to manage scene objects.
05 | Moving things | The worm's body moves along the grid using SetObjectPosition with +Y as down, showing how objects move in the scene with the correct coordinate direction.
06 | Keyboard input | Arrow keys turn the worm and Space restarts the game after the end, showing how held keys and one-press keys control the game's actions.
07 | Mouse and picking | The Game.OnClick and RayCastScene steps let the player click to interact with the worm and

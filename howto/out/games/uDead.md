01 | Game card and loop | The uDead game runs its setup, ~30 updates per second, and cleanup through Game.OnStart, Game.OnUpdate, and Game.OnStop so the player sees the game cycle in action.
02 | Shapes | The built-in MeshBox and MeshSphere meshes appear on screen immediately when spawned, showing how basic shapes are created with engine calls.
03 | Shapes | The hand-built wire shapes using Mesh.New, Mesh.AddVertex, Mesh.AddLine, and Mesh.AddFace are drawn point by point to demonstrate custom mesh construction.
04 | Objects in the scene | Entity.Spawn places named colored shapes into the world and Entity.Kill removes them, showing how objects are added and removed from the scene.
05 | Moving things | SetObjectPosition, SetObjectRotation, SetObjectRotationSpeed, and SetObjectVelocity move the spawned dead entities, demonstrating how objects can be animated with engine calls.

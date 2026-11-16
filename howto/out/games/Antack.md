01 | Game card and loop | The Antack game runs its setup, ~30 updates per second, and cleanup as a single card script driven by Game.OnStart, Game.OnUpdate, and Game.OnStop |
02 | Shapes | The built-in MeshBox and MeshPyramid meshes used for the ant-hill bases and enemy hills appear immediately after their creation steps |
03 | Shapes | The hand-built ant and enemy hill meshes are created point by point with Mesh.New, Mesh.AddVertex, Mesh.AddLine, and Mesh.AddFace before they are placed in the scene |
04 | Objects in the scene | Spawning the ant armies at the enemy hills and killing the red enemy armies the computer sends at shows Entity.Spawn, Entity.Kill, and Scene.ClearAll in action |
05 | Moving things | The ant armies and enemy armies move through the hills using SetObjectPosition, SetObjectRotation, SetObjectRotationSpeed, and SetObjectVelocity with +Y as down |

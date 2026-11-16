01 | Game card and loop | The card script runs Game.OnStart to set up the sea, Game.OnUpdate to update the boat, buoy, rocks, and laser about 30 times a second, and Game.OnStop to clean up |
02 | Shapes | The built-in MeshBox and MeshSphere meshes create the grid sea and buoy, with Mesh.Define naming them for the scene |
04 | Objects in the scene | Entity.Spawn places the named rock and laser shapes into the world with colours, Entity.Kill removes drifting rocks that hit the boat, and Scene.ClearAll resets the scene between levels |

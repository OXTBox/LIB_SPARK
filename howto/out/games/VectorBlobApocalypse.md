01 | Game card and loop | The game runs a continuous Game.OnUpdate loop about 30 times a second that spawns jittery vector blobs, spins them, and lets the player shoot them without stopping |
02 | Shapes | Built-in MeshBox and MeshSphere meshes are used to create the swarm of vector jelly blobs that appear from every side |
03 | Shapes | Hand-built Mesh.New, Mesh.AddVertex, and Mesh.AddFace wire the custom vector blob shapes point by point so they look like jittery jelly forms |
04 | Objects in the scene | Entity.Spawn places the named vector blob shapes into the world with colours, while Entity.Kill removes them when they are destroyed |

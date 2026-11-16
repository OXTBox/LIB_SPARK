01 | Game card and loop | The wireframe cube continuously spins over the floor grid in Game.OnUpdate, with Game.OnStart setting up the scene and Game.OnStop cleaning up after the game ends |
02 | Shapes | The built-in wireframe cube rendered by MeshBox is the visible proof that a named mesh shape works in the scene |
03 | Shapes | The hand-built wireframe cube created point by point with Mesh.New, Mesh.AddVertex, Mesh.AddLine, and Mesh.AddFace replaces the built-in cube as a visible example of hand-crafted wire shapes |
04 | Objects in the scene | The named wireframe cube entity is visible in the scene with its colour, and removing it via Entity.Kill shows the object lifecycle works |
05 | Moving things | The cube continuously spins over the floor grid via SetObjectRotation and SetObjectRotationSpeed, demonstrating that rotation and movement work in the game |

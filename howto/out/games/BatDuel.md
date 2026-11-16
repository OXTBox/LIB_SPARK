01 | Game card and loop | The bat, ball, and serve mechanics run continuously through Game.OnUpdate at about 30 updates per second, with Game.OnStart setting up the scene and Game.OnStop cleaning up after play |
02 | Shapes | The two bat meshes and the ball are built with built-in MeshBox and MeshSphere calls that appear immediately on screen |
04 | Objects in the scene | Spawning the ball into the world with Entity.Spawn places a named coloured shape in the scene, while Entity.Kill removes it and Scene.ClearAll resets the layout |
05 | Moving things | The bat and ball move through the scene using SetObjectPosition and SetObjectVelocity, with +Y being down so the ball bounces off the top and bottom edges |

01 | Game card and loop | The GeneticAnomaly card runs Game.OnStart to set up the procedural world, Game.OnUpdate to update about 30 times a second, and Game.OnStop to clean up after play ends. |
02 | Shapes | Built-in meshes like MeshBox and MeshPrism are used to create the stick figures and basic world structures for the game. |
08 | Camera | Engine.SetCam with gCameraYaw and gCameraPitch lets the player control the fixed top-down view and third-person camera behind the hero. |
15 | Animation | BVH stick clips from LIB_MOCAP are loaded to animate the stick figures walking and idling with feet that do not skate. |

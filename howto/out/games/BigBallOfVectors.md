01 | Game card and loop | | The Security Polyhedron spawns, gains sides and size with every catch, and the game runs its ~30 updates per second via Game.OnStart, Game.OnUpdate, and Game.OnStop.
02 | Shapes | | The crude Security Polyhedron is shown as a built-in MeshBox mesh that gains sides and size as it catches agents.
03 | Shapes | | The entanglement hazards are shown as hand-wired Mesh.New, Mesh.AddVertex, Mesh.AddLine, and Mesh.AddFace shapes that form the tangled ball.
04 | Objects in the scene | | The loose rogue AI agents are shown as Entity.Spawned named shapes that can be Entity.Killed or cleared with Scene.ClearAll.
05 | Moving things | | The Security Polyhedron moves and rotates through SetObjectPosition, SetObjectRotation, SetObjectRotationSpeed, and SetObjectVelocity as it catches agents, with +Y being down.
06 | Keyboard input | | Players command the Security Polyhedron with WASD and arrow keys via the keysDown hook, showing one press versus held movement.
07 | Mouse and picking | | Players aim and command the Security Polyhedron with mouse clicks via Game.OnClick, ScreenToCameraRay, RayCastScene, and Weapon.FireAt.
08 | Camera | | The Security Polyhedron is viewed

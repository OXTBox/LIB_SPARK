01 | Game card and loop | The runner’s spear-throw and cone-shield updates are driven entirely by Game.OnStart setup, Game.OnUpdate 30 times per second, and Game.OnStop cleanup, showing the card script loop runs the full game flow.
02 | Shapes | The boss Cone is built with MeshPrism and Mesh.Define, showing built-in meshes and named shape definitions appear on screen immediately.
04 | Objects in the scene | The shield cubes and key tokens are spawned via Entity.Spawn with colours, removed via Entity.Kill, and cleared with Scene.ClearAll, demonstrating object lifecycle management.
07 | Mouse and picking | The player throws the logic-probe spear using Game.OnClick, ScreenToCameraRay, RayCastScene, and Weapon.FireAt, showing mouse-driven scene interaction.

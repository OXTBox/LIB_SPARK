# 02 Shapes: built-in meshes
Goal: a named built-in wire mesh appears on screen as a visible shape in the middle of the view.
Needs: 01

1. A named shape on screen
   Adding: Mesh.Define "Cube", MeshBox(40,40,40), Entity.Spawn("Cube",0,0,0,"cyan") in Game.OnStart
   Makes this happen: a cyan wire cube sits in the middle of the view, visible as a shape.
   Engine calls: Mesh.Define, MeshBox, Entity.Spawn
2. A second named shape on screen
   Adding: Mesh.Define "Sphere", MeshSphere(30,30), Entity.Spawn("Sphere",0,40,0,"orange") in Game.OnStart
   Makes this happen: an orange wire sphere appears above the cube, both visible as shapes.
   Engine calls: Mesh.Define, MeshSphere, Entity.Spawn
3. A third named shape on screen
   Adding: Mesh.Define "Pyramid", MeshPyramid(25,25), Entity.Spawn("Pyramid",0,-40,0,"green") in Game.OnStart
   Makes this happen: a green wire pyramid appears below the cube, all three shapes visible together.
   Engine calls: Mesh.Define, MeshPyramid, Entity.Spawn
4. A grid shape on screen
   Adding: Mesh.Define "Grid", MeshGrid(60,20), Entity.Spawn("Grid",0,0,0,"white") in Game.OnStart
   Makes this happen: a white wire grid appears in the middle of the view, adding a fourth visible shape.
   Engine calls: Mesh.Define, MeshGrid, Entity.Spawn

Pitfalls:
- Mesh.Define only names a shape; nothing shows until Entity.Spawn puts it in the scene, so a defined mesh with no spawn stays invisible.
- Size changes need a new shape: Mesh.Define the new size, Entity.Kill the old shape, and Entity.Spawn the new one, rather than reusing the same named shape.

Games that show it: Simple_Test1

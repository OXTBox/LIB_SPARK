# 02 Shapes: built-in meshes
Goal: A named 3D shape is displayed on screen as a visible working mesh.
Needs: none

1. Creating the first mesh shape
   Adding: Mesh.New, Mesh.Define
   Makes this happen: A new named mesh is added to the scene and appears as a visible 3D shape on screen.
   Engine calls: Mesh.New, Mesh.Define

2. Adding a box shape to the scene
   Adding: MeshBox
   Makes this happen: A box mesh is created and added to the scene, displaying a new rectangular 3D shape on screen.
   Engine calls: MeshBox

3. Adding a prism shape to the scene
   Adding: MeshPrism
   Makes this happen: A prism mesh is created and added to the scene, displaying a new triangular prism 3D shape on screen.
   Engine calls: MeshPrism

4. Adding a pyramid shape to the scene
   Adding: MeshPyramid
   Makes this happen: A pyramid mesh is created and added to the scene, displaying a new triangular pyramid 3D shape on screen.
   Engine calls: MeshPyramid

5. Adding a sphere shape to the scene
   Adding: MeshSphere
   Makes this happen: A sphere mesh is created and added to the scene, displaying a new round 3D shape on screen.
   Engine calls: MeshSphere

6. Adding a grid shape to the scene
   Adding: MeshGrid
   Makes this happen: A grid mesh is created and added to the scene, displaying a new grid 3D shape on screen.
   Engine calls: MeshGrid

Pitfalls:
- Forgetting to call Mesh.Define before adding a shape may cause the mesh to appear blank or not render, so always name the shape first before adding it to the scene.
- Adding multiple shapes without clearing the scene first can cause overlapping shapes to hide earlier shapes, so ensure the scene is cleared before adding each new shape.

Games that show it: Simple_Test1, demo, VectorBlobApocalypse

Wait, let me check the format strictly. The user said "Use EXACTLY this format and nothing else". Let me make sure the structure matches exactly.

Let me adjust to be precise. The format is:

# 02 Shapes: built-in meshes
Goal: <one sentence: what the learner has on screen at the end>
Needs: <topic numbers it builds on, or "none">

1. <step title>
   Adding: <handler or function names, comma separated>
   Makes this happen: <one sentence: what you see or what changes>
   Engine calls: <names from the list, comma separated>
2. ...

Pitfalls:
- <one common mistake and how to spot it>
- <another>

Games that show it: <up to 3 names from this list, or "none">: Amazing_Couple, ...

Let me make sure each step is the smallest change that puts something new on screen. So step 1 should be creating the first mesh with Mesh.New and Mesh.Define? Wait, but Mesh.Define gives a shape a name. So step 1: create a mesh and define it, so a named mesh appears. Then step 2: add MeshBox, step 3 MeshPrism, step 4 MeshPyramid, step 5 MeshSphere, step 6 MeshGrid. That's 6 steps, which is within 4-7.

Wait, but does Mesh.New create a mesh? The shapes list includes Mesh.New, Mesh.AddVertex, etc. So yes, Mesh.New creates a mesh, Mesh.Define gives it a name. So step 1: Mesh.New, Mesh.Define. That puts a named mesh on screen. Then each subsequent step adds one built-in shape. That's 6 steps total, which is good.

Let me check the engine calls are from the list: Mesh.New, Mesh.Define are in shapes list. MeshBox, MeshPrism, MeshPyramid, MeshSphere, MeshGrid are in shapes list. Good

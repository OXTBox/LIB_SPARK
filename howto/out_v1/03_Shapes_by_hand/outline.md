# 03 Shapes: by hand
Goal: a small wire 3D shape made point by point from the Vibecode3D engine
Needs: none

1. Creating the base mesh
   Adding: Mesh.New
   Makes this happen: a new empty 3D mesh is created and ready to hold vertices, lines, and faces.
   Engine calls: Mesh.New

2. Adding the first vertex to the mesh
   Adding: Mesh.AddVertex
   Makes this happen: the first point of the shape is added to the mesh, giving it a starting position on screen.
   Engine calls: Mesh.AddVertex

3. Adding the first line to the mesh
   Adding: Mesh.AddLine
   Makes this happen: a line is drawn between the first vertex and a second point, showing the first edge of the shape.
   Engine calls: Mesh.AddLine

4. Adding the first face to the mesh
   Adding: Mesh.AddFace
   Makes this happen: a triangle face is added using the existing vertices, completing the first small working shape on screen.
   Engine calls: Mesh.AddFace

5. Adding more vertices to extend the shape
   Adding: Mesh.AddVertex
   Makes this happen: additional vertices are added around the shape, growing it into a larger wire figure.
   Engine calls: Mesh.AddVertex

6. Adding more lines and faces to finish the shape
   Adding: Mesh.AddLine, Mesh.AddFace
   Makes this happen: more edges and faces are added to connect the extended vertices, producing a complete small wire 3D shape.
   Engine calls: Mesh.AddLine, Mesh.AddFace

Pitfalls:
- Adding vertices out of order: vertices must be added in sequence so the lines and faces have valid connections, or the shape will appear broken or missing parts.
- Forgetting to connect vertices with lines: adding only vertices and faces without lines will leave the shape as disconnected points and faces with no visible edges.
- Adding faces with incorrect vertex references: faces must reference existing vertices that were added earlier, or the mesh will fail to render the face correctly.

Games that show it: Face, Simple_Test1, Simple_Test2:

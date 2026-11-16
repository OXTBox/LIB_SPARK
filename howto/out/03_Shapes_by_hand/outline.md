# 03 Shapes: by hand
Goal: a small wire cube made point-by-point with hand-drawn vertices, lines, and faces appears on screen.
Needs: 01, 04

1. A game card with an empty scene
   Adding: Game.OnStart (with Engine.ResetCamera, Scene.ClearAll, HUD.Clear)
   Makes this happen: press Play and the viewport is empty and nothing goes wrong; the game runs.
   Engine calls: Game.OnStart, Engine.ResetCamera, Scene.ClearAll, HUD.Clear
2. A wire cube shape defined by hand
   Adding: Mesh.Define "Cube", Mesh.AddVertex(0,0,0), Mesh.AddVertex(40,0,0), Mesh.AddVertex(40,40,0), Mesh.AddVertex(0,40,0), Mesh.AddVertex(0,0,40), Mesh.AddVertex(40,0,40), Mesh.AddVertex(40,40,40), Mesh.AddLine(0,1), Mesh.AddLine(1,2), Mesh.AddLine(2,3), Mesh.AddLine(3,4), Mesh.AddLine(4,5), Mesh.AddLine(5,6), Mesh.AddLine(6,7), Mesh.AddLine(7,0), Mesh.AddFace(0,1,2,3), Mesh.AddFace(1,2,7,6), Mesh.AddFace(2,3,7,6), Mesh.AddFace(3,4,0,7)
   Makes this happen: the cube is named "Cube" in the scene and sits in the middle of the view.
   Engine calls: Mesh.Define, Mesh.AddVertex, Mesh.AddLine, Mesh.AddFace
3. The cube placed in the scene
   Adding: Entity.Spawn("Cube",0,0,0,"cyan") in Game.OnStart
   Makes this happen: the hand-built wire cube appears on screen as a cyan wire shape.
   Engine calls: Entity.Spawn
4. The cube rotates with the loop
   Adding: on Game.OnUpdate (add 0.05 to an angle variable, SetObjectRotation with it)
   Makes this happen: the cube turns about 30 small rotations per second as the game runs.
   Engine calls: Game.OnUpdate, SetObjectRotation

Pitfalls:
- Mesh.Define only names a shape; nothing shows until Entity.Spawn puts it in the scene.
- Keep the rotation angle in a script-local variable; a plain local in Game.OnUpdate starts at 0 every step.

Games that show it: Simple_Test1

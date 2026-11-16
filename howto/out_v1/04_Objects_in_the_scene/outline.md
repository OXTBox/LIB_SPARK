# 04 Objects in the scene
Goal: A small named 3D shape appears in the scene with a colour, and can be removed or cleared from the scene.
Needs: none

1. Adding a coloured shape to the scene
   Adding: Entity.Spawn
   Makes this happen: A new named shape is placed in the world and appears on screen in its assigned colour.
   Engine calls: Entity.Spawn
2. Removing the added shape from the scene
   Adding: Entity.Kill
   Makes this happen: The previously added named shape is removed and disappears from the scene.
   Engine calls: Entity.Kill
3. Clearing all objects from the scene
   Adding: Scene.ClearAll
   Makes this happen: Every object currently in the scene is removed, leaving nothing on screen except the base scene.
   Engine calls: Scene.ClearAll

Pitfalls:
- Forgetting to assign a colour when spawning the shape will leave it with the default scene colour, so check the visible colour matches your intended colour before moving on.
- Spawning the shape without naming it will prevent you from targeting it later with Entity.Kill, so always include the name in the spawn call.
- Calling Scene.ClearAll before spawning the shape will remove the shape immediately, so perform the clear step only after the shape has been added.

Games that show it: Simple_Test1, demo, VectorBlobApocalypse

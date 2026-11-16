# 10 Collisions
Goal: A small 3D scene where two collidable shapes interact with each other and respond to collision detection.
Needs: none

1. Setting up collision groups and rules
   Adding: Collision.SetGroup, Collision.AddRule
   Makes this happen: Two distinct shapes are assigned collision groups and a collision rule is added so the engine can detect when they overlap.
   Engine calls: Collision.SetGroup, Collision.AddRule
2. Creating the collidable shapes
   Adding: Mesh.New, MeshBox
   Makes this happen: Two simple 3D boxes are created and placed in the scene so they can be tested against the collision rules.
   Engine calls: Mesh.New, MeshBox
3. Adding collision detection to the game update loop
   Adding: Game.OnUpdate, Collision.Hit
   Makes this happen: The game update loop is hooked to run collision checks each frame so overlapping shapes trigger the collision response.
   Engine calls: Game.OnUpdate, Collision.Hit
4. Handling collision overlap in the update loop
   Adding: Game.OnUpdate
   Makes this happen: When the shapes overlap, the update loop resolves the collision by moving the shapes apart so they no longer intersect.
   Engine calls: Game.OnUpdate

Pitfalls:
- Forgetting to add a collision rule between the two shapes will leave the engine unable to detect overlaps, so the shapes will never trigger the collision response.
- Adding the collision check to the wrong handler (such as Game.OnStart or Game.OnStop) will cause the collision to only run once at startup or when the game stops, instead of every frame during gameplay.

Games that show it: ProbeVsCone, WallBreaker, demo:

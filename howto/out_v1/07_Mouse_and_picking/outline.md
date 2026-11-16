# 07 Mouse and picking
Goal: A small 3D scene where clicking with the mouse selects and fires a projectile at the clicked object.
Needs: none

1. Set up the 3D scene and camera
   Adding: Game.OnStart
   Makes this happen: The Vibecode3D engine starts the game and prepares the 3D scene for mouse interactions.
   Engine calls: Game.OnStart

2. Add the mouse picking handlers
   Adding: Game.OnClick, ScreenToCameraRay, RayCastScene
   Makes this happen: The game now responds to mouse clicks by converting the click position into a 3D ray and casting it against the scene.
   Engine calls: Game.OnClick, ScreenToCameraRay, RayCastScene

3. Add the weapon firing handler
   Adding: Weapon.FireAt
   Makes this happen: Clicking on an object in the scene now fires the projectile at the clicked 3D position.
   Engine calls: Weapon.FireAt

Pitfalls:
- Forgetting to set up the camera before casting rays will cause the ray to miss all objects, so the scene appears empty even though the click handlers are added.
- Casting the ray without clearing the scene first can leave stale collision or object data, making the click fire at the wrong target.

Games that show it: Simple_Test1, VectorPong3D, demo

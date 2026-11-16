# 07 Mouse and picking
Goal: a single cube responds to the mouse click by firing a projectile that travels toward the cursor.
Needs: 01, 04

1. A clickable cube on screen
   Adding: Game.OnClick, Mesh.Define "Cube", MeshBox(40,40,40), Entity.Spawn("Cube",0,0,0,"cyan")
   Makes this happen: a cyan wire cube sits in the middle of the view and can be clicked with the mouse.
   Engine calls: Game.OnClick, Mesh.Define, MeshBox, Entity.Spawn
2. A projectile spawned at the click point
   Adding: ScreenToCameraRay, RayCastScene, Entity.Spawn("Projectile",0,0,0,"orange")
   Makes this happen: clicking the cube spawns an orange projectile at the camera ray position where the cube was hit.
   Engine calls: ScreenToCameraRay, RayCastScene, Entity.Spawn
3. The projectile moves toward the mouse cursor each update
   Adding: Game.OnUpdate, SetObjectVelocity, SetObjectPosition
   Makes this happen: the projectile travels toward the mouse cursor, about 30 small steps per second.
   Engine calls: Game.OnUpdate, SetObjectVelocity, SetObjectPosition
4. The projectile fires from the weapon when it reaches the target
   Adding: Weapon.FireAt
   Makes this happen: clicking the cube again fires the projectile from the weapon, and the projectile continues moving toward the cursor.
   Engine calls: Weapon.FireAt

Pitfalls:
- Game.OnClick is the mouse only; do not use it to read keyboard input, or the click will not trigger.
- RayCastScene only returns a hit when a shape is in the scene; if the cube is killed or removed, the click will not spawn a projectile.

Games that show it: Simple_Test1

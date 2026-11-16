# 06 Keyboard input
Goal: a wire cube responds to held WASD keys by moving right, left, up, and down on screen.
Needs: 01, 04

1. A game card with the update loop and a shape
   Adding: Game.OnStart (with Engine.ResetCamera, Scene.ClearAll, HUD.Clear), Mesh.Define "Cube", MeshBox(40,40,40), Entity.Spawn("Cube",0,0,0,"cyan"), Game.OnUpdate (add 0.05 to an angle, SetObjectRotation with it)
   Makes this happen: the game runs and a cyan wire cube sits in the middle of the view, slowly turning about 30 times per second.
   Engine calls: Game.OnStart, Engine.ResetCamera, Scene.ClearAll, HUD.Clear, Mesh.Define, MeshBox, Entity.Spawn, Game.OnUpdate, SetObjectRotation
2. A test hook to read the keys
   Adding: Game.OnClick (add a TestKeys handler that reads the keysDown)
   Makes this happen: the game now exposes a TestKeys hook that can be used to test key input without clicking the mouse.
   Engine calls: Game.OnClick
3. Held WASD keys move the cube
   Adding: inside Game.OnUpdate, read the keysDown for the W, A, S, D key codes and add the corresponding movement value to the cube's position
   Makes this happen: holding W moves the cube up (toward minus Y), holding S moves it down (toward plus Y), holding A moves it left, and holding D moves it right.
   Engine calls: Game.OnUpdate
4. Arrow keys move the cube in the same way
   Adding: inside Game.OnUpdate, read the keysDown for the arrow key codes and add the corresponding movement value to the cube's position
   Makes this happen: the arrow keys provide the same left, right, up, and down movement as the WASD keys.
   Engine calls: Game.OnUpdate
5. One press versus held movement
   Adding: inside Game.OnUpdate, only apply movement when the corresponding key is held (keysDown is true), and skip the movement for keys pressed only once
   Makes this happen: pressing a key briefly moves the cube only while the key is held down, so the cube moves smoothly in a direction instead of jumping erratically.
   Engine calls: Game.OnUpdate

Pitfalls:
- Keys are only read inside Game.OnUpdate, not in Game.OnClick; Game.OnClick is the mouse only, so a key press will not trigger movement if read there.
- A plain local variable in Game.OnUpdate starts at 0 every step, so keep the key state in a script-local variable that persists between updates.

Games that show it: Simple_Test1

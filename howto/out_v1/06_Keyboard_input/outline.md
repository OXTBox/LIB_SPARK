# 06 Keyboard input
Goal: A small working 3D game that responds to held and pressed keyboard keys with visible movement.
Needs: none

1. Setting up the keyboard input hook
   Adding: Game.OnClick, keysDown
   Makes this happen: The game registers its keyboard input handler so key presses and key holds are tracked for later use.
   Engine calls: Game.OnClick

2. Adding the TestKeys hook for keyboard testing
   Adding: Game.OnClick
   Makes this happen: A TestKeys handler is added to the game so tests can trigger and inspect keyboard input directly.
   Engine calls: Game.OnClick

3. Adding key code handling for WASD and arrow keys
   Adding: keysDown
   Makes this happen: The keyboard handler maps WASD and arrow key codes to movement inputs, enabling directional movement when keys are pressed or held.
   Engine calls: keysDown

4. Adding movement logic for held keys
   Adding: keysDown
   Makes this happen: The handler applies movement based on held keys, showing the player moving in the selected direction as keys are held down.
   Engine calls: keysDown

5. Adding one press versus held key detection
   Adding: keysDown
   Makes this happen: The handler distinguishes between a single key press and a key held down, so the game can react to both types of input correctly.
   Engine calls: keysDown

Pitfalls:
- Forgetting to map arrow keys to movement directions will leave the game unresponsive to arrow key input, so always verify the key code mappings in the handler.
- Confusing a key press with a key hold will cause the game to move erratically or stop moving, so track key state separately for pressed and held keys.

Games that show it: Simple_Test1, Simple_Test2, VectorPong3D:

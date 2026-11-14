# Probe Vs Cone
PITCH: The player throws a logic-probe spear at a boss guarded by moving shield cubes, collecting keys to unlock the boss and win the level. It is fun because the shield constantly shifts to hide the cubes, forcing quick, clever spear throws.
CONTROLS: Use the arrow keys to move and Space to throw the probe spear.
OBJECTS:
- probe spear | box 40,20 | cyan | moves toward the boss when thrown, bounces off walls, returns to hand after breaking a shield cube
- shield cube | box 60,60 | magenta | blocks the boss path, breaks when hit by the probe spear and drops a key token
- key token | box 20,20 | gold | collected to add to the password, disappears once picked up
- boss | box 120,120 | purple | guarded by shield rings, defeated only when the password is complete
RULES:
- The probe spear moves toward the boss after being thrown and bounces off screen walls until it lies still or breaks a shield cube.
- Shield cubes from the inner ring move outward to fill gaps in the outer ring every few seconds.
- Collecting key tokens adds to the assembled password.
- Breaking a shield cube returns the probe spear to the player's hand.
- The player loses a life each time the probe spear misses the boss and lies still without being picked up.
- Completing the password unlocks the boss, allowing the player to hit it for a level win.
WIN: The player completes the password and defeats the boss to win the level.
LOSE: The player runs out of lives after the probe spear misses the boss and lies still without being collected.
NUMBERS: spear speed=2.5, shield cube inner speed=1.2, shield cube outer speed=0.8, key token speed=0, lives=3, password slots=4
RISK: The dynamic shield ring movement and the probe spear bouncing logic that must stay safe until it is picked up will be the hardest to program.

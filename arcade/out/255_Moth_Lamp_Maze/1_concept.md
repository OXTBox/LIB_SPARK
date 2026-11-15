# Moth Lamp Maze
PITCH: You navigate a dark top-down maze while carrying a lamp, guiding moths around it to reach the exit before the lamp oil runs out. It is fun because every step of the path changes the moth behavior, creating a tight balance between movement and survival.
CONTROLS: Use the arrow keys to move in four directions: up, down, left, and right through the maze.
OBJECTS:
- Moth Lamp | box w=120 h=60 | wireframe cyan | acts as the player's light source that attracts moths and drains oil
- Moth | box w=40 h=40 | wireframe yellow | gathers around the lamp and slows the player's movement
- Fan | box w=200 h=120 | wireframe orange | blows moths away when the player walks under it
- Exit | box w=80 h=80 | wireframe green | marks the goal the player must reach
RULES:
- Moths gather around the lamp and slow the player's movement speed.
- Walking under the fan blows all nearby moths away, clearing the path.
- The lamp oil decreases by one unit every 30 steps.
- Reach the exit before the lamp oil reaches zero to complete the level.
- Each time the player is caught by a moth, one life is lost.
WIN: Reach the exit with remaining lamp oil.
LOSE: Lamp oil reaches zero before reaching the exit.
NUMBERS: lamp_oil=100, moth_speed=1.5, fan_range=150, steps_per_second=30
RISK: Balancing the precise movement speed of moths around the lamp while tracking the oil depletion over time to keep the player's path safe.

# Beacon Chain
PITCH: Walk through the dark wire maze, light every unlit beacon to open the exit, and watch your lit paths connect back to the last lit beacon. It is fun because solving the maze feels like uncovering a hidden light trail in a mysterious dark space.
CONTROLS: Use the arrow keys to move, and press Space to light the current beacon.
OBJECTS:
- Beacon | box w=40 h=40 | colour=light yellow | lights itself and draws a lit line on the floor back to the last lit beacon
- Maze Wall | box w=900 h=600 | colour=dark grey | forms the fixed wireframe maze structure for the level
- Exit Gate | box w=80 h=120 | colour=bright cyan | opens when all beacons in the level are lit, allowing the player to reach the exit
- Player | box w=30 h=30 | colour=white | moves through the maze using arrow keys, standing on the floor to light beacons
RULES:
- The player moves one step per arrow key press, advancing the game clock by 30 steps per second.
- Pressing Space lights the beacon in front of the player and draws a lit line to the last lit beacon.
- Each level contains more beacons and a larger maze than the previous level.
- The score increases by 10 points for every beacon successfully lit.
- Losing a life occurs when the player steps outside the maze walls or fails to light all beacons in the level.
WIN: Reach the exit gate after lighting every beacon in the current level.
LOSE: Step outside the maze walls, or fail to light all beacons in the current level.
NUMBERS: player_speed=1.5, beacon_lit_delay=0.5, level_beacon_count=3, level_maze_size=1.2
RISK: Programming the dynamic lit line rendering that connects beacons and updates the maze structure for each progressively larger level.

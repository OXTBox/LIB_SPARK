# Sweep Patrol
PITCH: Walk over dust cells to sweep them clean while dodging robot vacuums that leave dust behind, and clear every room to advance to harder levels. It is fun because the simple arrow movement creates a tight, satisfying balance between sweeping progress and vacuum evasion.
CONTROLS: Arrow keys only.
OBJECTS:
- dust cell | box w=100 h=100 | wireframe grey | Sweeps clean when stepped on, removing accumulated dust.
- robot vacuum | box w=80 h=80 | wireframe cyan | Moves along its own loop, leaving dust behind as it turns.
- furniture block | box w=150 h=150 | wireframe brown | Stops movement and blocks paths, forcing careful navigation.
- dust pile | box w=200 h=100 | wireframe yellow | Accumulates dust from vacuums, must be swept to clear the room.
RULES:
- Player moves only with arrow keys, one step per 30-step interval.
- Stepping on dust cells sweeps the cell clean and adds to the score.
- Robot vacuums follow fixed loops and leave dust behind when turning.
- Each level adds more vacuums and furniture to increase difficulty.
- Accumulating dust on the floor costs one life.
- Reaching the clear-room goal advances to the next level.
WIN: All dust cells in the current room are swept clean and the player reaches the clear-room goal.
LOSE: The player accumulates enough dust on the floor to lose all lives, or the move count is exhausted.
NUMBERS: player_speed=150, dust_cell_count=20, robot_vacuum_count=3, level_count=3, lives=3, move_count=600
RISK: Programming the robot vacuum loop behavior and ensuring dust accumulation logic stays balanced across increasing level difficulty.

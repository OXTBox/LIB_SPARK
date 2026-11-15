# Key Ring Maze
PITCH: Navigate a top-down maze by swapping coloured keys to unlock coloured locks, opening the path to the exit. It is fun because each level adds new colours and locks that require keys from the far side, creating a rewarding chain of puzzle steps.
CONTROLS: Arrows only. Walking into objects picks them up, swaps them, and presses switches.
OBJECTS:
- Coloured Key | box w=40 h=40 | red | Swaps the carried key when stepped on
- Coloured Lock | box w=60 h=60 | blue | Blocks passage until the matching key is carried
- Exit Door | box w=80 h=80 | green | Opens the path to the exit when unlocked
- Maze Wall | box w=900 h=600 | black | Forms the top-down maze corridors
- Switch Plate | box w=30 h=30 | yellow | Activates a lock when stepped on
RULES:
- Player moves only with arrow keys through the maze walls.
- Carrying one key at a time, walking onto a key swaps it with the carried key.
- Each level adds new colours and locks requiring keys from the far side of other locks.
- Score increases by 10 points for every lock successfully unlocked.
- A life is lost if the player walks into a locked wall or fails to unlock the exit.
WIN: The player reaches the exit door with the correct key combination unlocked.
LOSE: The player runs out of lives while navigating the maze.
NUMBERS: keys=1, locks=3, score=0, lives=3, level=1, speed=30
RISK: Programming the dynamic key-lock colour matching and swapping logic across multiple levels while keeping the top-down maze navigation consistent.

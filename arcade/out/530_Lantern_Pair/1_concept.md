# Lantern Pair
PITCH: The player leapsfrogs through a dark maze to guide the hero holding the lantern toward the exit, using simple key swaps to guide the lantern's light along the path. It is fun because the puzzle feels tight and the dark maze makes every step feel like a careful arcade leap.
CONTROLS: Arrows to move, TAB to swap the lantern between the hero and the player.
OBJECTS:
- Hero | box w=20 h=40 | colour=light yellow | the player's standing character who holds the lantern when not swapped
- Lantern | box w=10 h=10 | colour=bright orange | the glowing object that reaches four cells of light and must be guided to the exit
- Exit | box w=30 h=30 | colour=bright green | the goal cell the lantern must reach to complete the level
- Maze Wall | box w=900 h=600 | colour=black | the dark maze structure that blocks normal movement and defines the path
RULES:
- The hero and player move only through open maze cells, never through walls.
- The lantern stays with the hero unless TAB swaps it to the player, who then carries it forward.
- The lantern's light reaches exactly four adjacent open cells at any time.
- The player scores one point for each successful lantern movement toward the exit.
- Each level increases the maze size and reduces the lantern's light reach by one cell.
- A life is lost if the player moves into a wall or fails to reach the exit within the move limit.
WIN: The player reaches the exit with the lantern held by the player after completing all levels.
LOSE: The player runs out of lives by moving into walls or failing to meet the level move limit.
NUMBERS: hero_speed=10, lantern_speed=10, move_limit=100, lives=3
RISK: Programming the precise lantern light reach and swapping mechanics to guide the lantern through the expanding maze while keeping the 1983 wireframe arcade feel.

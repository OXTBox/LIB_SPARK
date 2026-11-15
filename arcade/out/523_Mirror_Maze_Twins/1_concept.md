# Mirror Maze Twins
PITCH: The player guides two heroes through a top-down maze by swapping their paths, using mirrored corridors to reach two buttons while each hero can see the other in a mirror. It is fun because the player must solve a spatial puzzle that relies on mirror reflections to progress without breaking the heroes' paths.
CONTROLS: Use the arrow keys to move both heroes in the maze, and press TAB to swap their current positions.
OBJECTS:
- Hero | box w=10 h=10 | wireframe cyan | moves along the maze corridors when arrows are pressed
- Mirror | box w=120 h=60 | wireframe magenta | reflects the other hero's corridor so the player can see the path
- Button | box w=30 h=30 | wireframe gold | must be pressed by a hero who can see the other hero in a mirror
- Maze Wall | box w=900 h=600 | wireframe dark grey | blocks movement and creates mirrored corridors
RULES:
- Both heroes move together with each arrow key press, staying inside the maze corridors.
- Pressing TAB swaps the two heroes' current positions instantly.
- Each hero can only reach a button if the other hero is visible in a mirror at the same time.
- The score increases by 1 point for every valid button press.
- A life is lost if either hero collides with a wall or falls out of the maze.
WIN: Reach and press both buttons while each hero can see the other in a mirror.
LOSE: A life is lost when either hero collides with a wall or falls out of the maze.
NUMBERS: hero_speed=15, mirror_speed=0, button_speed=0, wall_speed=0
RISK: Programming the mirror reflection logic to correctly show the other hero's corridor while maintaining the two heroes' independent movement paths without causing unintended collisions.

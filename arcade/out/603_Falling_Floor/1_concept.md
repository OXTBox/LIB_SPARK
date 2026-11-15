# Falling Floor
PITCH: The player navigates a top-down grid room while collecting every gem, avoiding falling cells that vanish after one second, and reaches the exit before the floor collapses around them. It is fun because the constant pressure of falling tiles creates a fast, tense arcade challenge with clear scoring and life limits.
CONTROLS: Use the arrow keys to move and Space to trigger the exit.
OBJECTS:
- Gem | box w=40 h=40 | colour=gold | collects points and removes from the floor
- Falling Cell | box w=60 h=60 | colour=gray | cracks and disappears after one second
- Exit | box w=80 h=80 | colour=green | completes the level and awards the score
- Wall | box w=100 h=100 | colour=blue | blocks movement and prevents falling into unsafe zones
RULES:
- Moving into a falling cell causes it to crack and disappear after one second.
- Collecting every gem adds 100 points to the player's score.
- Falling into a wall or a collapsed zone costs one life.
- The player must reach the exit before the room's floor fully collapses.
- Each level increases the speed of falling cells and room size.
- Losing all lives ends the game.
WIN: The player collects all gems and reaches the exit to complete the level.
LOSE: The player loses all lives and cannot continue moving through the room.
NUMBERS: gem_count=5, falling_cell_speed=120, wall_speed=80, exit_speed=60, level_size=900x600
RISK: Programming the dynamic falling cell logic that updates and removes cells based on player position while maintaining stable room boundaries for the exit and walls.

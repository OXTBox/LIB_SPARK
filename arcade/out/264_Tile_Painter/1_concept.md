# Tile Painter
PITCH: Walk across the grid to paint every floor cell one colour, then reach the exit to clear the level. It is fun because the puzzle changes with each room while the simple colour-changing mechanic stays satisfying.
CONTROLS: Use the arrow keys to move, and press Space to change your current cell colour.
OBJECTS:
- Player | box w=20 h=20 | colour=blue | moves one cell per arrow key press and changes the colour of the cell you stand on
- Floor Cell | box w=40 h=40 | colour=green | changes to the player's chosen colour when stepped on once, reverts to green when stepped on twice
- Exit Door | box w=60 h=60 | colour=purple | opens when the entire floor is painted the single chosen colour, blocking movement until it is unlocked
RULES:
- The player moves one cell per arrow key press, staying inside the room boundaries.
- Each cell changes colour once per single step on it, then reverts to green after a second step.
- The player scores 10 points for every cell successfully painted to the target colour.
- A life is lost if the player steps outside the room boundaries or fails to paint the floor before the level timer ends.
WIN: The player paints the entire floor one colour and reaches the exit door to complete the level.
LOSE: The player runs out of lives by leaving the room or failing to paint the floor before the level timer expires.
NUMBERS: player_speed=150, cell_step_time=30, level_timer=120, lives=3
RISK: Making the colour-reversion logic and pillar route blocking detection work correctly for every level layout without breaking movement.

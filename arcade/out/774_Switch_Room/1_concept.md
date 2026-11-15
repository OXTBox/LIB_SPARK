# Switch Room
PITCH: Step across a top-down room by pressing coloured floor switches to raise and lower wall sections, then reach the exit in the fewest switch presses possible. It is fun because every move changes the room layout and you must plan each switch press carefully to reach the exit quickly.
CONTROLS: Use the arrow keys to move and Space to press a switch.
OBJECTS:
- floor | box 900,600 | black | the playable top-down surface where the player moves
- wall | box 900,600 | red | a wall section that raises when its colour switch is pressed
- wall | box 900,600 | blue | a wall section that raises when its colour switch is pressed
- switch | box 20,20 | red | a floor switch that raises red walls and lowers other coloured walls
- switch | box 20,20 | blue | a floor switch that raises blue walls and lowers other coloured walls
- exit | box 30,30 | green | the goal location to reach after completing switch presses
RULES:
- The player moves only on the black floor surface.
- Pressing a switch raises all walls of its colour and lowers the walls of the other colours.
- Each successful switch press adds one to the total switch count.
- The player loses a life if they fall off the floor or touch a raised wall.
- Each level adds one new colour and one additional exit requiring a key from behind a wall.
- The game ends when the player runs out of lives.
WIN: Reach the exit after completing the required switch presses in the fewest presses possible.
LOSE: Run out of lives by falling off the floor or touching a raised wall.
NUMBERS: player_speed=120, switch_press_cost=1, lives=3, level_colours=3, level_exits=2
RISK: Programming the dynamic wall raising and lowering logic that changes the playable floor layout based on switch presses while tracking the required switch count for each level.

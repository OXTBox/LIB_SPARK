# Two Key Doors
PITCH: Control either of two heroes through a timed maze, opening doors only with their matching key, and reach the exit together for a satisfying arcade challenge. It is fun because the split control and closing doors create constant pressure while the shared goal keeps every move meaningful.
CONTROLS: Use arrow keys to move, TAB to swap control between PROMPT and GLAZE, Space to open doors.
OBJECTS:
- PROMPT | box w=90 h=60 | cyan | moves freely and opens cyan doors
- GLAZE | box w=90 h=60 | magenta | moves freely and opens magenta doors
- Door | box w=120 h=40 | cyan | opens only for PROMPT, closes after 5 seconds
- Door | box w=120 h=40 | magenta | opens only for GLAZE, closes after 5 seconds
- Exit | box w=180 h=120 | cyan | required for both heroes to complete the level
- Floor Plate | box w=100 h=100 | cyan | holds a door open while a hero stands on it
RULES:
- Arrow keys move the selected hero one step in the chosen direction.
- TAB swaps control between PROMPT and GLAZE, the other hero waits in place.
- Space opens the matching door for the active hero, closing it after 5 seconds.
- Standing on a floor plate keeps the associated door open until the hero leaves it.
- Each level adds more plates, longer routes and doors that close on a timer.
- Reaching the exit together with both heroes scores 1000 points.
- Losing a life occurs when a hero runs out of movement space or fails to reach the exit.
WIN: Both PROMPT and GLAZE reach the exit together to complete the level.
LOSE: Running out of movement space or failing to reach the exit with both heroes ends the game.
NUMBERS: PROMPT speed=120, GLAZE speed=120, Door timer=5, Level plates=3, Level doors=2, Exit distance=450
RISK: Programming the timer-based door closure and floor plate door-holding logic while maintaining the split control flow for both heroes in a single screen.

# Mirror Halls
PITCH: Walk through mirrored maze paths to match your twin's exit pads at the same time, using the mirror symmetry of the twin maze to solve each level. It is fun because every step you take creates a mirrored path that helps you reach the shared exit without breaking the twin's route.
CONTROLS: Use the arrow keys to move, and press Space to enter the exit pad.
OBJECTS:
- PROMPT | box w=90 h=60 | cyan | the player who walks the main maze and creates mirrored steps for the twin
- GLAZE | box w=90 h=60 | magenta | the twin hero who follows mirrored steps from the main maze and must reach the exit pad
- Exit Pad | box w=120 h=40 | yellow | the shared destination both heroes must occupy simultaneously to complete the level
- Wall | box w=30 h=30 | grey | solid barrier that blocks only the hero it stops, not the mirrored twin hero
RULES:
- Both heroes move one cell per arrow key press, with the twin moving along mirrored paths created by the player's steps.
- The player scores 10 points for each successful mirrored step taken.
- A hero loses a life if it falls into a wall or fails to reach the exit pad on time.
- Each level increases the number of mirrored cells and maze complexity.
WIN: The player and GLAZE stand on the Exit Pad at the same time to clear the level.
LOSE: The player loses all lives when both heroes fall into walls or the level time limit expires.
NUMBERS: player_speed=150, glaze_speed=150, step_count=0, lives=3, level=1
RISK: Programming the mirrored twin movement logic that adapts to every player step while keeping both heroes' paths consistent with the maze walls.

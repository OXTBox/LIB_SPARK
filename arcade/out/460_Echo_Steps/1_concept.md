# Echo Steps
PITCH: Walk through a dark room using arrow keys to light the floor, dodge your ghost echo, and reach the exit by matching your steps. It is fun because every step leaves a visible trail while a ghost copy of you challenges your rhythm.
CONTROLS: Arrow keys only.
OBJECTS:
- floor | box 900,600 | wireframe cyan | lights the area around the player for a short moment after each step
- walls | box 900,600 | wireframe dark grey | blocks movement and shows within two cells of the player's path
- ghost echo | box 900,600 | wireframe magenta | replays the player's last ten steps and can be touched to send the player back
- exit | box 100,100 | wireframe bright green | completes the level when reached
RULES:
- Each arrow key step moves the player one cell in the chosen direction.
- Each successful step adds one point to the score.
- Touching the ghost echo costs one life.
- The ghost echo follows the player's exact last ten steps.
- The player must reach the exit without losing all lives.
WIN: Reach the exit with at least one life remaining.
LOSE: Lose all lives by touching the ghost echo.
NUMBERS: player_speed=1, ghost_speed=1, score_start=0, lives_start=3, step_count=30
RISK: Programming the ghost echo to accurately replay the player's last ten steps while maintaining smooth top-down movement in the dark room.

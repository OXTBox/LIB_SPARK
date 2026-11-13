# Vine Run
PITCH: The player runs right across a jungle floor while dodging pits, rolling logs, and water, using jumps and vine swings to collect treasure and survive. It is fun because every step feels like a fast arcade chase with clear, immediate rewards for careful movement.
CONTROLS: Use the arrow keys to move right and the Space key to jump or swing.
OBJECTS:
- jungle floor | box w=900 h=600 | wireframe green | acts as the main running surface the player moves along
- pit | box w=120 h=40 | wireframe dark brown | blocks the player, causing a life loss if stepped into
- rolling log | box w=80 h=60 | wireframe brown | rolls across the floor, must be jumped over to avoid
- vine | box w=40 h=120 | wireframe green | allows the player to swing over water, avoiding falling into pits
- treasure | box w=30 h=30 | wireframe gold | adds to the player's score when collected
RULES:
- The jungle floor moves leftward across the screen at a steady speed.
- The player moves right automatically while pressing arrow keys to jump or swing over hazards.
- Collecting each treasure increases the player's score by 10 points.
- Falling into a pit costs one life and resets the player to the left side of the screen.
- The player loses all lives if they fall into a pit or swing into a hazard.
WIN: The player reaches the right edge of the screen with at least one life remaining.
LOSE: The player runs out of all lives while crossing the jungle floor.
NUMBERS: score=0, lives=3, floor_speed=120, pit_count=2, log_count=3, vine_count=1, treasure_count=5
RISK: Programming the smooth, continuous swinging motion over the water using the vine while simultaneously handling pit collisions and hazard avoidance in real time.

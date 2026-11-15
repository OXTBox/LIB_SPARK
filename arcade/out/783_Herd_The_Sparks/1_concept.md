# Herd The Sparks
PITCH: Steer drifting sparks into the corner pen while keeping them away from the electric fence, and grow the pen by clearing levels with more sparks and faster movement. It is fun because the tight, fast control of the sparks creates a constant challenge between driving them safely and filling the pen.
CONTROLS: Arrow keys only.
OBJECTS:
- spark | box w=40 h=40 | wireframe cyan | drifts away from the player and can be guided into the pen
- pen | box w=120 h=120 | wireframe green | collects sparks that enter it and grows with each addition
- electric fence | box w=300 h=60 | wireframe red | blocks sparks that touch it and costs a life
- switch | box w=50 h=50 | wireframe yellow | opens the pen when activated to accept more sparks
RULES:
- Sparks drift away from the player at a steady speed each step.
- Each spark that enters the pen adds one to the pen's collected count and increases the score.
- Sparks that touch the electric fence cost one life.
- Each level increases the number of sparks, their drift speed, and the pen size.
- The game ends when all lives are lost.
WIN: The player clears all levels by filling the final pen to its maximum size.
LOSE: The player runs out of all lives while sparks touch the electric fence.
NUMBERS: sparks=5, pen_width=120, pen_height=120, spark_speed=1.5, level_count=5
RISK: Keeping fast-drifting sparks safely inside the growing pen without letting any touch the electric fence during tight arena movements.

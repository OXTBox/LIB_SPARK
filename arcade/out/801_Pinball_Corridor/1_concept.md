# Pinball Corridor
PITCH: The player drives a wireframe figure through a dark corridor, bouncing off wall bumpers to collect glowing stars while dodging floor drains. The fast, focused movement and precise wall navigation create a tense, arcade-style challenge.
CONTROLS: Use only the left and right arrow keys. The left key moves the player left, the right key moves the player right.
OBJECTS:
- Player | box w=20 h=20 | wireframe cyan | moves through the corridor with left and right input
- Wall Bumper | box w=120 h=30 | wireframe gold | bounces the player along the corridor walls
- Star | box w=10 h=10 | wireframe bright yellow | adds 100 to the player's score when touched
- Floor Drain | box w=80 h=40 | wireframe dark red | removes one life when the player enters it
RULES:
- The player moves one step per key press in the selected direction.
- Collecting a star increases the player's score by 100 points.
- Entering a floor drain costs one life.
- The player cannot move backward; only forward wall bumps advance progress.
WIN: The player collects at least 5 stars to unlock the win state.
LOSE: The player runs out of lives after entering too many floor drains.
NUMBERS: player_speed=15, bumper_speed=10, star_speed=5, drain_speed=8, score_start=0, lives_start=3
RISK: Programming the precise wall bumper collision and drain detection to keep the player's path stable while collecting stars without losing lives.

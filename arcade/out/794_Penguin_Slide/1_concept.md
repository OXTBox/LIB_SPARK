# Penguin Slide
PITCH: The penguin slides down an icy slope on its own while you jump over cracks to catch fish in the air. It is fun because the simple jump controls create a fast, flowing arcade challenge.
CONTROLS: Press the Up key to jump the penguin into the air.
OBJECTS:
- penguin | box w=40 h=60 | colour=blue | slides down the slope automatically and can be jumped by the player
- crack | box w=120 h=20 | colour=black | blocks the slide path and must be jumped over
- fish | box w=30 h=20 | colour=green | can be caught in the air for points
RULES:
- The penguin slides down the slope at a fixed speed every step.
- Catch one fish in the air to add 10 points to the score.
- Jump over cracks to keep the slide path clear.
- Falling into a crack costs one life.
WIN: The score reaches 100 points.
LOSE: Falling into a crack ends the try.
NUMBERS: penguin_speed=15, crack_count=3, fish_count=5, score_start=0, life_start=3
RISK: Programming the precise jump timing to match the slope speed and crack positions for consistent play.

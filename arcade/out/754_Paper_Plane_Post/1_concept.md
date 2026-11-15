# Paper Plane Post
PITCH: The player steers a paper plane rightward over rooftops, collecting letters from open windows and riding the wind past chimneys for a fast, simple arcade score.
CONTROLS: Use the Up and Down keys to steer the plane; press Space to release the plane for a faster glide.
OBJECTS:
- paper plane | box w=120 h=40 | wireframe cyan | moves rightward across the screen, can be steered up and down
- letter | box w=30 h=30 | wireframe gold | scores 100 points when touched by the plane
- open window | box w=60 h=80 | wireframe light blue | allows the plane to pass through, no effect on movement
- chimney | box w=100 h=150 | wireframe dark gray | lifts the plane upward with the wind
RULES:
- The plane moves right automatically at a steady world speed.
- Touching a letter adds 100 points to the score.
- Pressing Space slows the plane's automatic rightward movement.
- Touching a closed window or falling into a wall costs one life.
- The plane falls if it moves below the bottom edge of the screen.
WIN: The score reaches 1000 points before the plane falls.
LOSE: The plane falls below the bottom edge of the screen.
NUMBERS: plane_speed=200, letter_score=100, life_count=3, level_steps=30
RISK: Programming the smooth up and down steering of the paper plane while keeping its automatic rightward movement consistent with the wind effects.

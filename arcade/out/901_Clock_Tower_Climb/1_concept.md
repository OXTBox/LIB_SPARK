# Clock Tower Climb
PITCH: Ride giant clock gears upward through the tower to reach the bell, using precise key movements to guide your path. It is fun because the mechanical climb feels like a real clock mechanism, with every step rewarding your careful navigation.
CONTROLS: Left, right, and up keys for walking and jumping.
OBJECTS:
- Giant Gear | box w=400 h=120 | colour=teal | turns slowly and its teeth act as moving platforms
- Clock Face | box w=200 h=200 | colour=amber | holds the clock mechanism and stops when the gear aligns
- Bell | box w=150 h=150 | colour=red | the final goal to reach after climbing the gears
- Tower Wall | box w=900 h=600 | colour=gray | the fixed side structure of the clock tower
RULES:
- Giant gears rotate slowly and their teeth move as platforms you can ride up.
- Collecting a gear adds 100 points to your score.
- Falling off a gear or hitting the bottom of the tower costs one life.
- The game ends when all gears are collected and you reach the bell.
WIN: Reach the bell after collecting all gears for a high score.
LOSE: Falling off a gear or hitting the bottom of the tower ends the current try.
NUMBERS: gear_speed=2.0, step_count=30, screen_width=900, screen_height=600
RISK: Programming the precise timing of gear rotation and platform alignment to keep the climb stable and fair.

# Hot Air Balloon
PITCH: The player controls a hot air balloon by burning fuel to rise and cooling to sink, letting the wind carry the balloon across the hills until it lands safely on a pad. It is fun because the simple up and down keys create smooth, arcade-style movement through a colorful wireframe landscape.
CONTROLS: Use only the up arrow key to burn fuel and lift the balloon, or use the down arrow key to cool and let the balloon sink.
OBJECTS:
- Hot Air Balloon | box w=40 h=60 | colour=orange | moves up when fuel is burned and sinks when fuel is cooled
- Landing Pad | box w=120 h=40 | colour=green | acts as a safe landing surface for the balloon
- Hill | box w=300 h=200 | colour=blue | provides terrain the balloon must navigate over
- Wind | box w=900 h=10 | colour=white | carries the balloon to the right across the screen
- Score Text | box w=200 h=40 | colour=black | displays the current score and level progress
RULES:
- The balloon moves upward when the up arrow is pressed and downward when the down arrow is pressed.
- Pressing the up arrow increases the balloon's height by 30 world units per step.
- Pressing the down arrow decreases the balloon's height by 20 world units per step.
- The wind continuously carries the balloon to the right by 15 world units per step.
- Landing on a landing pad adds 100 to the score.
- Falling below the bottom of the screen costs one life.
WIN: The balloon lands safely on a landing pad to complete the current level.
LOSE: Falling below the bottom of the screen, which ends the current try.
NUMBERS: balloon_height=0, score=0, lives=3, level=1, wind_speed=15
RISK: Programming the precise height and position balance between the up and down keys to ensure smooth, controlled movement without the balloon falling off the screen.

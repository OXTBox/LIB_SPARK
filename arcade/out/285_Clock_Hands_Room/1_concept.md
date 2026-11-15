# Clock Hands Room
PITCH: Stand in the clock-shaped room and dodge sweeping clock hands while collecting numbered keys in the correct order to score points. It is fun because the challenge stays focused and the clock hands create a constant, satisfying chase.
CONTROLS: Use the arrow keys to move up, down, left, and right through the room.
OBJECTS:
- Clock Hand | box w=100 h=20 | colour=blue | sweeps across the floor in a continuous arc
- Clock Hand | box w=100 h=20 | colour=green | sweeps across the floor in a continuous arc
- Number Key 1 | box w=40 h=40 | colour=red | must be collected first in the correct sequence
- Number Key 2 | box w=40 h=40 | colour=orange | must be collected second in the correct sequence
- Number Key 3 | box w=40 h=40 | colour=purple | must be collected third in the correct sequence
RULES:
- The two clock hands move continuously across the floor in sweeping arcs.
- Collect the numbered keys in the exact order shown on the screen.
- Each correct key collection adds 100 points to the score.
- Missing a key by letting a clock hand touch you costs one life.
- The game ends the try after 3 lives are lost.
WIN: The score reaches the target of 500 points.
LOSE: The 3 lives are lost when a clock hand touches the player.
NUMBERS: hand_speed=150, key_1_x=200, key_1_y=300, key_2_x=400, key_2_y=300, key_3_x=600, key_3_y=300, lives=3, score=0
RISK: The continuous, overlapping movement of the two sweeping clock hands and precise collision detection between the player and the hands will be the hardest part to program.

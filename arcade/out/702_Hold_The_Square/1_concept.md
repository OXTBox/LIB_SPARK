# Hold The Square
PITCH: Stand inside the glowing square to fill a score bar while drones push into the arena, and knock them out from behind to win the round. It is fun because you must balance quick movement and precise positioning to survive each round.
CONTROLS: Use the arrow keys to move and Space to fill the score bar.
OBJECTS:
- glowing square | box 400,400 | cyan | the player arena that fills the score bar when stood inside
- score bar | box 900,20 | green | shows the current fill level for the round
- drone | box 60,60 | red | pushes into the arena from the four sides and costs a life if hit from behind
RULES:
- The glowing square moves to a new position each round, starting slowly and speeding up.
- Drones enter the arena from the four sides at a steady pace.
- Standing inside the glowing square fills the score bar by one unit per step.
- Walking into a drone from behind knocks it out of the arena.
- Filling the score bar to full wins the round and earns extra lives.
- Losing all lives ends the game.
WIN: The score bar fills completely to win the round.
LOSE: Losing all lives ends the game.
NUMBERS: square_speed=10, drone_count=4, score_bar_fill_rate=1, lives=3, steps_per_second=30
RISK: Coordinating the square's position changes with drone entry timing and precise behind-drone movement to keep the score bar full without losing lives.

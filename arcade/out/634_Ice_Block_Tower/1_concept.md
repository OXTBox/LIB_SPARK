# Ice Block Tower
PITCH: Stack sliding ice blocks into a tower to reach the goal line, while melting blocks slowly disappear from the bottom to keep the tower stable. It is fun because you must balance speed and timing to build a tall, safe structure.
CONTROLS: Use left, right, and up keys to move the player and stack blocks respectively.
OBJECTS:
- Player | box w=40,h=60 | blue | moves left, right, and up to stack blocks
- Ice Block | box w=50,h=50 | cyan | slides in from the side and can be stacked into the tower
- Goal Line | box w=100,h=10 | green | marks the target the tower must reach
- Melting Block | box w=50,h=50 | yellow | slowly melts away from the bottom of the tower
RULES:
- Ice blocks slide in from the side at a steady speed.
- Stack blocks with the up key to build the tower upward.
- Reach the goal line to complete the level and add to the score.
- Melting blocks disappear from the bottom every 30 steps, reducing tower stability.
- Lose a life if the tower collapses from melting or unstable stacking.
WIN: Complete the tower to reach the goal line and secure a high score.
LOSE: The tower collapses from melting or unstable stacking, ending the try.
NUMBERS: player_speed=120, block_speed=80, melting_rate=30, goal_height=300
RISK: Balancing the timing of block stacking against the slow melting of tower blocks to prevent collapse while reaching the goal line.

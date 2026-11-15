# Ball Gate Arena
PITCH: Walk through the arena with arrows to push the ball through the lit gate, scoring goals while dodging drones that block your path. It is fun because every step of the game depends on timing the ball and the lit gate to score before the drones close in.
CONTROLS: Arrow keys only. Walking into objects picks them up, pushes them and presses switches.
OBJECTS:
- ball | box w=40 h=40 | cyan | moves with the player and can be pushed through gates
- gate | box w=80 h=80 | magenta | acts as a scoring portal when lit
- drone | box w=60 h=60 | orange | moves toward the player and blocks paths
- switch | box w=30 h=30 | yellow | activates the lit gate after each goal
- arena | box w=900 h=600 | black | contains the gates, ball, drones and switches
RULES:
- The ball moves with the player and can be pushed by walking into it.
- Only the lit gate scores a goal, and the lit gate changes after each goal.
- Drones move toward the player and must be avoided to reach the next gate.
- Each goal adds 100 to the score.
- The player loses a life if a drone touches the player.
WIN: Score 500 points by clearing all four gates in the arena.
LOSE: Lose all lives and the game ends in failure.
NUMBERS: ball_speed=120, gate_speed=0, drone_speed=80, switch_speed=0, lives=3, score=0, steps_per_second=30
RISK: Coordinating the lit gate state, ball movement and drone paths so the player can consistently score goals without being blocked by drones.

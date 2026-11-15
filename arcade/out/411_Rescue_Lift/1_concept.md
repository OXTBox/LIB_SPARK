# Rescue Lift
PITCH: Lower the wireframe cage into the mine shaft to lift miners from their ledges, then raise it back up to score points. It is fun because you must balance speed and cage capacity against falling rocks to save every miner.
CONTROLS: Use only the up arrow to raise the cage and the down arrow to lower it. Press Space to drop the cage immediately.
OBJECTS:
- cage | box w=80 h=60 | cyan | moves up or down with arrow keys and drops instantly on Space
- miner | box w=40 h=50 | orange | waits on a ledge and is lifted when the cage reaches their position
- rock | box w=30 h=30 | red | falls downward from the top of the shaft
- ledge | box w=120 h=20 | yellow | holds miners waiting to be rescued
RULES:
- The cage moves one world unit per step when arrows are pressed.
- Each rescued miner adds 100 points to the score.
- The cage holds three miners at once; adding a fourth miner cracks it and costs one life.
- Falling rocks damage the cage, reducing its remaining life.
- The shaft gets deeper each level, adding more miners and more rocks.
- The player loses a life when the cage is cracked or hits the bottom of the shaft.
WIN: The player rescues all miners in the current level before losing all lives.
LOSE: The player runs out of lives while rescuing miners in the current level.
NUMBERS: cage_speed=1, miner_speed=0, rock_speed=2, lives=3, score=0, level_depth=1
RISK: Balancing the cage movement speed with the timing of falling rocks to avoid cracking the cage while still reaching miners on ledges.

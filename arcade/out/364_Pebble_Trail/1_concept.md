# Pebble Trail
PITCH: Walk through the wire maze with arrow keys while dropping pebbles to mark your path, then collect all your pebbles to reach the exit and score a high score. It is fun because the trail you leave guides your next move and every pebble you collect builds your final score.
CONTROLS: Arrow keys to move, P to drop a pebble.
OBJECTS:
- Pebble | box w=20 h=10 | colour=light gray | stays at the floor where dropped, marks visited floor space
- Pebble Trail | box w=900 h=600 | colour=white | shows the floor path you have marked with pebbles
- Exit | box w=40 h=40 | colour=green | opens when all pebbles are collected, allowing safe exit
- Wall | box w=100 h=600 | colour=dark gray | blocks movement, cannot be passed through
RULES:
- Pebbles stay exactly where they are dropped and remain visible on the floor.
- Move with arrow keys only; walking into walls stops your movement.
- Drop a pebble with P to mark a floor position for your trail.
- Collect all pebbles you have dropped before entering the exit.
- Score increases by 10 for each pebble successfully collected.
- Lose a life if you enter the exit without collecting all pebbles.
WIN: Reach the exit with every pebble collected to complete the level.
LOSE: Enter the exit without collecting all of your dropped pebbles.
NUMBERS: pebbles=0, exit=1, lives=3, score=0, speed=120
RISK: Programming the pebble trail logic to correctly track collected pebbles and gate the exit state without breaking movement controls.

# Echo Bats
PITCH: You pilot a lantern through a dark cave by standing still while flying bats pass, then move to dodge their swoops and reach the exit. It is fun because the simple arrow keys create a tense, reactive chase through a mysterious wireframe cave.
CONTROLS: Use the arrow keys to move the lantern left, right, or stay still in place.
OBJECTS:
- lantern | box w=30 h=20 | colour=light blue | moves with the player and carries the player toward the cave exit
- bat | box w=40 h=20 | colour=dark purple | flies straight across the cave and turns sharply at walls
- cave wall | box w=900 h=600 | colour=dark gray | blocks bat paths and creates the cave layout
- cave exit | box w=80 h=60 | colour=green | marks the goal the lantern must reach to win
RULES:
- Bats fly straight across the cave and change direction when they hit a wall.
- Stand still with the lantern to let bats pass by without risking the player.
- Moving the lantern makes bats swoop directly at the lantern for a higher chance of being caught.
- Reaching the cave exit with the lantern scores a point for each successful pass.
- Being caught by a swooping bat costs one life.
WIN: Reach the cave exit with the lantern to complete the level.
LOSE: Being caught by a swooping bat ends the try.
NUMBERS: lantern_speed=10, bat_speed=15, lives=3, score=0, steps_per_second=30
RISK: Programming the bat pathfinding logic that makes bats turn at walls and swoop toward the lantern when the player moves.

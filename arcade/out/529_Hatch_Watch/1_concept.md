# Hatch Watch
PITCH: Players use arrow keys to guide wandering chicks into warm lamps before they escape the hen house, earning points for each successful hatch. It is fun because every step of the game feels like a quick, focused arcade challenge.
CONTROLS: Arrow keys only: Up moves the player forward, Down moves the player backward, Left moves the player left, Right moves the player right.
OBJECTS:
- Chick | box w=40 h=30 | wireframe green | moves randomly within the hen house until guided to a lamp
- Lamp | box w=60 h=60 | wireframe orange | attracts chicks and completes a hatch
- Hen House | box w=900 h=600 | wireframe grey | contains the chicks and the player, the boundary of the play area
- Door | box w=120 h=120 | wireframe white | opens when chicks wander outside the hen house
- Score | box w=200 h=40 | wireframe yellow | displays the current number of completed hatches
- Lives | box w=150 h=40 | wireframe red | tracks remaining attempts before the game ends
RULES:
- Chicks wander randomly inside the hen house until the player guides them to a lamp.
- Each successful hatch adds one point to the score.
- A chick that wanders outside the hen house through the door costs one life.
- The player moves one unit per arrow key press.
- The game ends when all lives are lost.
WIN: The game ends when all chicks have been successfully hatched and the score is recorded.
LOSE: All lives are lost when chicks wander outside the hen house through the door.
NUMBERS: player speed=10, chick wander speed=5, lamp attraction range=100, lives=3, score start=0
RISK: Programming the random wandering and attraction logic for chicks to reliably guide them to lamps within the hen house boundary.

# Lantern Festival
PITCH: The player moves a small boat along a dark river to guide floating lanterns safely beneath bridge arches, testing precision and timing in a quiet night setting. It is fun because every careful move builds the score while keeping the lanterns safe from the bridges.
CONTROLS: Use only the left and right arrow keys. The left key moves the boat to the left, the right key moves the boat to the right.
OBJECTS:
- boat | box w=100 h=40 | colour=light blue | moves the player boat along the river path
- lantern | box w=30 h=60 | colour=orange | floats slowly along the river toward the bridge arches
- bridge_arch | box w=200 h=100 | colour=dark grey | blocks lanterns if they pass too close
- dock | box w=150 h=30 | colour=dark grey | marks the starting position of the boat
RULES:
- The boat moves one step left or right with each key press, staying within the river path.
- Each lantern floats automatically toward the next bridge arch at a steady speed.
- A lantern scores 100 points when it safely passes under the bridge arch.
- A lantern that touches the bridge arch costs 1 life.
- The game ends when all lanterns have passed the bridges or the player has 0 lives.
WIN: The score is the total points earned from all successfully passed lanterns.
LOSE: The game ends when the player has 0 lives, or all lanterns have safely passed the bridges.
NUMBERS: boat_speed=100, lantern_speed=50, lives=3, score=0, steps_per_second=30
RISK: Programming the precise collision detection between the floating lanterns and the bridge arches to prevent accidental life loss while maintaining smooth lantern movement.

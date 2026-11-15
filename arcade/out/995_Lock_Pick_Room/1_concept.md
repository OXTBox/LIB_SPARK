# Lock Pick Room
PITCH: The player navigates a top-down pin tile room using arrow keys to raise pins in the correct sequence, opening the door to progress through the arcade-style space. It is fun because the challenge comes from precise sequencing rather than speed, rewarding careful planning in a clean wireframe environment.
CONTROLS: Arrow keys move the player, and the up arrow raises a pin tile when the player steps on it.
OBJECTS:
- Player | box w=40 h=40 | colour=blue | moves through the room using arrow keys
- Pin Tile | box w=60 h=60 | colour=green | raises when stepped on, drops if raised out of order
- Door | box w=80 h=120 | colour=orange | opens when all pins are raised in correct order
- Score Counter | box w=120 h=40 | colour=purple | displays the number of pins raised correctly
RULES:
- The player moves through the room using arrow keys only.
- Stepping on a pin tile raises it to the correct state.
- Raising pins out of the required sequence causes them to drop again.
- The door opens only after all pins are raised in the correct order.
- The score increases by 1 for each pin raised correctly.
- A player loses a life if they raise a pin out of order three times.
WIN: The player raises all pins in the correct sequence to open the door and complete the level.
LOSE: A player loses a life for each out-of-order pin raise, and the try ends when the player has three lives lost.
NUMBERS: player_speed=120, pin_tile_size=60, door_width=80, score_counter_width=120, lives=3
RISK: Programming the pin sequence logic to correctly track the required order and handle out-of-order raises while maintaining the wireframe visual style.

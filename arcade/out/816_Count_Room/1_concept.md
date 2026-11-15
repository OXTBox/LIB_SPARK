# Count Room
PITCH: Walk over numbered floor tiles in order to clear the room, and solve each level by matching the hidden number sequence before time runs out. It is fun because the simple movement becomes a tight counting challenge that keeps your focus sharp.
CONTROLS: Use the arrow keys to move, and press Space to confirm your tile selection.
OBJECTS:
- numbered_tile | box w=120 h=60 | wireframe_cyan | displays the current counting number to collect
- wall | box w=180 h=60 | wireframe_magenta | blocks movement and hides the next number
- count_counter | box w=300 h=80 | wireframe_lime | shows the current counting sequence and timer
- key_tile | box w=120 h=60 | wireframe_amber | swaps numbers every 10 seconds during the level
RULES:
- Move only with the arrow keys to step over numbered tiles in order from 1 to 3.
- Collect each numbered tile in the correct counting sequence to advance the level.
- A wrong tile selection resets the count back to 1 immediately.
- Tiles swap numbers every 10 seconds and walls hide the next required number.
- Score increases by 10 points for each correctly collected tile.
- Lose a life when the count timer reaches zero or you fail to collect the required tile.
WIN: Clear all numbered tiles in the correct order to complete the level.
LOSE: Lose all lives when the count timer expires or you miss the required tile sequence.
NUMBERS: count_counter=30, key_tile_swap_interval=10, tile_speed=30
RISK: Programming the dynamic tile number swapping and hidden wall number logic to keep the counting sequence accurate during timed intervals.

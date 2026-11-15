# Pipe Flow Room
PITCH: Walk through a grid of pipe tiles with arrows to turn them into a connected water path from the tank to the drain, solving each level before the tank overflows. It is fun because every step shapes the flow and the challenge grows with each level.
CONTROLS: Arrow keys only; walking onto a tile turns it a quarter.
OBJECTS:
- Tank | box w=120 h=80 | colour=teal | acts as the water source that fills over time
- Pipe Tile | box w=60 h=60 | colour=blue | can be turned a quarter by walking onto it
- Drain | box w=100 h=60 | colour=orange | receives the connected water flow to finish the level
- Fixed Pipe | box w=60 h=60 | colour=gray | cannot be turned, blocks the path
- Water Stream | box w=40 h=40 | colour=purple | flows through connected pipe tiles to the drain
RULES:
- Only arrow keys move the player through the grid.
- Walking onto a turnable pipe tile rotates it a quarter.
- Connect the tank to the drain with continuous pipe paths.
- Score points for each correctly connected pipe tile.
- The tank overflows and costs a life if the time limit ends without a connection.
WIN: The player connects the tank to the drain within the level time limit.
LOSE: The tank overflows before the player connects the tank to the drain.
NUMBERS: tank_fill_rate=1.5, level_time=60, pipe_tile_rotation_quarter=90, screen_width=900, screen_height=600
RISK: Programming the real-time water flow simulation that connects rotating pipe tiles to the drain while enforcing the time limit and overflow life loss.

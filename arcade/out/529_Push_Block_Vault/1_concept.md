# Push Block Vault
PITCH: Push stone blocks across the grid to fill marked tiles and open the vault door, solving tight top-down puzzle rooms while earning bonus points for efficient moves. It is fun because every step feels like a deliberate puzzle solve with clear, satisfying feedback on each successful push.
CONTROLS: Use arrow keys to move blocks and Space to undo the last move.
OBJECTS:
- Stone Block | box 40,40 | wireframe cyan | Moves one square in the direction of the arrow key when pushed, stopping at walls.
- Marked Tile | box 40,40 | wireframe gold | Acts as a required target tile that must be filled by a stone block to unlock the vault door.
- Vault Door | box 60,60 | wireframe red | Opens when all marked tiles are filled, granting the level completion score.
- Floor Tile | box 40,40 | wireframe black | Acts as empty walkable space, or becomes floor after a block is swallowed by a pit.
- Pit | box 40,40 | wireframe dark gray | Swallows a pushed block, converting it into a floor tile.
WIN: Complete all marked tiles with stone blocks to open the vault door and clear the level.
LOSE: Lose all lives when a block falls into a pit or a move limit is exceeded without opening the vault door.
NUMBERS: blocks=3, marked_tiles=4, lives=3, move_limit=120, pit_count=2, speed=120
RISK: Programming the block movement logic with collision detection against walls and pit conversion rules to ensure blocks stop correctly and only move when pushed.

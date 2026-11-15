# Crystal Pairs
PITCH: Walk through the covered tiles to uncover matching crystals in a row, keeping them while avoiding mismatches that cover them again. It is fun because clearing the room in few steps rewards quick, careful movement.
CONTROLS: Arrows only. Walking onto tiles uncovers them, pushes crystals and triggers switches.
OBJECTS:
- covered tile | box w=900 h=600 | wireframe cyan | uncovers the tile beneath when stepped on
- crystal | box w=40 h=40 | wireframe gold | stays when matched in a row, gets covered when mismatched
- switch | box w=60 h=60 | wireframe magenta | unlocks the next uncovered tile when stepped on
- score counter | box w=200 h=60 | wireframe white | shows the current score
- life indicator | box w=120 h=60 | wireframe green | shows remaining lives
RULES:
- Arrows move the player one tile per step.
- Stepping on a tile uncovers it, revealing its crystal.
- Two matching crystals in a row keep both crystals.
- A mismatched crystal pair covers both crystals again.
- Each successful match adds 10 to the score.
- A mismatch costs 1 life.
- The room clears when all tiles are uncovered and no crystals remain.
WIN: The room is fully cleared with a positive score.
LOSE: All lives are lost before the room is cleared.
NUMBERS: player_speed=150, score_start=0, lives_start=3, tile_count=12, crystal_count=12
RISK: Tracking crystal positions and matching logic across multiple uncovered tiles in real time.

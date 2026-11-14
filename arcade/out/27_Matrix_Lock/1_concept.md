# Matrix Lock
PITCH: Walk along the grid floor to dodge falling wireframe shapes, rotate them to clear rows and score points. It is fun because every step tests your reaction while building a clean, structured arcade flow.
CONTROLS: Use arrow keys to move, Space to rotate the falling shape.
OBJECTS:
- falling shape | box 80,80 | cyan wireframe | drops from above one at a time, stays in place after landing
- player figure | box 40,40 | magenta wireframe | stands on the grid floor, can move along it
- floor grid | box 900,600 | black wireframe | provides the walkable grid surface for the player and landing zones
- score counter | box 120,40 | yellow wireframe | displays the current score of cleared rows
- life indicator | box 100,40 | red wireframe | shows remaining lives for the player
WIN: Clear enough filled rows to complete the level.
LOSE: The player is walled in with no free cell to step to, or a falling shape lands on the player figure.
NUMBERS: speed=120, lives=3, score=0, rows_to_clear=10
RISK: Programming the collision detection between the player figure and falling shapes while maintaining smooth wireframe rendering on the grid floor.

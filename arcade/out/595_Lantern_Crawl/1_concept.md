# Lantern Crawl
PITCH: You explore a dark wireframe maze with a lantern that only lights the next three cells, refilling as you enter dead ends, and reach the exit stair before the light fades. It is fun because every step tests your navigation and timing against a shrinking light.
CONTROLS: Use the arrow keys to move, and press Space to enter the exit stair.
OBJECTS:
- lantern | box w=3, h=1 | colour=amber wireframe | lights the next three walkable cells and burns down as you move
- oil flask | box w=1, h=1 | colour=olive wireframe | refills the lantern when placed in a dead end
- exit stair | box w=4, h=1 | colour=cyan wireframe | marks the goal to reach for the level
- wall | box w=900, h=600 | colour=black wireframe | forms the maze boundary and blocks movement
RULES:
- The lantern lights exactly three adjacent walkable cells and loses one unit of charge each step you move.
- Oil flasks only refill the lantern when you stand in a dead end cell.
- Moving into a non-lit cell costs one life if the lantern charge reaches zero before you reach the stair.
- Reaching the exit stair completes the level and adds 100 to the score.
- Each level increases maze size and reduces available oil flask count.
- The score resets to zero at the start of each new level.
WIN: Reach the exit stair before the lantern charge reaches zero to complete the level.
LOSE: The lantern charge hits zero while you are in a dark, unlit cell before reaching the exit stair.
NUMBERS: lantern_charge=3, oil_flasks=4, level_size=3, steps_per_second=30, screen_width=900, screen_height=600
RISK: Managing the lantern charge and dead-end refill timing while navigating larger maze layouts with fewer oil flasks.

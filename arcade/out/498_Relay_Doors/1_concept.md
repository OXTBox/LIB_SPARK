# Relay Doors
PITCH: Players navigate a top-down maze by swapping plates to open doors, taking turns holding doors for each other to reach the exit together. It is fun because the puzzle requires quick teamwork to unlock every path before the game ends.
CONTROLS: Arrows to walk, TAB to swap plates.
OBJECTS:
- hero | box w=40 h=40 | wireframe cyan | moves through the maze and holds plates to open doors
- plate | box w=30 h=30 | wireframe yellow | stays down only while a hero stands on it, opens doors when held
- door | box w=60 h=60 | wireframe magenta | blocks the path until a plate is held on it
- switch | box w=20 h=20 | wireframe green | triggers when a plate is held on it, opening the connected door
- exit | box w=100 h=100 | wireframe white | the goal to reach together with the hero
RULES:
- Heroes walk with arrow keys and swap plates using TAB.
- Plates stay down only while a hero stands on them.
- Doors open when a plate is held on them.
- Switches trigger when a plate is held on them to open connected doors.
- Reach the exit together to complete the level.
- Each failed door attempt costs one life.
- The game ends after three lives are lost.
WIN: The hero reaches the exit together with the other hero after all doors are opened.
LOSE: The player loses all three lives when doors cannot be opened or the hero cannot reach the exit.
NUMBERS: hero speed=120, plate speed=0, door speed=0, switch speed=0, exit speed=0, lives=3, level steps=30
RISK: Programming the turn-based plate and door interaction logic so plates only remain down while a hero stands on them and doors open correctly when plates are swapped.

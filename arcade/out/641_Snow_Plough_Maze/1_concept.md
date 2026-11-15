# Snow Plough Maze
PITCH: Drive the snow plough through a snowy town street grid, clearing paths to reach every house from the hospital, and keep the cleared routes open as snow falls back. It is fun because you must plan your route carefully while managing the snow that erases your progress.
CONTROLS: Arrow keys only.
OBJECTS:
- Snow Plough | box 60,30 | wireframe cyan | moves with arrow keys to clear the street cell beneath it
- Snow Cell | box 40,40 | wireframe white | gets cleared when the plough drives over it, then falls back to snow after a delay
- Street Grid | box 900,600 | wireframe grey | the town layout where the plough travels and houses are placed
- House | box 50,50 | wireframe blue | a required destination that must be reached from the hospital
- Hospital | box 50,50 | wireframe green | the starting point for the route to every house
RULES:
- The plough moves one cell per arrow key press, clearing the cell it enters.
- Snow falls back onto cleared cells after 10 seconds, erasing the cleared path.
- A score of 100 points is added for each house successfully reached.
- Each house reached incorrectly costs one life.
- The game ends when all houses are cleared and the route remains open.
WIN: All houses are reached from the hospital with the route remaining open after snow falls.
LOSE: All lives are used while failing to clear the route to every house.
NUMBERS: plough speed=100, snow fall delay=10, house score=100, lives=3, steps per second=30.
RISK: Programming the snow fall-back logic that erases cleared cells while the player continues driving through the grid.

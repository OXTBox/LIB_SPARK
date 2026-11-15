# Twin Lifts
PITCH: Guide two heroes through side-by-side lift shafts to reach the roof, swapping them to open doors on every floor. It is fun because the path depends on both heroes working together at each level.
CONTROLS: Arrow keys to move, TAB to swap heroes.
OBJECTS:
- PROMPT | box 900,30 | wireframe cyan | moves upward when its hero stands inside
- GLAZE | box 900,30 | wireframe magenta | moves upward when its hero stands inside
- DOOR | box 120,120 | wireframe yellow | opens when its hero stands inside
- FLOOR | box 900,60 | wireframe grey | blocks movement until its hero stands inside
- ROOF | box 900,60 | wireframe white | final destination for both heroes
RULES:
- Each hero can only move while standing inside their own lift shaft.
- Heroes swap positions with TAB to access the other lift.
- A hero opens a door when standing inside it, allowing passage to the next floor.
- The player scores 100 points for each door opened.
- A hero loses a life if they fall into a gap between floors.
WIN: Both heroes reach the roof on the final level.
LOSE: A hero falls into a gap between floors and the game ends.
NUMBERS:
- PROMPT speed=12
- GLAZE speed=12
- DOOR speed=0
- FLOOR speed=0
- ROOF speed=0
RISK: Coordinating the movement of two heroes in side-by-side shafts while managing door and floor states across multiple levels.

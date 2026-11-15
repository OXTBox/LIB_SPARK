# Night Bus
PITCH: Drive the wireframe night bus along the dark road and stop at lit bus stops by slowing near them to catch passengers, building a fun score while avoiding missed stops.
CONTROLS: Use only the left and right keys: left moves the bus left, right moves the bus right.
OBJECTS:
- bus | box 400,120 | wireframe blue | moves along the dark road and stops at lit bus stops
- bus stop | box 80,60 | wireframe green | marks the lit stops where the bus must slow to catch passengers
- passenger | box 30,40 | wireframe yellow | adds to the score when caught at a stop
RULES:
- The bus moves automatically forward along the dark wire road.
- Slow near a lit bus stop to catch the passenger and add to the score.
- Missing a lit bus stop loses one passenger.
- The score increases by one for each passenger caught correctly.
- Losing all passengers ends the try.
WIN: The score reaches the target passenger count to complete the level.
LOSE: Losing all passengers ends the try.
NUMBERS: bus speed=120, passenger score=1, passenger count=5, stop distance=200
RISK: Programming the precise slowing behavior near lit bus stops to catch passengers without missing them.

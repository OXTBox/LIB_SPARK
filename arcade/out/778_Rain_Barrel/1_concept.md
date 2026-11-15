# Rain Barrel
PITCH: You steer a barrel along rooftops to catch overflowing gutters, filling it until you empty it into the tank. It is fun because every rain catch is a quick, satisfying arcade challenge.
CONTROLS: Use only the left and right keys. The left key moves the barrel left, the right key moves the barrel right.
OBJECTS:
- barrel | box w=20 h=40 | wireframe cyan | carries rain from gutters to the tank
- gutter | box w=30 h=20 | wireframe blue | overflows rain that must be caught
- tank | box w=120 h=60 | wireframe green | receives the full barrel to score points
- raindrop | box w=10 h=10 | wireframe yellow | falls from the gutter and must be caught by the barrel
- rooftop | box w=900 h=200 | wireframe grey | the fixed side view surface the barrel moves along
RULES:
- The barrel moves only with the left and right keys, staying on the rooftop surface.
- Catching a raindrop fills the barrel by one unit.
- A full barrel is emptied into the tank instantly.
- Each successfully emptied barrel scores 100 points.
- Falling off the rooftop costs one life.
WIN: The score reaches 500 points.
LOSE: Falling off the rooftop costs one life; three lives ends the game.
NUMBERS: barrel_speed=120, gutter_overflow_rate=40, tank_capacity=100, score_per_emptied_barrel=100, lives=3, steps_per_second=30
RISK: Keeping the barrel precisely aligned to catch overflowing gutters while moving along the rooftop without missing any rain is the hardest part to program.

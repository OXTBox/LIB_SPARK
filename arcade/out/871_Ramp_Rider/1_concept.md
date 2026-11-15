# Ramp Rider
PITCH: Tilt the dirt bike through ramps and mud to race three other riders, using precise air control and turbo power to finish the course without overheating. It is fun because every jump and landing decision directly shapes your race result and keeps the 1983 arcade challenge tight and exciting.
CONTROLS: Use arrow keys to tilt the bike and Space to activate turbo.
OBJECTS:
- Dirt Bike | box w=120 h=60 | wireframe orange | the player’s racing vehicle that moves along the course
- Rider 1 | box w=80 h=100 | wireframe blue | the first opponent that races alongside the player
- Rider 2 | box w=80 h=100 | wireframe green | the second opponent that races alongside the player
- Rider 3 | box w=80 h=100 | wireframe purple | the third opponent that races alongside the player
- Turbo Fuel | box w=100 h=40 | wireframe yellow | powers the bike for faster movement and higher jumps
- Overheat Warning | box w=120 h=50 | wireframe red | shows when the engine is overheated and the bike must cool down
RULES:
- The dirt bike moves forward along the course while the player tilts it with arrow keys.
- Landing flat on a ramp or flat ground scores points equal to the jump height reached.
- Landing badly causes the bike to tumble and costs one life.
- Holding Space for turbo increases speed and jump height but consumes fuel.
- The engine overheats after sustained turbo use and requires a cool-down pause before racing resumes.
- The first rider to finish the course wins the race, with higher finishing positions awarding bonus points.
- Losing all lives ends the race immediately.
WIN: The player finishes the course first and retains at least one life.
LOSE: The player loses all lives during the race or finishes the course last.
NUMBERS: bike_speed=220, rider_speed=180, turbo_speed=280, lives=3, score=0, course_length=1200, fuel=100
RISK: Programming precise air-tilt physics to ensure stable landing on ramps while managing turbo fuel and overheating constraints without causing unfair tumble outcomes.

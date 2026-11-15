# Lift Bridge
PITCH: Raise and lower the bridge to guide boats over safely while keeping cars on the road, creating a fast, focused challenge that rewards quick, precise decisions.
CONTROLS: Use the up key to raise the bridge and the down key to lower the bridge.
OBJECTS:
- Bridge | box 900, 100 | wireframe blue | moves up or down to let boats cross or block cars
- River | box 900, 600 | wireframe cyan | the water path boats travel along
- Boat | box 100, 30 | wireframe green | travels along the river to cross the bridge
- Car | box 120, 50 | wireframe orange | travels along the road to cross the bridge
RULES:
- The bridge rises and lowers smoothly with each key press.
- Boats pass safely when the bridge is high enough for them.
- Cars pass safely when the bridge is low enough for them.
- A boat hitting a low bridge or a car falling into the river costs one life.
- The score increases by 1 point for each safe crossing.
WIN: The player completes all required safe crossings without losing all lives.
LOSE: A boat hits a low bridge or a car falls into the river, ending the try.
NUMBERS: bridge_height=100, boat_speed=12, car_speed=18, lives=3, score=0
RISK: Precisely timing the bridge height to match the speed and size of moving boats and cars without causing collisions.

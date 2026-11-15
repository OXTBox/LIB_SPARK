# Treasure Map Steps
PITCH: Follow the exact map directions step by step from the palm tree to dig the hidden treasure, and solve the island puzzle by making every move correct. It is fun because each wrong step reveals a cross and you must carefully track the map to reach the treasure without losing your chance.
CONTROLS: Use the arrow keys only: up moves north, down moves south, left moves west, right moves east.
OBJECTS:
- palm tree | box w=100 h=100 | green | the starting point of the map path
- map panel | box w=200 h=100 | yellow | shows the required north and east steps
- treasure chest | box w=80 h=80 | gold | the goal to reach after following the map
- cross marker | box w=40 h=40 | red | shows a wrong step was taken
RULES:
- The player moves one step at a time in the direction of the arrow keys.
- The map panel shows the required number of north and east steps to follow.
- Each correct step advances the player along the map path.
- Each wrong step places a red cross marker on the current position.
- The player wins by reaching the treasure chest after following all map steps exactly.
- Each wrong step costs one life.
WIN: Reach the treasure chest after following the map steps exactly.
LOSE: Lose all lives after taking wrong steps.
NUMBERS: start_steps=8, lives=3, move_speed=30, screen_width=900, screen_height=600
RISK: Tracking the exact map path step by step and correctly detecting whether each player move matches the required direction to avoid placing cross markers.

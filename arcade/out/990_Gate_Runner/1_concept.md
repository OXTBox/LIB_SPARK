# Gate Runner
PITCH: Guide a wireframe car along a dark track by matching your current colour to incoming gates, and pass through white gates to swap colours for a new run. It is fun because the fast, colour-matching challenge keeps your focus sharp and every swap adds a fresh challenge.
CONTROLS: Use only the left and right arrow keys and Space.
OBJECTS:
- car | box w=120 h=60 | white | moves along the wire track with left and right input
- white gate | box w=80 h=120 | white | swaps the player's current colour when passed through
- red gate | box w=80 h=120 | red | blocks the player unless the current colour matches red
- track | box w=900 h=600 | black | provides the wireframe path for the car to travel along
RULES:
- The car moves forward automatically along the wire track.
- Left and right arrow keys move the car one step left or right along the track.
- Passing through a matching coloured gate scores 100 points.
- Passing through a white gate swaps the player's current colour.
- Hitting a gate that does not match the current colour costs one life.
- Each level increases the gate speed by 2 world units per step.
- The player loses a life when the car leaves the track boundaries.
WIN: The player reaches the final level without losing all lives.
LOSE: The player loses all lives and cannot continue the run.
NUMBERS: car speed=30 steps per second, level 1 gate speed=20 world units per step, starting lives=3, starting score=0, total levels=5
RISK: Programming the dynamic colour-matching logic for gates that change speed and colour state across levels while keeping the wireframe rendering consistent.

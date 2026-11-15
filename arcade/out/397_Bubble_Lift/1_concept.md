# Bubble Lift
PITCH: Ride rising bubbles through an underwater cave to reach the top ledge, avoiding eels that cross the water for a fast, focused arcade challenge.
CONTROLS: Use only the left and right keys: left moves the player left, right moves the player right.
OBJECTS:
- Player | box w=20 h=40 | wireframe cyan | moves left or right with the arrow keys
- Bubble | box w=60 h=120 | wireframe yellow | rises upward when stood on, carries the player up
- Vent | box w=40 h=80 | wireframe orange | emits a bubble that rises from the bottom
- Eel | box w=100 h=60 | wireframe green | swims horizontally across the water
RULES:
- Bubbles rise steadily from vents and can only be ridden when the player stands on them.
- Stepping off a bubble at the top ledge scores one point.
- Eels cross the water horizontally and catch the player if they touch them.
- The player loses a life for each eel caught.
- The game ends when the player has no lives left.
WIN: Reach the top ledge on a single ride to complete the level.
LOSE: The player loses all lives after being caught by an eel.
NUMBERS: player_speed=150, bubble_speed=80, eel_speed=60, lives=3, score=0
RISK: Coordinating the player's movement with bubble rise timing while preventing eels from catching the player mid-ride.

# Sky Raiders
PITCH: You control a cannon at the bottom of the screen and shoot at marching raiders marching down the top, clearing each row before they reach the floor. It is fun because every shot is a quick decision and the rows keep coming faster as the game advances.
CONTROLS: Use the arrow keys to move the cannon and Space to fire.
OBJECTS:
- cannon | box 120,30 | cyan | moves left or right with arrow keys and fires a shot when Space is pressed
- raider | box 80,100 | red | marches sideways across the top and steps down at each edge
- shot | box 20,20 | yellow | travels upward from the cannon and destroys raiders it hits
RULES:
- Raiders march sideways across the top and step down one row at each edge.
- The cannon slides freely along the bottom of the screen.
- Each raider cleared from a row scores 100 points.
- Raiders that reach the bottom cost one life.
- The raider speed increases by 5 world units per step as levels progress.
WIN: Clear all rows before any raider reaches the bottom.
LOSE: Lose all lives when raiders reach the bottom of the screen.
NUMBERS: cannon_speed=2, raider_speed=10, shot_speed=15, lives=3, score=0, rows=5
RISK: The dynamic speed scaling of the raiders while managing the cannon's movement and shot timing without missing any raider rows.

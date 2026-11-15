# Star Weaver
PITCH: The player navigates under a star dome, drawing lines between stars to trace the shape shown in the corner, creating a beautiful cosmic artwork. It is fun because every stroke connects the stars and builds a unique, rewarding cosmic pattern.
CONTROLS: Arrow keys to turn and tilt the view, Space to draw a line between the current star and the next selected star.
OBJECTS:
- Star | box w=100 h=100 | colour=gold | acts as a fixed point the player can select to draw lines from
- Line | box w=30 h=30 | colour=blue | connects two selected stars to form the traced shape
- Corner Shape | box w=400 h=300 | colour=purple | shows the target pattern the player must complete
- Star Dome | box w=900 h=600 | colour=white | provides the starfield background for drawing lines
RULES:
- The player uses arrow keys to rotate and tilt the view of the star dome.
- Space draws a line between the currently selected star and the next star in the view.
- Each completed line adds to the player's score based on the length of the drawn line.
- The player loses a life if they accidentally draw a line that does not match the target shape.
- The game ends with a win when the player completes all required lines of the target shape.
WIN: The player successfully traces the complete target shape shown in the corner.
LOSE: The player loses all lives after drawing incorrect lines that do not match the target shape.
NUMBERS: stars=10, lines=5, lives=3, score=0, speed=1.0
RISK: Programming the precise star selection and line alignment logic to match the target shape accurately while handling player view rotations smoothly.

# Stack Down
PITCH: You guide falling four-block shapes through arrow controls to clear full rows and score points, while keeping the well from filling to the top. It is fun because every move directly affects the score and your survival in a tight, fast arcade loop.
CONTROLS: Use the arrow keys to slide and turn the falling shape, and press Space to drop it into the well.
OBJECTS:
- falling shape | box w=4 h=4 | wireframe cyan | the shape that falls one block at a time into the well
- well | box w=900 h=600 | wireframe amber | the vertical space where shapes land and rows disappear
- arrow guide | box w=100 h=20 | wireframe blue | the control interface for sliding and turning the falling shape
- score display | box w=200 h=40 | wireframe green | shows the current score earned from cleared rows
- life display | box w=100 h=40 | wireframe red | shows the remaining lives before the game ends
RULES:
- The falling shape moves one block at a time downward into the well.
- Arrow keys slide and turn the shape before it drops into the well.
- A full row of four blocks disappears and adds points to the score.
- Each drop costs one life if the shape lands outside the valid well area.
- The game ends when the well fills to the top of the screen.
WIN: The game ends when the well fills to the top, but you win if you reach a score of 1000 or more before that happens.
LOSE: The game ends when the well fills to the top or your lives reach zero.
NUMBERS: score_start=0, lives_start=3, speed_start=1.5, steps_per_second=30
RISK: Programming the precise collision detection and row-clearing logic for the falling shape and well to ensure consistent scoring and life costs without errors.

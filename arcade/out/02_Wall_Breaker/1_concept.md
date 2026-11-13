# Wall Breaker
PITCH: The player controls a bat to keep a ball in play while the ball knocks out rows of bricks at the top, clearing every brick to finish the level. It is fun because the fast, precise movement creates a tight, satisfying challenge between keeping the ball and destroying the wall.
CONTROLS: Use the arrow keys to move the bat and Space to launch the ball.
OBJECTS:
- ball | box w=30 h=30 | wireframe cyan | moves upward when launched, stays in play when guided by the bat
- bat | box w=40 h=20 | wireframe magenta | moves with arrow keys, catches the ball to keep it in play
- bricks | box w=90 h=120 | wireframe orange | form rows at the top, are destroyed when hit by the ball
WIN: Clear all bricks in the level to complete the game successfully.
LOSE: The ball falls past the bat, costing one life.
NUMBERS: ball_speed=120, bat_speed=60, lives=3, levels=1
RISK: Coordinating the bat's movement with the ball's trajectory to prevent the ball from falling past the bat while still allowing it to hit the bricks.

# Bat Duel
PITCH: You control the left bat to keep a bouncing ball between the two bats, using precise vertical movement to score points and earn high scores. It is fun because the fast, rhythmic back-and-forth duel creates a tight, engaging challenge that rewards quick, accurate control.
CONTROLS: Use the arrow keys to move the left bat up and down, and press Space to score a point.
OBJECTS:
- Left Bat | box w=120 h=20 | colour=blue | acts as the player-controlled bat that moves vertically with arrow keys
- Right Bat | box w=120 h=20 | colour=green | acts as the computer-controlled bat that moves automatically to track the ball
- Ball | box w=20 h=20 | colour=yellow | bounces back and forth between the two bats to score points
RULES:
- The left bat moves only up and down with the arrow keys, while the right bat moves automatically.
- A point is scored every time the ball passes a bat.
- The ball bounces between the two bats at a constant speed.
- Each life lasts for 30 points before it is lost.
- Losing all lives ends the game.
WIN: The player scores more than 300 points before losing all lives.
LOSE: The player loses all lives and the game ends in failure.
NUMBERS: ball_speed=40, lives=3, points_per_life=30, score_start=0
RISK: Programming the automatic movement of the right bat to perfectly track the ball while keeping the left bat responsive with arrow keys is the hardest part to implement.

# Vector Pong 3D
PITCH: Slide your bat left, right, up and down to keep the ball in the 3D tennis court, and angle shots off the side walls and ceiling to score points against the computer bat. The ball travels deep into the court and bounces off floating obstacles, creating fast-paced depth challenges.

CONTROLS: Use the arrow keys to move the bat and Space to shoot the ball.

OBJECTS:
- Player Bat | box w=120, h=40 | cyan | moves with arrow keys and shoots the ball when Space is pressed
- Computer Bat | box w=120, h=40 | magenta | moves automatically toward the ball and returns it to the court
- Ball | box w=30, h=30 | yellow | travels through the court, bounces off walls and floating obstacles, and scores a point when it passes a bat
- Floating Obstacle | box w=60, h=60 | orange | bounces the ball mid-court and adds depth to the court
- Side Wall | box w=900, h=150 | grey | blocks shots from the sides of the court
- Ceiling | box w=900, h=100 | grey | blocks upward shots into the court

RULES:
- The ball moves forward through the 3D court at a fixed speed each step.
- The player bat moves with arrow key input and shoots the ball when Space is pressed.
- The computer bat automatically tracks the ball and returns it to the court.
- A point is scored when the ball passes either bat.
- The player loses a life for each missed shot that leaves the court.
- The player gains a point for each successful shot that reaches the opponent bat.
- The game restarts with a new set of lives after a life is lost.

WIN: Win the game by scoring more points than the computer bat.
LOSE: Lose the game after all lives are used up.
NUMBERS: ball_speed=120, player_lives=3, computer_points=0, player_points=0, step_count=30
RISK: Programming the 3D ball trajectory and floating obstacle collision logic while keeping the wireframe arcade visuals consistent.

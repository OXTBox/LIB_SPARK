# Mirror Shots
PITCH: Players steer a light beam through angled mirror rooms to hit a glowing target, using mirrors to redirect the beam with every step. It is fun because the challenge comes from precise spatial planning and quick mirror placement.
CONTROLS: Use the arrow keys to move, and press Space to fire the light beam ahead.
OBJECTS:
- player | box w=20 h=20 | wireframe cyan | moves through the room with arrow keys
- mirror | box w=40 h=40 | wireframe magenta | reflects the light beam when touched
- target | box w=30 h=30 | wireframe gold | must be hit by the light beam to score
- light beam | box w=10 h=10 | wireframe white | travels forward when Space is pressed and bounces off mirrors
RULES:
- The player moves one step in the direction of the arrow keys each step.
- Mirrors reflect the light beam instantly when the player walks into them.
- The light beam travels forward from the player's position when Space is pressed.
- Hitting the target with the light beam adds 100 to the score.
- The player loses a life if the light beam hits a wall without hitting the target.
WIN: The player reaches the target with the light beam and the score reaches 300.
LOSE: The player runs out of all lives and cannot reach the target.
NUMBERS: player_speed=100, mirror_speed=0, target_speed=0, beam_speed=150, lives=3, score=0, steps_per_second=30
RISK: Programming the precise reflection logic for angled mirrors to ensure the beam bounces correctly without missing the target or hitting walls.

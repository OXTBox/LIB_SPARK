# Dot Maze
PITCH: The player navigates a winding corridor maze, collecting every glowing dot while dodging two fast chasers that follow their movement. It is fun because the constant chase creates a tight, focused arcade challenge with clear scoring goals.
CONTROLS: Use the arrow keys to move through the maze and Space to collect dots.
OBJECTS:
- player | box w=40 h=40 | cyan | moves through the maze and collects dots
- dot | box w=20 h=20 | yellow | adds to the player's score when touched
- chaser | box w=30 h=30 | red | moves after the player and costs a life on contact
RULES:
- The player moves one step per arrow key press, while chasers follow the player's path.
- Each dot collected increases the player's score by 10 points.
- Touching a chaser immediately costs one life.
- The level ends when all dots in the maze are collected.
- The player loses a life if they touch a chaser and has no remaining lives.
WIN: The player collects every dot in the maze to complete the level successfully.
LOSE: The player runs out of lives after touching a chaser, ending the game.
NUMBERS: player_lives=3, chaser_speed=120, dot_speed=60, step_duration=30
RISK: Programming the real-time chaser path that smoothly follows the player's movement while maintaining the 1983 wireframe arcade visual style.

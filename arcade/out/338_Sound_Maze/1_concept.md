# Sound Maze
PITCH: Players navigate a wireframe maze using only keyboard input and spatial memory to reach the exit, finding the path through sound cues and faint wall traces. It is fun because the challenge comes from feeling the maze with your hands and recalling its layout rather than reading it.
CONTROLS: Use arrow keys to move, Space to activate sound triggers.
OBJECTS:
- Maze Walls | box w=400 h=300 | wireframe cyan | act as faint obstacles that flash briefly when touched, marking the maze layout
- Exit Portal | box w=80 h=80 | wireframe gold | serves as the goal to reach to complete the level
- Sound Trigger | box w=50 h=50 | wireframe magenta | emits audible cues to help players locate walls and paths
- Ramp Link | box w=120 h=20 | wireframe green | connects the first floor to the second floor, adding a new challenge per level
- Score Counter | box w=150 h=40 | wireframe white | displays the current score and level progress
RULES:
- Players move with arrow keys, stepping one unit per 30-step interval.
- Touching a maze wall causes a brief flash and costs one life.
- Activating sound triggers adds points to the score.
- Each level reduces visible maze area and adds a second floor connected by a ramp.
- Reaching the exit portal completes the current level and advances to the next.
- Losing all lives ends the game.
WIN: Reach the exit portal in every level to complete the Sound Maze.
LOSE: Losing all lives before reaching the exit portal ends the game.
NUMBERS: speed=150, lives=3, score=0, level=1, maze_walls=4, floors=1
RISK: Programming the dynamic wall flash effects and second floor ramp transitions while relying on player memory for navigation without visual wall outlines.

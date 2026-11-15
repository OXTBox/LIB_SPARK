# Sleepwalker Guide
PITCH: Use arrow keys to guide a sleepwalker through a dark house, turning them around walls to lead them safely to bed. It is fun because you must read the house layout and act quickly to keep the sleepwalker from hitting dangerous areas.
CONTROLS: Arrow keys only.
OBJECTS:
- sleepwalker | box w=40 h=40 | wireframe cyan | walks straight ahead and turns right at walls
- wall | box w=900 h=600 | wireframe grey | blocks the sleepwalker and triggers a right turn
- bed | box w=120 h=80 | wireframe magenta | marks the safe destination for the sleepwalker
- stairs | box w=100 h=100 | wireframe red | costs one life if the sleepwalker enters it
RULES:
- The sleepwalker moves forward one step per arrow press.
- The sleepwalker turns right automatically when it hits a wall.
- The player scores 100 points for each successful turn of the sleepwalker.
- The sleepwalker loses one life when it enters the stairs.
- The sleepwalker reaches the bed to complete the level.
WIN: The sleepwalker reaches the bed without losing all lives.
LOSE: The sleepwalker enters the stairs and loses all lives.
NUMBERS: sleepwalker_speed=1, wall_speed=0, bed_speed=0, stairs_speed=0, score_start=0, lives_start=3
RISK: Programming the automatic right turn at walls while tracking the sleepwalker's path through the house layout.

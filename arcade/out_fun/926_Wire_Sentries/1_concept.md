# Wire Sentries

PITCH: A lone wire sentry guard patrols a dark maze, forcing a tiny player to dodge its straight-line sight while collecting data cores.

FUN:
- TOY: Moving with the arrow keys lets you slide smoothly through the open maze corridors. The screen shows your wireframe body as a bright moving line as you travel.
- CHOICE: You want to collect every data core for a high score, but moving too close to the sentry's path costs lives and sends you back to the last checkpoint pad.
- SURPRISE: Sentries change their patrol direction mid-loop, so your planned safe route suddenly becomes a direct line of sight.
- MOMENT: You slide past the sentry's path just as it turns, grab a data core, and the screen shows your bright wireframe line glowing as you collect it.
- EXTRA: You can pause the sentry's patrol with the arrow keys to reposition yourself safely before taking a core.

CONTROLS: Arrow keys move the player in the direction of the pressed key.

OBJECTS:
- player | box w=20 h=40 | colour=bright cyan | moves through the maze and collects data cores
- data core | box w=15 h=15 | colour=bright green | adds to the player's score when stepped on
- sentry | box w=30 h=30 | colour=dim red | walks fixed loops and sees straight along its row or column
- checkpoint pad | box w=40 h=40 | colour=dim yellow | resets the player to this position when caught

RULES:
- The player moves only with the arrow keys through the maze corridors.
- Sentries walk fixed loops and see straight along their current row or column.
- Stepping on a data core adds 10 to the player's score.
- Being seen by a sentry sends the player back to the last checkpoint pad.
- The third time a player is caught, the run ends.

WIN: Collect all data cores in the maze to complete the level.
LOSE: Being seen by a sentry three times ends the run.

NUMBERS:
- player speed=120 units per step
- sentry speed=80 units per step
- score start=0
- lives start=3
- steps per second=30

RISK: Programming the sentry's fixed patrol loops and detecting straight-line sight lines along rows and columns for the top-down maze.

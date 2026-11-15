# Guard Swap
PITCH: Use arrow keys to guide two heroes through a top-down castle maze while clearing guards with knockouts and glaze, and escape the castle by combining both tricks to open doors. It is fun because every step of the path requires a unique strategy, keeping the 1983 arcade challenge alive.
CONTROLS: Use arrow keys to move, Space to knock out guards or apply glaze.
OBJECTS:
- hero | box w=40 h=60 | colour=teal | moves through the castle maze to reach the exit
- guard | box w=50 h=50 | colour=orange | blocks the path and can be knocked out from behind
- glaze | box w=30 h=30 | colour=purple | talks guards into leaving doors open for 10 seconds
- door | box w=80 h=100 | colour=red | blocks passage until both tricks are used on it
RULES:
- Guards move slowly through the castle and turn around more often as levels progress.
- Arrow keys move the heroes forward through the maze toward the castle exit.
- Space knocks out a guard from behind for a short escape window.
- Space applies glaze to a guard, making them leave doors open for 10 seconds.
- Each successful escape adds 100 to the score.
- Losing a life occurs when a hero gets trapped by guards without using both tricks.
WIN: Both heroes reach the castle exit and complete the level.
LOSE: A hero loses all lives before both heroes reach the exit.
NUMBERS: hero_speed=2.5, guard_speed=1.2, glaze_duration=10, score_per_level=100, lives=3
RISK: Programming the dynamic guard turning logic and the synchronized door opening requirement for both heroes across multiple levels.

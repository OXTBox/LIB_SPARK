# Hover Polo
PITCH: Push the hover puck into the rival goal with your hover craft while the computer craft defends, using only arrow keys to bounce the puck off the walls. It is fun because you must time every move to score five goals before the rival closes its goal.
CONTROLS: Arrow keys to move the hover craft and direct the puck.
OBJECTS:
- hover craft | box w=120 h=60 | colour=teal | moves the player craft through the top-down field
- puck | box w=40 h=40 | colour=orange | bounces off walls and can be pushed into the rival goal
- rival craft | box w=120 h=60 | colour=red | defends the rival goal and moves faster each level
- rival goal | box w=80 h=80 | colour=purple | the target the puck must enter to score
- field walls | box w=900 h=600 | colour=black | the boundary that stops the puck from leaving the screen
RULES:
- The hover craft moves only with the arrow keys, with no other input required.
- The puck bounces off the field walls and follows the hover craft's direction.
- The puck enters the rival goal to score one point.
- First player to reach five points wins the level.
- The rival craft speeds up and the rival goal shrinks each level.
- A life is lost if the puck leaves the field walls or the player craft hits the rival craft.
WIN: The player reaches five points before the rival does to win the game.
LOSE: The player loses a life when the puck leaves the field or the player craft hits the rival craft, and losing all lives ends the game.
NUMBERS: puck speed=120 units per step, rival craft speed=90 units per step, level speed increase=10 units per level, goal width=80 units, score target=5, lives=3, field width=900, field height=600
RISK: Timing the puck's bounce and pushing it into the shrinking rival goal while the rival craft defends the goal is the hardest part to program.

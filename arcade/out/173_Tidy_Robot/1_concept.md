# Tidy Robot
PITCH: Walk around your kid's room with arrow keys to push toys into the toy box, and keep the cat from knocking toys away to keep your score high. It is fun because the simple movement makes tidying feel like a satisfying arcade challenge.
CONTROLS: Arrow keys move the player; pressing them walks the player into adjacent toys to push them toward the toy box.
OBJECTS:
- player | box w=40 h=40 | wireframe blue | moves through the room and pushes toys it touches
- toy | box w=30 h=30 | wireframe green | sits in the room and must be pushed into the toy box
- toy box | box w=80 h=60 | wireframe grey | collects pushed toys to increase the score
- cat | box w=35 h=35 | wireframe yellow | walks randomly around the room and knocks toys out now and then
RULES:
- The player moves only with arrow keys and cannot jump over toys.
- Each toy pushed into the toy box adds 10 to the score.
- The cat walks randomly around the room and knocks toys out if it touches them.
- Each life is lost when a toy is knocked out by the cat.
- The game ends after 3 lives are lost.
WIN: The score reaches 50 with all toys inside the toy box.
LOSE: The player loses all 3 lives when the cat knocks out toys.
NUMBERS: player_speed=120, toy_speed=60, cat_speed=40, score_start=0, lives_start=3, steps_per_second=30
RISK: Programming the cat's random walking path and its timing to knock toys out without interfering with the player's movement.

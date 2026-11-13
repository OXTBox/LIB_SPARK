# Long Worm
PITCH: The player guides a never-stopping worm through a grid by turning it with arrows, growing longer each time it eats food and risking its life when it hits walls or its own body. It is fun because every move builds the worm while keeping it alive on a simple, fast arcade grid.
CONTROLS: Use the arrow keys to turn the worm and Space to move it forward one cell at a time.
OBJECTS:
- worm | box w=10 h=5 | wireframe green | the moving entity that grows when it eats food
- food | box w=4 h=4 | wireframe orange | the item the worm eats to grow one cell longer
- wall | box w=900 h=600 | wireframe grey | the fixed grid boundary that costs a life when touched
- body | box w=10 h=5 | wireframe red | the worm's own trail that costs a life when touched
RULES:
- The worm moves one cell per step and never stops, only changing direction with arrow inputs.
- Eating food increases the worm's length by one cell.
- Each successful step adds 10 to the player's score.
- Hitting a wall or its own body costs one life and resets the worm to its starting position.
WIN: The player reaches the highest possible level by keeping the worm alive and growing it as long as possible.
LOSE: The player runs out of all lives after hitting a wall or its own body.
NUMBERS: worm_speed=1.5, food_speed=0.5, score_start=0, lives_start=3, level_start=1
RISK: Programming the collision detection between the moving worm and both the fixed wall boundary and the worm's own growing body trail accurately while keeping the movement smooth at 30 steps per second.

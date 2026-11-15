# Tabletop Racers
PITCH: You steer tiny toy cars across a giant kitchen table, dodging crumbs and pencils while racing rivals to the far edge. It is fun because every move feels like a real arcade race with tight, fast reactions and clear score goals.
CONTROLS: Use the arrow keys to steer and Space to accelerate.
OBJECTS:
- toy car | box 40,20 | cyan | moves with player input and follows the steering direction
- crumb | box 15,10 | yellow | acts as an obstacle that blocks the car path and costs time
- pencil | box 25,15 | orange | acts as a fast obstacle that blocks the car path and costs time
- rival | box 40,20 | magenta | moves automatically toward the finish line and pulls the player back if they lead too far
- juice spill | box 30,15 | red | acts as a hazard that costs time and can end a life if hit
RULES:
- Cars move forward one step per 30 steps per second.
- The player scores 10 points for every step completed toward the finish line.
- Crumbs and pencils reduce the player's time by 2 seconds each.
- Juice spills reduce the player's time by 5 seconds each.
- Falling off the table edge costs 1 life.
- Leading a rival by more than 100 units removes the rival from the round.
WIN: The player reaches the far edge of the kitchen table with all lives remaining.
LOSE: The player falls off the table edge and loses all remaining lives, ending the round.
NUMBERS: start_lives=3, start_time=60, start_score=0, screen_width=900, screen_height=600, step_speed=1
RISK: Programming the automatic rival movement and dynamic obstacle collision detection to match the arcade-style timing and scoring rules.

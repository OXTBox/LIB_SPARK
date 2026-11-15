# Patrol Swap
PITCH: Two players move through a prison yard maze while a searchlight follows the last mover, and you must swap their positions to reach the gate without letting the light catch the other hero. It is fun because the light creates constant pressure to plan your moves instead of rushing forward.
CONTROLS: Use the arrow keys to walk, and press TAB to swap the two heroes.
OBJECTS:
- Hero A | box w=40 h=40 | colour=blue | moves through the yard maze, can pick up keys and push switches
- Hero B | box w=40 h=40 | colour=green | moves through the yard maze, can pick up keys and push switches
- Searchlight | box w=120 h=60 | colour=orange | follows the hero who moved last, casting a light beam that blocks the other hero
- Prison Gate | box w=80 h=80 | colour=purple | the goal both heroes must reach to complete the level
RULES:
- Both heroes move one step per arrow press, and the searchlight shifts to follow the last mover after each step.
- The score increases by 10 points for every key a hero successfully picks up.
- A life is lost if the searchlight catches the hero that did not move, or if a hero falls into a wall.
WIN: Both heroes reach the prison gate at the same time to complete the level.
LOSE: A life is lost when the searchlight catches the other hero, or a hero falls into a wall; the game ends when all lives are lost.
NUMBERS: hero_speed=15, searchlight_speed=10, key_count=3, life_count=3, step_delay=30
RISK: Programming the searchlight to accurately follow the last mover while both heroes move independently through the maze without causing unfair collisions is the hardest part to implement.

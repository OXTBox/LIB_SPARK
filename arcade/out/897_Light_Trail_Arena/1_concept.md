# Light Trail Arena
PITCH: Navigate shrinking top-down grid arenas while dodging glowing walls, using speed boost pickups to survive longer rounds. It is fun because every movement is precise and each round raises the challenge with tighter space.
CONTROLS: Use arrow keys to move bikes, press Space to activate speed boost.
OBJECTS:
- Wall | box w=900,h=600 | colour=glowing cyan | acts as a solid barrier that ends the player's life if touched
- Speed Boost | box w=40,h=40 | colour=glowing yellow | grants a temporary speed increase for the next move
- Player Bike | box w=30,h=30 | colour=glowing white | the moving entity controlled by the player
RULES:
- Bikes move only in straight lines along grid axes until the player presses an arrow key to turn at right angles.
- The score increases by 10 points for every step the bike moves without hitting a wall.
- The arena shrinks by 10 world units each round, reducing safe movement space.
- Touching any wall costs one life and resets the bike to the starting position of the current round.
- Each speed boost pickup adds 20 points to the score and grants a temporary speed boost.
WIN: The player reaches the final arena size with a score above 500 points.
LOSE: The player runs out of all lives before reaching the final arena size.
NUMBERS: starting_lives=3, starting_score=0, arena_size=900, speed_boost_duration=5, steps_per_second=30
RISK: Programming the dynamic arena shrinking logic that adjusts wall boundaries and movement constraints each round while maintaining smooth player control.

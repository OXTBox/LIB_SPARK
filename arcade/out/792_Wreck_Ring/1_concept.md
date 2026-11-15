# Wreck Ring
PITCH: Pilot a wireframe car through ramps and a lava pit while collecting power-ups, and win the round by being the last car moving across the arena. It is fun because every move matters and the race rewards quick, precise driving.
CONTROLS: Use arrow keys to steer and Space to accelerate.
OBJECTS:
- rocket | box w=120 h=40 | cyan | increases car health by 20
- mine | box w=80 h=80 | orange | damages the car it touches by 30
- repair | box w=100 h=60 | green | restores car health by 50
RULES:
- Cars move automatically forward at a set speed, and the player steers with arrow keys.
- The last car still moving at the end of each round wins the round.
- Collecting power-ups adds score, and touching mines reduces car health.
- Each car has limited health, and losing all health costs one life.
- The game ends after three rounds, and the player with the most round wins wins the game.
WIN: You win the game by winning the best of three rounds.
LOSE: You lose the game if you run out of lives before completing all three rounds.
NUMBERS: cars=2, health=100, lives=3, score=0, speed=120
RISK: Programming the precise collision detection and continuous movement logic for the wireframe cars and power-up interactions.

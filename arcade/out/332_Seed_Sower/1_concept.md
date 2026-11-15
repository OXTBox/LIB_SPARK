# Seed Sower
PITCH: Walk along top-down field rows to sow seeds, then circle back later to avoid birds that eat fresh seeds, creating a fast-paced timing challenge.
CONTROLS: Arrow keys move the player along the rows; no other keys are used.
OBJECTS:
- Player | box w=20 h=20 | green | moves along field rows to sow seeds
- Seed | box w=10 h=10 | yellow | stays planted until birds eat it
- Bird | box w=15 h=15 | orange | follows the player and eats seeds sown recently
- Field Row | box w=900 h=40 | blue | contains planting positions for seeds
RULES:
- The player moves only along the field rows using arrow keys.
- Sowing a seed adds 10 to the score.
- Birds eat seeds sown within the last 3 seconds, costing 1 life.
- Each life allows 3 additional sowing attempts.
- The game ends when all lives are lost.
WIN: The score is the highest number of seeds successfully sown before losing all lives.
LOSE: All lives are lost after seeds are eaten by birds.
NUMBERS: player_speed=120, seed_speed=80, bird_speed=100, lives=3, score=0
RISK: Coordinating bird movement to accurately track the player and timing seed consumption within the last few seconds.

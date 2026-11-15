# Puddle Jumper
PITCH: You steer a small jumper along a rainy street, jumping over puddles and dodging car splashes to reach school dry. It is fun because every jump and dodge builds the score while keeping you as dry as possible.
CONTROLS: Left and right move the jumper sideways, up jumps the jumper over puddles.
OBJECTS:
- Puddle | box w=120 h=40 | colour=teal | moves horizontally across the street, blocking the jumper
- Car Splash | box w=100 h=60 | colour=orange | moves horizontally across the street, hitting the jumper when it overlaps
- School | box w=150 h=80 | colour=indigo | the final destination the jumper must reach
- Jumper | box w=40 h=60 | colour=green | the player character that moves with the controls
RULES:
- Puddles move left to right at a steady speed, blocking the path forward.
- Car splashes move left to right at a faster speed, hitting the jumper when they overlap.
- Each successful jump over a puddle adds 10 to the score.
- Each splash hit makes the jumper wetter by 1 point; reaching 3 wet points costs one life.
- The jumper starts with 3 lives and can only move left, right, or jump with the given keys.
WIN: Reach the school on the dry side of the street with at least 1 life remaining.
LOSE: Lose all 3 lives when the jumper gets hit by enough splashes to reach 3 wet points.
NUMBERS: jumper_speed=150, puddle_speed=200, splash_speed=300, score_start=0, lives_start=3, wet_start=0
RISK: Programming the precise collision detection between the jumper and moving puddles and splashes to prevent unfair hits while keeping the path navigable.

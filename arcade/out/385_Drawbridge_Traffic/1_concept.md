# Drawbridge Traffic
PITCH: Raise and lower the barrier to let cars pass through the canal barges, balancing timing to avoid collisions and score high. It is fun because the simple control creates constant tension with every crossing attempt.
CONTROLS: Use only the up arrow to raise the barrier and the down arrow to lower it.
OBJECTS:
- barrier | box 120,30 | wireframe cyan | raises and lowers to let cars pass through the canal
- car | box 60,30 | wireframe orange | moves along the canal between the barges
- barge | box 200,80 | wireframe blue | blocks the canal path when the barrier is lowered
- score | box 100,40 | wireframe green | displays the current score from successful crossings
- life | box 80,40 | wireframe red | tracks remaining attempts before the game ends
RULES:
- Cars move continuously along the canal between the barges.
- Raise the barrier to block cars, then lower it to let them pass.
- Each successful car crossing adds 10 to the score.
- Lowering the barrier into a car costs 1 life.
- The game ends after 3 lives are lost.
WIN: Score 100 or more by clearing all cars through the canal.
LOSE: 3 lives lost when lowering the barrier into a car.
NUMBERS: barrier_speed=5, car_speed=3, barge_speed=2, score_start=0, life_start=3
RISK: Precisely timing the barrier raise and lower to match car movement between the barges without accidentally colliding with cars.

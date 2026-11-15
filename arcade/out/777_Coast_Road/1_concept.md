# Coast Road
PITCH: Drive a convertible along a sunny coast road while dodging traffic, and choose your route at each fork to unlock a new path of five stages. It is fun because every run feels like a fresh coastal adventure with time bonuses and simple keyboard control.
CONTROLS: Use the arrow keys to steer and Space to accelerate.
OBJECTS:
- Traffic | box w=40 h=80 | colour=orange | moves along the road and must be dodged
- Truck | box w=80 h=120 | colour=red | travels slower than traffic and blocks the road
- Checkpoint | box w=60 h=60 | colour=green | grants a time bonus and restores one life
- Time Bonus | box w=50 h=50 | colour=blue | adds extra score when collected
- Road Fork | box w=100 h=40 | colour=purple | switches the road direction for the next stage
RULES:
- Traffic and trucks move forward along the road at fixed speeds.
- Accelerate with Space to increase your speed and score points per step.
- Collect checkpoints to gain time bonuses and protect your lives.
- Losing all lives costs the current stage and resets your progress.
- Each road fork offers a left or right route for the next stage.
WIN: Complete all five stages of your chosen route to finish the game.
LOSE: Lose all lives before completing all five stages of your route.
NUMBERS: speed=120, lives=3, stages=5, score=0, time_bonus=100
RISK: Programming the dynamic road fork logic that changes route direction based on player steering while maintaining smooth wireframe rendering of moving traffic and trucks.

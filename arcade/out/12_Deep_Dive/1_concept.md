# Deep Dive
PITCH: You pilot a diver through the dark sea, collecting pearls while dodging fish and keeping your air supply alive. The fast-moving water and limited air create a tense, endless underwater adventure.
CONTROLS: Use arrow keys to move the diver, press Space to refill air at the surface.
OBJECTS:
- diver | box w=40 h=40 | cyan | moves through the water collecting pearls
- pearl | box w=20 h=20 | gold | scores one point when touched by the diver
- fish | box w=60 h=30 | blue | crosses the screen and costs one life when touched
- air | box w=900 h=100 | white | refills when the diver reaches the surface
RULES:
- The diver moves in all four directions at a constant speed through the water.
- Collecting a pearl adds one point to the score.
- Fish cross the screen from side to side continuously.
- Running out of air costs one life.
- Touching a fish costs one life.
- Air is refilled automatically when the diver reaches the surface.
WIN: The player reaches the highest possible level with a full life remaining.
LOSE: The player runs out of all lives before reaching the final level.
NUMBERS: diver_speed=120, pearl_count=10, fish_speed=80, air_refill_steps=60, lives=3, score=0
RISK: Programming the continuous air refill timer and the synchronized movement of crossing fish across the screen without collisions.

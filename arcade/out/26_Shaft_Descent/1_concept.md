# Shaft Descent
PITCH: Run down a tall vertical shaft of platforms while dodging patrol drones, jump with a real arc to clear gaps, and reach the exit before the air runs out. It is fun because every step tests your timing and reflexes in a tight, focused vertical world.
CONTROLS: Use the arrow keys to move and Space to jump.
OBJECTS:
- Player | box w=20,h=40 | cyan wireframe | moves down the shaft and can jump with an arc curve
- Platform | box w=120,h=20 | orange wireframe | provides stable ground to run on and jump from
- Patrol Drone | box w=30,h=30 | red wireframe | moves back and forth along the shaft path, blocking the way
- Exit | box w=80,h=40 | green wireframe | marks the goal at the bottom of the shaft
RULES:
- The player descends the shaft at a steady world speed unless jumping, which applies a real upward arc curve.
- Jump height and distance depend on the jump arc, allowing players to clear platform gaps safely.
- Dropping through gaps lets the player move faster down the shaft to reach the exit quicker.
- Scoring increases by 10 points for each platform successfully passed.
- A life is lost if the player hits a patrol drone or falls out of the shaft.
- The air supply decreases each step, forcing the player to reach the exit before it runs out.
WIN: Reach the green exit at the bottom of the shaft before the air runs out.
LOSE: Hit a patrol drone, fall out of the shaft, or run out of air before reaching the exit.
NUMBERS: player_speed=120, platform_count=15, drone_count=4, air_steps=120, score_per_platform=10, lives=3
RISK: Implementing the real jump arc curve with consistent height and distance across all shaft platforms while balancing drop speed and air depletion timing.

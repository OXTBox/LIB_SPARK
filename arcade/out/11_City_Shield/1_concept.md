# City Shield
PITCH: You aim a cross at falling streaks and fire bursts to destroy them, protecting the city blocks until all streaks are cleared. It is fun because every shot directly fights the falling threat and your score grows with each successful strike.
CONTROLS: Use the arrow keys to move the aiming cross and press Space to fire bursts.
OBJECTS:
- aiming cross | box w=40 h=20 | colour=#4a90d9 | acts as the player's targeting and firing tool
- streak | box w=80 h=30 | colour=#d94a4a | falls from the top toward the city blocks and must be destroyed by bursts
- city block | box w=150 h=120 | colour=#4a70b9 | acts as the protected target that remains until all streaks are cleared
- burst | box w=100 h=100 | colour=#f0c04a | destroys any streak inside its area when fired
RULES:
- Streaks fall from the top of the screen toward the six city blocks at a steady speed.
- Each streak destroyed by a burst adds 100 to the player's score.
- The level ends when all streaks have run out of the screen.
- The game ends when every city block has been destroyed.
- The player loses a life each time a city block is hit by a falling streak.
WIN: The game is won when all streaks are cleared and no city blocks remain damaged.
LOSE: The game is lost when all lives are exhausted before clearing all streaks.
NUMBERS: streaks_start=10, city_blocks=6, lives_start=3, score_start=0, streak_speed=120, burst_speed=30
RISK: Programming the precise burst targeting and streak destruction logic to ensure accurate hits while maintaining the 1983 arcade wireframe visual style.

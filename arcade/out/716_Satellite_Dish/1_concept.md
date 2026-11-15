# Satellite Dish
PITCH: Aim your satellite dish with the arrow keys to track a slow satellite across the sky and keep the signal bar full while dodging clouds that block the signal. It is fun because you must constantly adjust your aim to match the moving target while keeping the signal strong.
CONTROLS: Use the arrow keys to aim the satellite dish in any direction needed to track the sky satellite.
OBJECTS:
- satellite dish | box w=200 h=100 | wireframe cyan | acts as the aiming tool for the player
- satellite | box w=150 h=150 | wireframe yellow | moves slowly across the sky and must be tracked
- signal bar | box w=300 h=20 | wireframe green | shows the strength of the received signal
- cloud | box w=250 h=150 | wireframe grey | blocks the signal and must be avoided
RULES:
- The satellite moves slowly across the sky in fixed steps.
- The signal bar fills as the dish tracks the satellite and drains when clouds block the signal.
- Score points for each successful full signal cycle.
- A cloud that blocks the signal for more than two steps costs one life.
- The dish cannot move, only aim, so there is no movement penalty.
WIN: The player keeps the signal bar full for five consecutive full cycles to win the level.
LOSE: A life is lost when a cloud blocks the signal for more than two steps, and the game ends when all lives are used.
NUMBERS: dish_aim_speed=1.0, satellite_speed=0.3, signal_bar_fill_rate=0.5, cloud_block_duration=2.0, lives=3, score_start=0
RISK: Tracking the slow satellite across the sky while managing the signal bar and avoiding moving clouds to keep the signal full is the hardest part to program.

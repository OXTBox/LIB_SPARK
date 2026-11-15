# Mole Holes
PITCH: Players navigate a top-down lawn to stand on holes while moles appear, sending them back down to score points. It is fun because the fast-paced timing challenge keeps the screen always busy with quick, satisfying actions.
CONTROLS: Use the arrow keys to move in the four directions of the lawn.
OBJECTS:
- Mole | box w=40 h=20 | colour #8B4513 | pops up from holes and moves across the lawn
- Hole | box w=60 h=60 | colour #2F4F2F | acts as a safe platform to stand on while moles are up
- Player | box w=30 h=30 | colour #FFFFFF | moves with the arrow keys and stays on holes to send moles down
- Score | box w=100 h=30 | colour #FFD700 | displays the current points earned from successful mole drops
- Life | box w=40 h=40 | colour #DC143C | tracks remaining attempts before the game ends
RULES:
- Moles pop up randomly from holes and move quickly across the lawn.
- Standing on a hole while a mole is up sends the mole back down and adds one point to the score.
- Holes you stand on for longer than two seconds get filled with dirt and become unsafe.
- Each life allows three successful mole drops before the game ends.
WIN: The player reaches the highest possible score by completing all safe mole drops.
LOSE: The player runs out of lives after failing to send moles down safely.
NUMBERS: player_speed=120, mole_speed=90, hole_fill_delay=60, max_lives=3, max_score=1000
RISK: Timing the precise moment to stand on a hole while a mole is visible and avoiding overstaying on holes to trigger filling is the hardest part to program.

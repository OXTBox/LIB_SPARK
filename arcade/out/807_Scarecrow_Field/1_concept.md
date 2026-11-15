# Scarecrow Field
PITCH: Walk through the top-down crop field with arrows to move scarecrows away from your crops, keeping the field safe from landing crows for a high score. It is fun because every step of the field matters and you must think ahead to protect your crops from the crows.
CONTROLS: Use the arrow keys to move one cell in the chosen direction; each arrow key moves the selected scarecrow one cell in that direction.
OBJECTS:
- Crop | box w=30 h=20 | green | acts as the protected field area that crows cannot land on
- Scarecrow | box w=25 h=25 | orange | blocks crows from landing on the cell it occupies
- Crow | box w=30 h=30 | grey | lands on an empty cell if no scarecrow can guard it
RULES:
- Crops stay fixed in their starting positions throughout the play session.
- Crows move one cell per step toward the center of the field.
- Scarecrows move one cell per arrow key press, blocking crows from landing on their cells.
- Score increases by 1 point for every crop the crows cannot reach.
- A life is lost if a crow lands on a crop without a scarecrow guarding it.
WIN: The score reaches the target score of 50.
LOSE: A life is lost when a crow lands on a crop without a scarecrow guarding it.
NUMBERS: crops=12, scarecrows=3, crows=2, score_target=50, lives=3, step_speed=1, field_width=900, field_height=600
RISK: Programming the logic to detect whether a cell is guarded by a scarecrow and preventing crows from landing on unguarded crops while moving multiple objects simultaneously.

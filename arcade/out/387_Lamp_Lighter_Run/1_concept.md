# Lamp Lighter Run
PITCH: Walk along a dark wire street at night, lighting every lamp before dawn to stop drifting shadow shapes from extinguishing them, and score points for each lamp you safely light. It is fun because the simple arrow controls create a steady, tense rhythm of chasing lights while shadows constantly threaten the street.
CONTROLS: Use only the arrow keys and Space.
OBJECTS:
- Lamp | box w=40 h=60 | colour=light grey | lights up the lamp to keep it lit during the level
- Shadow | box w=120 h=80 | colour=dark blue | drifts across the street and puts out lamps it touches
- Street | box w=900 h=600 | colour=black | the wire street where the player walks and shadows move
- Dawn | box w=900 h=10 | colour=light yellow | marks the end of the level when all lamps are lit
RULES:
- The player moves forward with the arrow keys at a steady walking speed.
- Each lamp lit successfully earns 100 points toward the level score.
- Shadows drift continuously across the street at varying speeds.
- Touching a shadow with the player costs 1 life and resets the player to the start of the street.
- All lamps must be lit before the Dawn appears to complete the level.
- Each level adds more shadows and extends the street length.
WIN: The player lights every lamp before Dawn appears to complete the level.
LOSE: The player runs out of all lives before lighting every lamp before Dawn appears.
NUMBERS: player_speed=120, lamp_count=5, shadow_count=3, score_per_lamp=100, lives=3, level_length=900, steps_per_second=30
RISK: Programming the dynamic interaction between the player's walking path and the unpredictable drifting shadow movements to ensure lamps are not accidentally extinguished by shadows while the player walks past them.

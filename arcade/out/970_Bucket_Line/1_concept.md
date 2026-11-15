# Bucket Line
PITCH: Carry water from the well to the burning house using only left and right movement, putting out one fire per trip while new fires keep spreading. It is fun because the simple movement creates a tight, satisfying loop of rescue and survival.
CONTROLS: Left and right arrow keys only.
OBJECTS:
- Water bucket | box w=40 h=20 | colour=light blue | carries water to put out fires
- Fire | box w=60 h=40 | colour=red | burns and spreads to nearby areas
- Well | box w=50 h=50 | colour=dark green | holds the water source for trips
- House | box w=120 h=80 | colour=orange | contains the main fire to extinguish
- Fire switch | box w=30 h=30 | colour=purple | starts new fires when activated
RULES:
- The player walks left or right to move between the well and the house.
- Each full trip from the well to the house puts out one fire.
- New fires start at the fire switch when the player walks into it.
- The score increases by 10 for every fire successfully put out.
- A life is lost if the player walks into a fire without carrying water.
WIN: The player puts out all fires in the house and stops new fires from starting.
LOSE: The player runs out of lives while fires spread across the screen.
NUMBERS: well=1, house=1, fire=3, score=0, lives=3, speed=120
RISK: Coordinating the spread of new fires with the player's movement and water transport to keep the game balanced without adding complex logic.

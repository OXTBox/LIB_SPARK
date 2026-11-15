# Pursuit Grid
PITCH: You move through a top-down grid while three hunters chase, block, or wander around you, and you collect all five keys to clear each level. It is fun because the hunters react to your every move, creating constant pressure and a fast, focused arcade flow.
CONTROLS: Use arrow keys to move one cell per step, and press Space to collect nearby keys.
OBJECTS:
- hunter | box w=1, h=1 | wireframe blue | moves one cell per player step, following its assigned habit
- key | box w=1, h=1 | wireframe gold | must be collected to complete the level
- player | box w=1, h=1 | wireframe green | moves one cell per step using arrow keys
RULES:
- The three hunters move one cell each time you move one cell, using their assigned habits.
- Collect all five keys to win the current level and advance to the next one.
- Each level increases one hunter's speed by two steps every fourth turn.
- Lose a life if any hunter reaches your cell.
- Score one point for each key collected before losing a life.
WIN: Collect all five keys to clear the level and reach the final level.
LOSE: Lose a life when any hunter reaches your cell, reducing your remaining lives.
NUMBERS: keys=5, lives=3, hunter_steps_per_turn=1, level_speed_increase=2, steps_per_second=30, screen_width=900, screen_height=600
RISK: Programming the three hunters' distinct movement habits and their speed increases every fourth turn while keeping them within the grid boundaries.

# Glass Bottle Shelf
PITCH: Move the basket left or right to catch rolling bottles before they crash the floor, building a high score with every successful catch. It is fun because the simple side-view action keeps the focus on precise timing and quick reflexes.
CONTROLS: Use only the left arrow key to move the basket left and the right arrow key to move the basket right.
OBJECTS:
- Basket | box 120,80 | cyan | moves left or right to catch rolling bottles
- Bottle | box 40,60 | magenta | rolls off the shelf and must be caught by the basket
- Shelf | box 900,200 | light blue | holds the bottles above the floor
- Floor | box 900,400 | dark grey | receives dropped bottles and cracks when they land
- Player | box 60,100 | white | remains stationary at the shelf edge
RULES:
- Bottles roll slowly off the shelf toward the floor every 30 steps.
- Catch one bottle to add 100 points to the score.
- Moving the basket into the floor area costs one life.
- The basket cannot move faster than 5 world units per step.
- The game ends after 3 lives are lost.
WIN: The score is the highest number of bottles caught before the game ends.
LOSE: The game ends when all 3 lives are lost.
NUMBERS: basket_speed=5, bottle_roll_speed=2, score_start=0, lives_start=3, steps_per_level=30
RISK: Precisely controlling the basket movement speed to match the rolling bottles' timing without overshooting the catch zone.

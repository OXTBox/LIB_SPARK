# Path Painter Duel
PITCH: Two heroes move through a top-down grid arena, colouring every cell they walk on to fill enclosed areas. The player wins by collecting the most colour before the clock ends, creating a fast-paced colour-collecting duel.
CONTROLS: Use the arrow keys to move, and Space to colour the current cell.
OBJECTS:
- PROMPT | box 900,600 | wireframe cyan | the player hero that moves and colours cells
- GLAZE | box 900,600 | wireframe magenta | the rival hero that moves and colours cells
- ARENA | box 900,600 | wireframe yellow | the fixed top-down grid arena with walls
- CLOCK | box 30,20 | wireframe orange | the timer that counts down the duel
- SCORE | box 40,20 | wireframe green | the score tracker showing colour collected
- LIVES | box 40,20 | wireframe red | the life counter that decreases on hits
RULES:
- Both heroes move one cell per arrow key press, only inside the arena bounds.
- Each hero colours the cell they stand on when Space is pressed.
- Enclosing an area with your colour fills the entire enclosed region.
- The score increases by one for every fully coloured cell.
- A life is lost if the hero touches a wall or the rival's coloured area.
- The clock counts down from the starting value each level.
- The level ends when the clock reaches zero.
WIN: The player collects the most colour points before the clock ends.
LOSE: The player loses a life on every wall or rival contact, and loses the level if lives reach zero.
NUMBERS: arena=900,600, prompt_speed=120, glaze_speed=150, clock_start=120, score_start=0, lives_start=3
RISK: Determining the correct enclosed area detection and automatic filling logic for the coloured grid cells.

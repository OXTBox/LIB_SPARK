# Wire Ferry
PITCH: Carry heavy crates across a wire-strewn river on a tipping ferry, balancing the load with left and right keys while racing against a clock. It is fun because every step of the crossing depends on precise weight control and quick reflexes.
CONTROLS: Use the left arrow key to move left and the right arrow key to move right, and press Space to carry crates.
OBJECTS:
- Ferry | box 400,120 | wireframe cyan | moves left or right with arrow keys and carries crates
- Crate | box 40,40 | wireframe orange | adds weight to the ferry, affecting balance
- Current | box 0,60 | wireframe blue | pushes the ferry to the right over time
- Clock | box 0,80 | wireframe red | counts down the time available for crossing
WIN: Complete all levels by carrying every crate across the river before the clock runs out.
LOSE: Lose all lives when the ferry tips from unbalanced crates or the clock reaches zero.
NUMBERS: ferry_speed=120, crate_weight=80, current_speed=40, clock_duration=180, lives=3, levels=5
RISK: Balancing the ferry's left and right weight dynamically while managing current push and clock pressure simultaneously is the hardest part to program.

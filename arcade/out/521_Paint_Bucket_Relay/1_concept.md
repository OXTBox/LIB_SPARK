# Paint Bucket Relay
PITCH: Two players race to complete their yard tasks by moving buckets and brushes through the top-down yard, using quick swaps to coordinate their work and earn points for every finished planks.
CONTROLS: Arrow keys move the hero and brush, TAB swaps the two heroes between their tasks.
OBJECTS:
- PROMPT | box w=400 h=20 | colour=green | fills the bucket for the hero at the tap
- GLAZE | box w=300 h=150 | colour=blue | paints the fence planks for the hero at the fence
- HERO_TAP | box w=30 h=30 | colour=orange | stands at the tap to fill buckets
- HERO_FENCE | box w=30 h=30 | colour=purple | stands at the fence to paint planks
- DRY_BRUSH | box w=50 h=20 | colour=white | returns to the fence to apply paint
RULES:
- The hero at the tap fills the bucket when the PROMPT is adjacent.
- The hero at the fence paints a plank when the GLAZE is adjacent.
- The DRY_BRUSH must return to the fence to complete the paint task.
- Each completed task adds 100 to the player's score.
- A dry brush that leaves the fence without completing a paint task costs 1 life.
WIN: The player reaches the highest possible score before the move limit ends.
LOSE: The player runs out of lives after a failed brush return or the move count reaches zero.
NUMBERS: hero_speed=120, brush_speed=90, move_limit=600, lives=3
RISK: Coordinating the two heroes and the dry brush to maintain the correct task order without timing errors.

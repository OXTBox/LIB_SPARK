# Night Garden
PITCH: Walk the dark hedge maze with arrow keys to collect every glowing flower while a gardener walks the paths, and stand in the gardener's lantern light to return to the gate. It is fun because the simple path-following challenge creates a tense, rewarding garden exploration experience.
CONTROLS: Arrow keys to move, Space to enter the gardener's light.
OBJECTS:
- hedge | box 900,600 | dark grey | blocks movement and forms the maze paths
- flower | box 30,30 | soft green | must be collected to score points
- gardener | box 40,60 | warm yellow | walks the paths and provides light
- lantern | box 50,50 | warm yellow | sends the player back to the gate when stood in
- gate | box 80,100 | bright white | the final exit point for the level
RULES:
- The gardener moves along the hedge paths automatically every 30 steps.
- Collecting each flower adds 10 points to the score.
- Moving into the gardener's lantern light returns you to the gate.
- Walking into a hedge wall or outside the maze costs one life.
- Each level adds more flowers and gardeners in dead ends.
- The score carries over between levels.
WIN: Collect all flowers in the current level to complete the level.
LOSE: Lose all lives to exit the game.
NUMBERS: gardener speed=1.5, flower count=12, life count=3, level count=3, score start=0
RISK: Programming the automatic gardener path-following logic while ensuring smooth player interaction with the lantern light zones.

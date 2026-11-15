# Tide Pool Hop
PITCH: The player hops from rocky shore to rocky shore, collecting shells before the rising tide covers the low rocks. It is fun because each hop is a quick, focused challenge that keeps the player focused on the moving shoreline.
CONTROLS: Arrow keys only.
OBJECTS:
- rocky shore | box w=900 h=600 | wireframe cyan | acts as the stable platform for hopping
- low rock | box w=120 h=40 | wireframe blue | acts as a hop target that gets covered by the tide
- shell | box w=30 h=30 | wireframe green | adds 100 to the player's score when collected
- tide | box w=900 h=60 | wireframe orange | rises over low rocks and covers them
- switch | box w=40 h=40 | wireframe yellow | triggers a tide retreat when pressed
RULES:
- The player moves by hopping from rock to rock using arrow keys.
- Each collected shell adds 100 points to the score.
- Low rocks become covered by the tide and cannot be hopped onto.
- Pressing the switch causes the tide to retreat, uncovering the low rocks.
- Covered low rocks cost one life.
WIN: Collect all shells before the tide fully covers the shore.
LOSE: Losing all lives ends the try.
NUMBERS: player_speed=120, shell_score=100, life_cost=1, tide_speed=40, step_count=30
RISK: Programming the dynamic tide movement that changes platform availability in real time while maintaining smooth hop mechanics.

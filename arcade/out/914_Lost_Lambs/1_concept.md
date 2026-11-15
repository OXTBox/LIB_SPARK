# Lost Lambs
PITCH: Walk through the hillside maze with arrow keys to guide the lambs into the fold, and keep them safe from the wandering wolf as you score points for each lamb safely led. It is fun because the simple arrow controls create a focused, tense top-down challenge that rewards careful movement and quick decisions.
CONTROLS: Use the arrow keys to move the player through the hillside maze; the lambs follow the player once they are adjacent to them.
OBJECTS:
- Player | box w=30 h=30 | wireframe blue | moves through the maze with arrow keys, triggering lambs to follow when adjacent
- Lamb | box w=20 h=20 | wireframe green | follows the player when adjacent, scores a point when safely brought into the fold
- Wolf | box w=40 h=40 | wireframe grey | walks along the hedges, moves away from the player to scare lambs when they come close
- Fold | box w=100 h=100 | wireframe yellow | the safe destination where lambs must be led to score points
RULES:
- The player moves only with the arrow keys through the hillside maze.
- Lambs follow the player automatically once the player walks next to them.
- Each lamb safely brought into the fold scores one point.
- The wolf walks along the hedges and moves away from the player to scare lambs when they come close.
- A lamb that is scared away by the wolf loses one life.
WIN: Lead all lambs into the fold to complete the level.
LOSE: A lamb is scared away by the wolf, ending the current try.
NUMBERS: player_speed=120, lamb_speed=80, wolf_speed=60, step_count=30
RISK: Coordinating the automatic lamb following behavior with the wolf's avoidance logic to ensure lambs stay safe while the player navigates the maze.

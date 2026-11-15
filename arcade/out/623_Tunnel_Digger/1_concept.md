# Tunnel Digger
PITCH: Walk into the earth with the arrow keys to dig tunnels, collecting gems while rocks above fall and crush the path. It is fun because every step deepens the challenge while the simple, direct digging action stays satisfying.
CONTROLS: Arrow keys to walk and dig; Space is not required for this game.
OBJECTS:
- gem | box w=40 h=40 | colour=gold wireframe | collects 100 points and is removed from play
- rock | box w=80 h=80 | colour=gray wireframe | falls after one step and blocks dug tunnels
- tunnel | box w=900 h=20 | colour=dark gray wireframe | created by digging and allows passage between levels
- switch | box w=30 h=30 | colour=blue wireframe | triggers rock fall when pressed
RULES:
- Players move forward by pressing arrow keys, digging earth as they walk into it.
- Rocks above dug cells fall after one step and block further passage.
- Collecting gems adds 100 points to the score.
- Each level is deeper, with more rocks and gems under the player.
- A life is lost when a rock falls on the player or the tunnel is blocked.
WIN: Collect all gems in the current level to complete the level.
LOSE: Lose all lives to end the game.
NUMBERS: base_speed=10, gem_count=5, rock_count=3, level_depth=20, score_per_gem=100, lives=3
RISK: Timing rock falls precisely so they fall onto the player or block the tunnel while maintaining smooth digging movement.

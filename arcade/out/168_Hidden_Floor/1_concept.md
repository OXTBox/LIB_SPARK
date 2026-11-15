# Hidden Floor
PITCH: Walk through a top-down room of plain tiles to uncover hidden holes, collect the clues they hide, and reach the exit before any hole sends you back to the start. It is fun because every step reveals a new secret while you race to unlock the final path.
CONTROLS: Arrow keys only.
OBJECTS:
- tile | box w=90 h=90 | wireframe grey | safe floor tile that shows the number of hidden holes next to it when stepped on
- hole | box w=40 h=40 | wireframe dark red | hidden unsafe tile that sends the player back to the start and reveals itself
- key | box w=30 h=30 | wireframe blue | pickup object that unlocks safe passages and opens the exit path
- switch | box w=50 h=50 | wireframe green | mechanism that opens the exit route after collecting required keys
- exit | box w=80 h=80 | wireframe bright green | final goal tile that completes the level once reached
RULES:
- Player moves only with arrow keys, one tile per step.
- Stepping on a safe tile reveals the number of hidden holes adjacent to it.
- Stepping on a hole resets the player to the start of the room and shows the hole's location.
- Collecting required keys unlocks safe passages and enables the exit route.
- The player scores points for each hidden hole successfully uncovered.
- A player loses a life if stepping on a hole after collecting all required keys.
WIN: Reach the exit tile after collecting all required keys and uncovering every hidden hole.
LOSE: Lose all lives by stepping on a hole after collecting all required keys, or fail to reach the exit before lives run out.
NUMBERS: player_lives=3, score=0, steps_per_second=30, screen_width=900, screen_height=600
RISK: Programming the hidden hole detection and dynamic tile state changes that reveal and reset player position based on tile interactions.

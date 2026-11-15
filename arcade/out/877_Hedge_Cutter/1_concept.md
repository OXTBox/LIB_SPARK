# Hedge Cutter
PITCH: Walk through an overgrown hedge maze with arrow keys to cut a path to the fountain, scoring fewer cuts than the required par to win. It is fun because every step shapes the garden and the challenge comes from managing the growing hedge.
CONTROLS: Use the arrow keys to move your player through the garden; no other keys are used.
OBJECTS:
- player | box w=20 h=20 | wireframe green | moves through the garden using arrow keys
- hedge | box w=120 h=120 | wireframe brown | grows back after being cut and blocks movement
- fountain | box w=40 h=40 | wireframe blue | the final destination of the path
- score | box w=100 h=30 | wireframe white | tracks the number of cuts made to reach the fountain
- par | box w=80 h=30 | wireframe grey | sets the required cut count for winning
RULES:
- The player moves one step per arrow key press through the open garden space.
- Each time the player walks into a hedge, it is cut and the cut count increases by one.
- The hedge grows back after a set delay, blocking the player again.
- The goal is to reach the fountain with a total cut count below the par value.
- Each failed attempt resets the cut count to zero and the hedge to its original state.
WIN: Reach the fountain with a total cut count below the par value.
LOSE: nothing: the score is moves against par.
NUMBERS: player_speed=1, hedge_growth_delay=45, par=8, cuts_per_step=1
RISK: Programming the dynamic hedge growth and cut-back logic to maintain consistent maze flow while tracking the player's path accurately.

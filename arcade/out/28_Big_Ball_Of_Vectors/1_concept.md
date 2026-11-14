# Big Ball Of Vectors
PITCH: Roll the crude security polyhedron across the open grid to catch fleeing rogue agents, growing stronger with every catch until you clear the level quota. It is fun because the ball evolves through each catch while entanglement hazards force you to stay precise.
CONTROLS: Use the arrow keys to roll the ball and Space to stop.
OBJECTS:
- security polyhedron | box 100,100 | wireframe cyan | the player's rolling ball that grows sides and size after each catch
- rogue agent | box 60,60 | wireframe magenta | a fleeing agent that runs away from the ball until it escapes the grid edge
- entanglement hazard | box 80,80 | wireframe orange | a drifting hazard that makes the ball go rogue and roll on its own if touched
- score counter | box 40,20 | wireframe yellow | displays the current score and level quota
- life indicator | box 40,20 | wireframe green | shows remaining lives before the player loses all progress
- level quota | box 40,20 | wireframe blue | shows the required catches to complete the current level
RULES:
- The security polyhedron rolls in straight lines when the player uses arrow keys, stopping on Space.
- Each successful catch with a rogue agent increases the ball's sides and size by one unit.
- Every rogue agent that escapes the grid edge adds one entanglement hazard to the map.
- Catching a rogue agent scores one point toward the level quota.
- Touching an entanglement hazard costs one life and makes the ball roll on its own for a moment.
- The ball starts with three sides and a small size, growing until the level quota is reached.
WIN: The player catches the required number of rogue agents to complete the level quota and reach the final level.
LOSE: The player loses all remaining lives when touching an entanglement hazard, or fails to catch the quota within the level time limit.
NUMBERS: ball_sides=3, ball_size=100, agent_speed=120, hazard_speed=80, score=0, lives=3, level_quota=10, step_speed=30, screen_width=900, screen_height=600
RISK: Programming the dynamic entanglement hazard drift and the ball's automatic rogue rolling behavior while maintaining smooth wireframe rendering on the vector engine.

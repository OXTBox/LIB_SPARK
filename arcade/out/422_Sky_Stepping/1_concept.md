# Sky Stepping
PITCH: Walk on floating slabs above clouds to reach the far tower, collecting steps that help you climb higher levels. It is fun because the challenge stays simple while the slabs drift and sink, keeping every move meaningful.
CONTROLS: Arrow keys only.
OBJECTS:
- floating slab | box 200,40 | wireframe blue | acts as a walkable platform that sinks slightly each step and drifts slowly
- cloud layer | box 900,300 | wireframe white | provides the background atmosphere above the walking area
- far tower | box 100,600 | wireframe grey | the final goal to reach at the end of each level
- step token | box 20,20 | wireframe yellow | scores points when collected during platform movement
RULES:
- Floating slabs sink a little each step and drift slowly across the screen.
- Each slab can support three steps before it sinks and disappears.
- Collecting step tokens adds to the player's score.
- Slabs that sink cost one life.
- Each level features slabs farther apart and more drifting slabs.
WIN: Reach the far tower at the end of the current level.
LOSE: Lose all lives when slabs sink and disappear.
NUMBERS: slab_sink_speed=1, step_token_score=100, life_cost=1, level_slab_distance=150, drift_speed=0.5
RISK: Managing the sinking and drifting mechanics of the floating slabs while keeping the walking experience smooth and consistent across levels.

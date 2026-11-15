# Domino Run
PITCH: Walk across the top-down floor with arrows to tip the first domino, letting the chain topple toward the bell for a high score. Straightening standing dominoes from the side creates safe gaps to reach the goal.
CONTROLS: Use the arrow keys to move forward, left, or right across the floor.
OBJECTS:
- Domino | box w=40 h=20 | wireframe blue | tips when walked into, starts the chain reaction toward the bell
- Bell | box w=50 h=50 | wireframe red | completes the chain, awards the score
- Standing Domino | box w=40 h=20 | wireframe green | straightens when walked into from the side, creating a safe path
- Floor | box w=900 h=600 | wireframe black | the top-down game surface where the player and dominoes move
RULES:
- The player moves only with the arrow keys across the floor.
- Tipping the first domino starts the chain reaction toward the bell.
- Walking into a standing domino from the side straightens it to create a safe gap.
- The score increases as the chain reaches the bell.
- Walking into a fallen domino costs one life.
WIN: Tip the chain to the bell and reach the goal for a high score.
LOSE: Falling into a fallen domino ends the try.
NUMBERS: player_speed=2.5, domino_tip_speed=1.0, bell_reach_speed=1.5, life_count=3
RISK: Programming the chain reaction logic to accurately transfer the toppling state from each domino to the next without breaking the wireframe rendering.

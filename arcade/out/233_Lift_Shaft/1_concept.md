# Lift Shaft
PITCH: Carry a person from their floor to the floor written above their head by riding lifts and walking open corridors, and climb higher floors to reach the top of the building. It is fun because every move helps you reach the final floor while the lifts move on their own and more people wait as you go higher.
CONTROLS: Use arrow keys to move, Space to ride lifts.
OBJECTS:
- Person | box w=30 h=50 | wireframe cyan | carries the player through floors and corridors
- Lift | box w=120 h=80 | wireframe magenta | moves up and down on its own along the shaft
- Floor | box w=900 h=40 | wireframe yellow | holds the person and provides walking space
- Corridor | box w=200 h=100 | wireframe blue | connects floors for walking between levels
- Score | box w=200 h=40 | wireframe green | shows the current score and lives
- Waiting Person | box w=30 h=50 | wireframe orange | waits at a floor until the player arrives
RULES:
- The player moves with arrow keys and rides lifts when pressing Space.
- Each floor reached adds 10 to the score.
- Lifts move automatically up and down on their own.
- Reaching the top floor wins the game.
- Losing all lives costs a life and resets the player to their starting floor.
- Waiting people must be carried to the top to avoid losing a life.
WIN: Reach the top floor of the building to complete the game.
LOSE: Lose all lives by failing to carry waiting people to the top floor.
NUMBERS: player_speed=150, lift_speed=80, floor_height=40, corridor_height=100, score_start=0, lives_start=3
RISK: Programming the automatic lift movement and dynamic floor skipping logic that adapts to each level's new layout.

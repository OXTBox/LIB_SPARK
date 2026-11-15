# Orbit Room
PITCH: You dodge bouncing sparks inside a slowly turning round room and step through the rare aligned gaps to reach the exit door. It is fun because the wall rhythm keeps you focused and the timing challenge builds with every level.
CONTROLS: Use the arrow keys to move and Space to step through the aligned gaps.
OBJECTS:
- Turning Wall | box w=900 h=600 | colour=orange wireframe | rotates slowly in place to create moving gaps
- Spark | box w=40 h=40 | colour=red wireframe | bounces off the walls and moves across the room
- Exit Door | box w=80 h=80 | colour=green wireframe | opens only when wall gaps align perfectly
- Player | box w=30 h=30 | colour=blue wireframe | moves within the room and steps through aligned gaps
RULES:
- The turning wall rotates continuously in place, creating shifting gaps in its surface.
- Sparks bounce off the walls and move across the room at a steady speed.
- Pressing Space steps through the exit door only when a gap aligns perfectly with the door.
- Each level adds one more rotating ring and more sparks to increase difficulty.
- Scoring increases by 10 points for each successful gap alignment.
- Losing a life occurs when a spark touches the player or the player steps through an unaligned gap.
WIN: The player reaches the exit door after completing all levels successfully.
LOSE: The player runs out of all lives before reaching the exit door.
NUMBERS: wall_rotation_speed=0.5, spark_speed=1.2, level_count=3, lives=3, score=0
RISK: Programming the precise timing alignment between the rotating wall gaps and the player's step action to ensure consistent gap openings across all levels.

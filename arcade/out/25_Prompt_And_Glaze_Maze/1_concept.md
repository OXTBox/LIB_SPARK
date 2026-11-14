# Prompt And Glaze Maze
PITCH: Players swap between two agents to collect every energy dot in a maze while dodging chasing enemies, using thrown polyhedra to charm or de-rezz them for a score boost.
CONTROLS: Use arrow keys to move and Space to throw the active agent's powerup. Press TAB to swap agents.
OBJECTS:
- energy dot | box w=20 h=20 | colour #00FFFF | collects full points and advances the level
- PROMPT | box w=40 h=40 | colour #FF0000 | de-rezzes enemies to remove them
- GLAZE | box w=40 h=40 | colour #00FF00 | charms enemies to follow as friends
- polyhedron | box w=60 h=60 | colour #FFFF00 | bounces around corners and loses sides per strike
RULES:
- Both agents move automatically along the maze path at fixed speeds.
- Energy dots award 100 points each and must all be collected to finish the level.
- The thrown polyhedron loses one side per enemy strike and disappears when fully broken.
- Enemies chase the active agent and cost one life when touched by the active agent.
- Switching agents with TAB pauses the active agent's movement for one step.
WIN: Collect all energy dots to complete the level and reach the final score goal.
LOSE: Lose all lives when enemies touch the active agent, ending the game.
NUMBERS: agent_speed=120, polyhedron_side_count=6, enemy_chase_speed=80, life_count=3, energy_dot_count=12
RISK: Programming the polyhedron's side-loss physics and enemy charm/de-rezz behavior to balance accurately in the maze.

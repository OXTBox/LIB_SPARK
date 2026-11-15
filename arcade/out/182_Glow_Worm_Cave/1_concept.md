# Glow Worm Cave
PITCH: The player explores a dark cave with arrow keys, following glowing worm light to find three crystals and return to the entrance. It is fun because the cave feels alive and the glowing worms guide the player safely through a hidden path.
CONTROLS: Arrow keys only.
OBJECTS:
- Glow Worm | box w=120 h=40 | colour=light green | lights up for a few seconds when passed to show the way back
- Crystal | box w=40 h=40 | colour=bright cyan | must be collected to complete the cave
- Entrance | box w=80 h=120 | colour=dim amber | marks the starting point and the required return location
RULES:
- Glow worms stay on the cave walls and light up for a few seconds after the player passes them.
- Collect all three crystals to unlock the path back to the entrance.
- Each step of movement costs one life if the player leaves the safe glowing path.
- Collecting a crystal adds 100 to the score.
- Returning to the entrance with all crystals clears the level.
WIN: The player collects all three crystals and returns to the entrance successfully.
LOSE: The player loses all lives when moving outside the glowing worm path.
NUMBERS: lives=3, score=0, crystals=3, steps_per_second=30, screen_width=900, screen_height=600
RISK: Programming the dynamic glow worm lighting and path-following logic to keep the player guided safely while maintaining the 1983 wireframe visual style.

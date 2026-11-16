# Ghost Light Mine
PITCH: A tiny miner with a flickering lantern must guide a drifting ghost through an old mine maze while its lantern burns down and oil flasks hide in dead ends.
FUN:
- TOY: Moving the lantern with the arrow keys makes the ghost drift smoothly through the tunnels, and the screen shows the ghost's fading wireframe copies trailing behind it.
- CHOICE: The player must choose between using a scarce oil flask to keep the lantern lit and saving it for a later dead end, or risking the lantern burning out and losing the ghost.
- SURPRISE: A ghost copy that has faded to almost nothing suddenly reappears in a tunnel the player has already passed, forcing a careful re-check of the path.
- MOMENT: A player sees the ghost's trailing copies fade into thin lines and the lantern still has oil, then presses the arrow keys to guide the ghost through the last tunnel and steps out of the mine.
- EXTRA: The player can move the lantern freely through the mine to explore dead ends and collect oil flasks before the lantern burns out.
CONTROLS: Arrow keys move the lantern and guide the ghost; no other keys are used.
OBJECTS:
- lantern | box w=120 h=80 | colour=amber wireframe | keeps the ghost from drifting away and burns down over time
- ghost | box w=40 h=60 | colour=white wireframe | drifts through the tunnels and follows the lantern
- oil flask | box w=40 h=40 | colour=green wireframe | refills the lantern's oil so it burns down slower
- iron bar gate | box w=100 h=120 | colour=silver wireframe | blocks the tunnel until the player finds and uses the key
- pickaxe | box w=60 h=40 | colour=gray wireframe | breaks the broken wall to open the tunnel
- dynamite | box w=80 h=60 | colour=orange wireframe | clears the cave-in to open the tunnel
RULES:
- The lantern moves with the arrow keys and its oil burns down one unit per step.
- The ghost drifts through the tunnels and follows the lantern's movement.
- Each level has one blockage that must be cleared with the correct tool found in a dead end.
- The player scores one point for each tunnel cleared successfully.
- Using an oil flask costs one life if the lantern burns out before the level is cleared.
WIN: The player clears the blockage, guide the ghost through the final tunnel, and reach the exit of the mine.
LOSE: The lantern burns out completely, or the player runs out of lives from using oil flasks.
NUMBERS: lantern_oil=100, ghost_trail_length=5, oil_flask_count=3, level_blocks=1, screen_width=900, screen_height=600, speed=30
RISK: Programming the fading ghost copies and the lantern oil burn-down mechanics while keeping the wireframe 1983 arcade look consistent.

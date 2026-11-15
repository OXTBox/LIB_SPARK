# Bridge Builder Room
PITCH: Push planks into chasms to build a safe bridge across the room, then reach the exit with your planks. It is fun because every bridge you build must fit exactly, and each level challenges you with wider gaps and fewer spare planks.
CONTROLS: Use the arrow keys to move, and press Space to push planks into the chasm.
OBJECTS:
- plank | box w=1, h=1 | wireframe cyan | acts as a bridge cell that stays in the chasm after being pushed
- chasm | box w=3, h=600 | wireframe red | a gap that must be bridged with planks to pass safely
- exit | box w=2, h=2 | wireframe green | the goal location to reach once the bridge is complete
- player | box w=1, h=1 | wireframe yellow | the moving player who pushes planks into the chasm
RULES:
- Planks stay in the chasm after being pushed and cannot be moved again.
- The score increases by 10 for every plank successfully placed in the chasm.
- A life is lost if the player steps into a chasm without a plank covering the gap.
- Each level introduces wider chasms and fewer spare planks to increase difficulty.
- The player must reach the exit with all planks used to complete the level.
WIN: The player reaches the exit with a fully bridged chasm using all available planks.
LOSE: The player steps into an uncovered chasm, losing a life and restarting the current level.
NUMBERS: player_speed=10, plank_speed=5, chasm_width=3, spare_planks=3, level_steps=30
RISK: Programming the precise bridge placement logic that ensures planks remain correctly positioned across varying chasm widths while tracking player safety across levels.

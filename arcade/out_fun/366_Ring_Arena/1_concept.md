# Ring Arena
PITCH: A tiny wireframe wanderer fights drifting drone waves in a circular arena, trying to clear each wave before the drones close in.
FUN:
- TOY: Pressing Space releases a fast shockwave that expands outward, and the screen shows the expanding wireframe ring as the wave travels.
- CHOICE: You must stay still to charge your shockwave, but moving keeps the wave faster and lets you dodge drones.
- SURPRISE: Drones drift in from the arena edge and their speed increases with every wave cleared.
- MOMENT: You hold still, the shockwave expands, and the last drone is swallowed by the wave, filling the screen with a burst of expanding wireframe rings.
- EXTRA: You can pause the arena to fully charge your shockwave before releasing it.
CONTROLS: Arrow keys move the player, Space releases the shockwave.
OBJECTS:
- player | box w=40 h=40 | wireframe cyan | moves through the arena and charges the shockwave when still
- shockwave | box w=100 h=100 | wireframe yellow | expands outward when released, clearing drones it touches
- drone | box w=30 h=30 | wireframe magenta | drifts in from the arena edge, moving faster as waves clear
RULES:
- Arrow keys move the player through the circular arena.
- Pressing Space releases the shockwave, which expands outward and clears any drones it touches.
- Staying still charges the shockwave; moving cancels the charge.
- Clearing a wave scores 100 points per wave cleared.
- Each wave has faster drifting drones; failing to clear a wave costs one life.
WIN: Clear all waves in the arena to win the game.
LOSE: Lose all lives when a wave cannot be cleared before the drones close in.
NUMBERS: player_speed=120, shockwave_speed=200, drone_speed=80, wave_count=5, score_per_wave=100, lives=3
RISK: Programming the dynamic shockwave expansion and the increasing drone speeds per wave to match the wireframe rendering smoothly.

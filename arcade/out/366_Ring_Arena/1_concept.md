# Ring Arena
PITCH: You control a stationary drone in a circular arena, charging shockwaves to clear incoming drones while dodging faster, shrinking safe zones. The tension comes from balancing stillness to charge and movement to survive each wave.
CONTROLS: Use arrow keys to move, Space to release shockwaves.
OBJECTS:
- Player Drone | box 120,40 | cyan | Charges shockwaves when stationary, releases them to clear drones inside the ring
- Shockwave | box 200,200 | magenta | Expands outward to destroy all drones within its radius
- Drone | box 40,40 | red | Spawns at the arena edge and drifts toward the player
- Safe Zone | box 450,450 | green | Defines the area where shockwaves can effectively destroy drones
RULES:
- Drones spawn at the arena edge and slowly drift toward the player.
- Stay stationary to charge the shockwave; moving cancels the charge.
- Each shockwave clears all drones inside its radius.
- Each wave increases drone speed and shrinks the safe zone.
- Score points for clearing drones without losing lives.
- Losing all lives ends the game.
WIN: The player clears all waves before lives reach zero.
LOSE: The player runs out of all lives while drones remain in the arena.
NUMBERS: player_charge=100, drone_speed=1.5, wave_speed_increase=0.2, safe_zone_shrink=10, lives=3, score=0
RISK: Balancing the stationary charge mechanic with dynamic drone movement and shrinking safe zones while maintaining the 1983 wireframe visual style.

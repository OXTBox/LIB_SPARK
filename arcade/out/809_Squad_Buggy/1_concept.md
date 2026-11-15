# Squad Buggy
PITCH: Pilot an armored buggy across open hills while three soldiers ride along, shooting enemies by themselves and guarding the squad to reach each flag. The mix of steering, squad combat, and guarding creates a fast, tense arcade experience.
CONTROLS: Use the arrow keys to steer the buggy and press Space to stop beside a soldier to pick him up.
OBJECTS:
- Buggy | box 900,600 | wireframe cyan | moves along the hills with arrow key input
- Soldier | box 40,80 | wireframe orange | rides the buggy, shoots nearest enemy, can be thrown off by bumps
- Mounted Gunner | box 60,100 | wireframe red | stands at the buggy’s mounted gun, shoots nearest enemy
- Flag | box 50,120 | wireframe green | marks the target location for the squad to reach
- Enemy | box 50,70 | wireframe purple | moves toward the buggy and is shot by soldiers and the gunner
RULES:
- The buggy moves forward with arrow keys and stops when Space is pressed.
- Soldiers and the gunner automatically target and shoot the nearest enemy in range.
- Bumps from enemy contact can throw a soldier off the buggy.
- Stop beside a fallen soldier to pick him up and restore his position on the buggy.
- Reaching a flag grants a score and requires the squad to hold it for 20 seconds.
- Losing all three soldiers costs one life.
- Each level increases enemy speed and bump frequency to raise difficulty.
WIN: Reach and hold all flags in the level to complete the game.
LOSE: Lose all three soldiers and fail the level.
NUMBERS: buggy_speed=120, soldier_shoot_range=400, soldier_shoot_cooldown=15, flag_hold_seconds=20, enemy_base_speed=60, life_start=3
RISK: Programming the automatic targeting and collision logic for soldiers, the mounted gunner, and bump interactions to keep the squad stable during driving.

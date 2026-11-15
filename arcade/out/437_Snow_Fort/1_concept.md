# Snow Fort
PITCH: Walk through the snowy yard to build a snow wall around your fort, blocking incoming snowballs before they break through the gaps. It is fun because you must balance quick building and defensive positioning to survive the snow volley.
CONTROLS: Use the arrow keys to move your character through the snowy yard; no other keys are used.
OBJECTS:
- player | box w=40 h=60 | wireframe blue | moves through the snowy yard to build the snow wall
- snow_pack | box w=120 h=80 | wireframe white | acts as walkable snow that the player walks into to gather material
- snow_wall | box w=300 h=120 | wireframe grey | forms the defensive wall around the fort to block incoming snowballs
- snowball | box w=40 h=40 | wireframe black | moves toward the fort and breaks through gaps in the snow wall
- fort | box w=80 h=80 | wireframe green | the player's safe base that snowballs must be blocked from reaching
RULES:
- The player moves only with the arrow keys through the snowy yard.
- The player gathers snow material by walking into snow packs.
- The player builds the snow wall around the fort to block incoming snowballs.
- Snowballs move toward the fort and break through any gaps in the snow wall.
- The score increases by 1 for every snowball successfully blocked by the snow wall.
- A life is lost when a snowball breaks through the snow wall and reaches the fort.
WIN: The player builds a complete snow wall around the fort and blocks all incoming snowballs.
LOSE: A life is lost when a snowball breaks through the snow wall and reaches the fort.
NUMBERS: player_speed=120, snow_pack_size=80, snow_wall_width=300, snowball_speed=90, fort_size=80, lives=3
RISK: Programming the dynamic snow wall building and precise snowball collision detection to maintain the defensive barrier around the fort.

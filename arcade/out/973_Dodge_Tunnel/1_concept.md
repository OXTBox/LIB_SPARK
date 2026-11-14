# Dodge Tunnel
PITCH: You control a wireframe cube moving through a dark tunnel while dodging fast cubes from the four corners, using smooth slide and climb moves to stay safe as the waves get faster. It is fun because every dodge feels responsive and the increasing speed creates constant challenge.
CONTROLS: Use the arrow keys to slide and climb, and press Space to jump.
OBJECTS:
- player cube | box 40,40 | cyan | the main character you control through the tunnel
- incoming cube | box 50,50 | red | fast cubes flying from the four tunnel corners
- tunnel wall | box 900,600 | black | the dark wireframe tunnel surrounding the play area
- score text | box 120,30 | white | displays your current score in the top corner
- life indicator | box 80,50 | orange | shows your remaining lives in the top right
RULES:
- Incoming cubes move from the four tunnel corners toward the center at increasing speed each wave.
- Pressing arrow keys moves the player cube up, down, left, or right to dodge the incoming cubes.
- Pressing Space makes the player cube jump higher to avoid low incoming cubes.
- Each successfully dodged cube adds 10 points to your score.
- Losing all lives costs 3 lives and resets the player to the tunnel center.
WIN: The game ends when you reach the highest wave level without losing all lives.
LOSE: You lose all lives and the game ends in failure.
NUMBERS: waves=5, player speed=2.5, incoming cube speed=1.8, score start=0, lives start=3, wave speed increment=0.2
RISK: Programming the dynamic speed scaling of incoming cubes while maintaining smooth player movement and collision detection for all four tunnel corners.

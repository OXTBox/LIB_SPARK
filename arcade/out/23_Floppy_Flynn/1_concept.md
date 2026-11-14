# Floppy Flynn
PITCH: You pilot a two-legged blue ship through destructible terrain by tapping to lift it, using its flapping legs to stay airborne while breaking the ground to fly higher. The score grows with every distance covered, and crashing only tears parts off the ship or breaks terrain instead of ending the game.
CONTROLS: Use arrow keys to move the ship and Space to lift the legs.
OBJECTS:
- Floppy Flynn ship | box 120,40 | blue | The player-controlled two-legged ship that flaps legs to stay up.
- Left leg | box 20,30 | blue | Flaps upward when Space is pressed to help the ship stay airborne.
- Right leg | box 20,30 | blue | Flaps upward when Space is pressed to help the ship stay airborne.
- Terrain block | box 400,100 | green | Destructible ground that breaks when the ship flies through it, creating gaps for flight.
- Score counter | box 100,30 | white | Displays the current distance score in world units.
- Life indicator | box 80,50 | red | Shows the remaining player lives.
RULES:
- The ship falls under gravity unless the legs are lifted with Space.
- Each successful gap traversal adds distance to the score.
- A crash tears one loose part off the ship or breaks the terrain.
- The ship loses a life when it falls below the screen and too few parts remain to fly.
- The game ends when all lives are lost.
WIN: The player reaches the highest possible distance score while keeping the ship flying.
LOSE: All player lives are lost when the ship plummets with too few remaining parts.
NUMBERS: ship_parts=3, lives=3, score_start=0, terrain_blocks=5, speed=120
RISK: Balancing the leg-flap physics and terrain destruction so the ship stays controllable while maintaining enough flight capability when parts are torn off.

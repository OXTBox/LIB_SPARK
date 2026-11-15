# Leaf Pile
PITCH: Walk through the autumn yard with arrows to push leaves forward, then gather them into one large pile at the marked spot while wind scatters loose leaves. It is fun because you must balance steady pushing and wind control to build the perfect pile.
CONTROLS: Use the arrow keys to move through the yard; the up arrow pushes leaves ahead of you.
OBJECTS:
- leaf | box w=80 h=20 | wireframe green | moves forward when pushed by the player
- wind | box w=120 h=40 | wireframe yellow | scatters loose leaves across the yard
- pile | box w=300 h=150 | wireframe brown | the target area to collect leaves into
- player | box w=40 h=40 | wireframe orange | moves through the yard with arrow keys
RULES:
- Leaves move forward automatically when the player walks over them.
- The player pushes leaves ahead of them by moving forward with the arrow keys.
- Wind scatters loose leaves randomly across the yard at a steady speed.
- Collecting leaves into the pile increases the score by 1 per leaf.
- Losing a life occurs when the player steps on a scattered leaf.
WIN: The player builds a pile of at least 100 leaves at the marked spot to win the level.
LOSE: The player loses a life when stepping on a scattered leaf; three lives end the game.
NUMBERS: player_speed=120, wind_speed=60, pile_target=100, lives=3, steps_per_second=30
RISK: Balancing the wind scattering speed against the player's pushing speed to ensure leaves collect into the pile without being scattered away.

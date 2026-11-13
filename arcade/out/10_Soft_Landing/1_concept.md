# Soft Landing
PITCH: The player guides a falling lander through the air using thrust and engine shots, landing softly on a flat pad to score points and survive. It is fun because the slow, precise control of the lander creates a tense, satisfying challenge against gravity and fuel limits.
CONTROLS: Use arrow keys to tilt the lander, Space to fire the main engine.
OBJECTS:
- Lander | box w=120 h=60 | wireframe cyan | the falling craft the player controls
- Ground Pad | box w=800 h=40 | wireframe green | the flat surface the lander must land on
- Fuel Tank | box w=40 h=80 | wireframe orange | consumes fuel when the main engine is fired
- Score Display | box w=200 h=60 | wireframe yellow | shows the current score and lives
RULES:
- The lander falls slowly under gravity at a steady rate each step.
- Tilting with arrow keys moves the lander sideways without changing vertical speed.
- Firing the main engine with Space burns fuel and provides a small upward thrust.
- Landing on the flat pad slowly enough scores points equal to the landing speed.
- Missing the ground pad by more than a small margin costs one life.
- Fuel runs out after a fixed number of engine shots, forcing careful movement.
- Each level increases the required landing speed, making the challenge harder.
WIN: The player lands on the flat pad at the required slow speed to complete the level.
LOSE: The player runs out of fuel or loses all lives before landing successfully on the pad.
NUMBERS: lander_fall_speed=2.0, fuel_max=10, score_start=0, lives_start=3, level_speed=1.0
RISK: Precisely controlling the lander's vertical speed to land slowly enough on the ground while managing limited fuel is the hardest part to program.

# Rock Field
PITCH: The player steers a ship through drifting rocks and splits them with shots to score points and survive the field. It is fun because every move changes the rock field and builds a growing score in a simple arcade style.
CONTROLS: Use the arrow keys to steer the ship and Space to fire.
OBJECTS:
- ship | box w=120 h=60 | wireframe cyan | moves with arrow keys and fires on Space
- big rock | box w=300 h=300 | wireframe amber | drifts across the screen and can be split by shots
- small rock | box w=120 h=120 | wireframe orange | drifts slowly and adds points when reached
- rock fragment | box w=80 h=80 | wireframe yellow | drifts after a big rock is split and can be collected
RULES:
- Big rocks drift slowly across the screen from one edge to the other.
- Firing a shot splits a big rock into two small rock fragments.
- Small rocks add 10 points each when the player reaches them.
- The ship loses one life if it hits a big rock or a small rock.
- Objects leaving one edge of the screen reappear on the opposite edge.
WIN: The player reaches a target score of 500 points to win the game.
LOSE: The player runs out of lives and the game ends in failure.
NUMBERS: ship_speed=150, big_rock_speed=80, small_rock_speed=40, fragment_speed=20, start_lives=3, target_score=500
RISK: Splitting big rocks into multiple drifting fragments with proper collision and movement logic across the screen.

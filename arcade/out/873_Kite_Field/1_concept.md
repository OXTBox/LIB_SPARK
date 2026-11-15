# Kite Field
PITCH: Walk the windy field with your kite line to pull it through glowing hoops, while dodging birds that cross the sky for a fast, simple arcade score.
CONTROLS: Left and right to walk, up and down to pull the line.
OBJECTS:
- Kite | box w=100 h=40 | wireframe cyan | pulls the player line upward and keeps the kite aloft
- Player | box w=20 h=60 | wireframe orange | moves along the field with left and right keys
- Hoop | box w=80 h=80 | wireframe yellow | scores a point when the kite passes through it
- Bird | box w=60 h=40 | wireframe green | crosses the sky and costs a life if hit
RULES:
- The kite rises and falls with the up and down keys, staying in the air to reach hoops.
- Pressing left or right moves the player through the field without changing the kite height.
- Each hoop passed by the kite adds one point to the score.
- Hitting a bird costs one life and removes the bird from the sky.
- The player loses the game after three lives are lost.
WIN: The player reaches the final field section with the kite through all hoops and three lives remaining.
LOSE: The player loses all three lives while dodging birds across the sky.
NUMBERS: player_speed=120, kite_speed=80, hoop_speed=40, bird_speed=60, lives=3, score=0, steps_per_second=30
RISK: Keeping the kite height balanced while the player walks and pulls the line through moving hoops without missing any without losing lives.

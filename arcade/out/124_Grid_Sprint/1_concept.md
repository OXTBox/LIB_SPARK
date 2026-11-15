# Grid Sprint
PITCH: You pilot a wireframe car around curving roads toward a horizon, setting your start place with a timed qualifying lap before racing seven rivals. The fast high gear and slow recovery after crashes make every speed choice a tense challenge.
CONTROLS: Use arrow keys to steer and Shift to switch between low and high gear, press Space to start the race.
OBJECTS:
- Car | box w=120 h=60 | wireframe cyan | moves along the curving road and responds to gear shifts and steering input
- Road | box w=900 h=400 | wireframe amber | defines the track path the car follows and where roadside signs appear
- Sign | box w=40 h=60 | wireframe red | causes the car to spin out when hit, resetting the checkpoint timer
- Checkpoint | box w=60 h=60 | wireframe green | restores the checkpoint timer when the car reaches it during the race
- Rival | box w=80 h=80 | wireframe orange | races alongside the player, affecting the player's start place and race outcome
- Score | box w=200 h=60 | wireframe white | displays the player's current score and remaining lives during the game
RULES:
- The car moves forward along the curving road at a speed determined by the active gear.
- The qualifying lap sets the player's start place in the race against the seven rivals.
- The race ends when the player finishes the timed race lap or hits a roadside sign.
- The score increases by 10 points for every full lap completed during the race.
- The checkpoint timer decreases over time and resets to full when the car reaches a checkpoint.
- Hitting a roadside sign costs one life and resets the car to the last checkpoint position.
- The race is won by finishing the race lap ahead of all rivals, lost by running out of lives.
WIN: The player finishes the race lap ahead of all seven rivals with at least one life remaining.
LOSE: The player runs out of all lives after hitting roadside signs or fails to finish the race lap ahead of the rivals.
NUMBERS: start_lives=3, qualifying_lap_steps=600, race_lap_steps=600, low_gear_speed=120, high_gear_speed=240, checkpoint_timer=300, score_per_lap=10
RISK: Programming the smooth gear shift mechanics and the checkpoint timer recovery logic while keeping the wireframe rendering consistent with the 1983 arcade visual style.

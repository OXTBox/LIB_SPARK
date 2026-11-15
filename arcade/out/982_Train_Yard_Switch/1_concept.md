# Train Yard Switch
PITCH: Steer trains along top-down rail tracks to match their colours with the siding they must enter, keeping every train safe before the next one arrives. It is fun because each switch decision challenges your timing while rewarding quick, precise steering.
CONTROLS: Arrows only. Walking onto a switch flips it to guide the train into the correct siding.
OBJECTS:
- Main Track | box 900,100 | wireframe grey | carries the train forward when no switch is active
- Switch | box 60,40 | wireframe blue | flips to direct the train into the matching siding
- Siding | box 120,80 | wireframe green | holds the train once its colour matches the siding
- Train | box 80,80 | wireframe red | moves along the track and must reach its matching siding
- Station Platform | box 300,100 | wireframe yellow | acts as a safe stopping zone for the train
RULES:
- Trains move forward automatically along the active track until they reach a switch or siding.
- Steering the train into the siding of its colour scores 100 points per correct match.
- Two trains occupy the same track at once cost one life.
- The try ends when a train falls off the edge of the screen or two trains collide on the same track.
WIN: The player clears all trains from the yard with a full score.
LOSE: Two trains occupy the same track, or a train falls off the screen edge.
NUMBERS: track_speed=120, switch_delay=30, siding_width=120, train_speed=90, lives=3, score_start=0
RISK: Keeping multiple trains on separate tracks with precise timing while managing switch states without missing a collision is the hardest part to program.

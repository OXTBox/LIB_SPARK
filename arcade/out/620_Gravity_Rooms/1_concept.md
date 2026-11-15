# Gravity Rooms
PITCH: Flip gravity to move through square rooms, collect keys to unlock doors, and reach the exit before spikes strike. It is fun because gravity changes let you explore every corner of each room with simple, direct controls.
CONTROLS: Left, right, and Up keys to flip gravity; walking into objects picks them up, pushes them, and activates switches.
OBJECTS:
- key | box w=10 h=10 | wireframe blue | unlocks the room door when picked up
- door | box w=40 h=60 | wireframe green | opens when its key is collected, allowing passage to the next room
- floor | box w=900 h=50 | wireframe grey | contains spikes that end a try when touched
- ceiling | box w=900 h=50 | wireframe grey | contains spikes that end a try when touched
- switch | box w=20 h=20 | wireframe yellow | activates when a key is pushed into it
RULES:
- Gravity flips every step the Up key is pressed, changing which surface you fall toward.
- Collecting a key adds it to your score.
- Picking up a key pushes it in the current movement direction.
- Touching any spike on the floor or ceiling ends the current try.
- Each room has one door that opens after collecting its key.
- The score increases by 10 for every key collected.
WIN: Reach the door of the final room to complete the game.
LOSE: Touching any spike on the floor or ceiling ends the current try.
NUMBERS: keys=3, doors=5, switches=5, lives=3, score=0, speed=120
RISK: Flipping gravity mid-movement while navigating tight room boundaries and managing key push directions to avoid spikes.

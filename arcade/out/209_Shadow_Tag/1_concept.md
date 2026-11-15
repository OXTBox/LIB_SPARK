# Shadow Tag
PITCH: The player navigates a dark courtyard, dodging the moving light beam while collecting coins, and the challenge comes from timing the light's shadow shifts to avoid being tagged.
It is fun because the fast-moving light creates constant pressure, and each level increases the light's speed for a growing challenge.
CONTROLS: Arrow keys to move through the courtyard, collect coins, and avoid the light beam.
OBJECTS:
- light beam | box w=400 h=20 | colour=blue | moves in a circular path across the courtyard, casting shadows that touch the player when outside pillars
- player | box w=30 h=60 | colour=green | moves with arrow keys, gets tagged when the light beam touches them outside a pillar shadow
- pillar | box w=120 h=120 | colour=grey | blocks the light beam, casting a shadow that protects the player when they are inside
- coin | box w=20 h=20 | colour=gold | adds to the player's score when collected
- switch | box w=40 h=40 | colour=orange | opens a path to new coin locations, required to progress through levels
RULES:
- The light beam circles the courtyard in a fixed pattern, moving faster each level.
- Collecting coins increases the player's score by 10 points each.
- The player loses a life when the light beam touches them outside a pillar shadow.
- The player must collect all coins in a level to advance to the next level.
- Each level increases the light beam's speed by 10 world units per step.
WIN: The player collects all coins in the final level and reaches the exit gate.
LOSE: The player runs out of lives before collecting all coins in the final level.
NUMBERS: light beam speed=100, coin count=5, lives=3, level count=3
RISK: The precise timing of the light beam's circular path and shadow shifts to avoid being tagged while moving through the courtyard.

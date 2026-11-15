# Recycling Robot
PITCH: The player guides a Recycling Robot through a busy street, collecting litter and sorting it into the correct bins to earn points while avoiding trash that hurts the robot. It is fun because every step of the street feels like a quick, satisfying arcade challenge.
CONTROLS: Arrows only.
OBJECTS:
- Recycling Robot | box 40,80 | wireframe cyan | moves with arrow keys to collect litter and place it in bins
- Litter | box 30,30 | wireframe orange | picked up by the robot and carried up to three at a time
- Bin | box 60,60 | wireframe green | accepts the correct litter type when the robot walks into it
- Wind | box 100,40 | wireframe yellow | blows new litter into the street at regular intervals
RULES:
- The Recycling Robot moves only with the arrow keys and carries up to three litter items.
- Collecting litter and placing it in the matching bin increases the score by 10 points each time.
- Walking into wrong litter types or dropping litter in the wrong bin costs one life.
- Wind continuously adds new litter to the street, keeping the street busy and challenging.
- The game ends a try when the robot loses all lives.
WIN: The score reaches the target score to complete the street level.
LOSE: The Recycling Robot loses all lives.
NUMBERS: robot_speed=120, litter_speed=80, wind_interval=45, score_target=500
RISK: Sorting litter into the correct bins by matching types while managing the limited carry capacity of the Recycling Robot.

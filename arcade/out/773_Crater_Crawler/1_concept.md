# Crater Crawler
PITCH: Pilot a six-wheel moon rover across a lettered crater course, dodging boulders and shooting saucers that drop deadly bombs to clear the path. It is fun because every jump and shot feels like a precise arcade challenge on the moon.
CONTROLS: Use the arrow keys to move and Space to jump or shoot.
OBJECTS:
- rover | box w=120 h=60 | wireframe cyan | moves forward automatically and responds to arrow key input
- boulder | box w=80 h=80 | wireframe orange | blocks the rover path and must be jumped over
- saucer | box w=60 h=60 | wireframe magenta | drops bombs that create new craters and cost lives
- crater | box w=100 h=100 | wireframe grey | creates a hazard zone that the rover must avoid
- bomb | box w=40 h=40 | wireframe red | damages the rover and costs a life when it hits the rover
RULES:
- The rover moves forward automatically at a steady speed through the lettered course sections.
- The player scores points for each crater cleared and each boulder jumped over.
- The rover loses a life whenever a bomb or crater hazard touches it.
- Each lettered checkpoint section has a required time to complete to advance to the next letter.
- The rover cannot move backward or stop; only forward movement and jumps are allowed.
- Shooting saucers is optional but helps clear hazards and speed up scoring.
WIN: The rover reaches the final lettered checkpoint Z with all required section times completed.
LOSE: The rover runs out of lives before reaching the final checkpoint Z.
NUMBERS: rover_speed=120, boulder_speed=0, saucer_speed=80, crater_speed=0, score_start=0, lives_start=3, checkpoint_time=30
RISK: Programming the dynamic bomb and crater generation system that reacts to saucer actions and updates the hazard zones in real time.

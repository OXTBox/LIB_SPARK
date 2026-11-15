# Courier Run
PITCH: You carry parcels through narrow city alleys while dodging chasing dogs, racing against a shrinking clock to reach the next numbered door. It is fun because the fast maze navigation and constant chase create a tense, focused arcade experience.
CONTROLS: Use arrow keys to move through alleys and press Space to carry parcels.
OBJECTS:
- parcel | box w=120 h=80 | colour=teal | carries the current parcel from the depot to the numbered door
- depot | box w=100 h=100 | colour=blue | the starting point for all parcels
- numbered door | box w=60 h=60 | colour=orange | the target location for the current parcel, marked with the next address number
- dog | box w=80 h=80 | colour=red | chases the player through alleys and must be avoided to prevent losing a life
RULES:
- Parcels move automatically from the depot toward the numbered door when the player is in the correct alley.
- The player scores points for each parcel successfully delivered to the numbered door.
- Dogs move continuously toward the player at increasing speed each level.
- Each dog contact costs one life.
- The clock shrinks by one second each level, ending the level if it reaches zero.
WIN: The player delivers all parcels in the current level before the clock ends.
LOSE: The player runs out of lives or the level clock reaches zero.
NUMBERS: parcels=3, dogs=2, clock=60, score=0, lives=3, level=1
RISK: Programming the dynamic dog chase behavior that adjusts speed based on the player's position and level progression while maintaining smooth maze navigation.

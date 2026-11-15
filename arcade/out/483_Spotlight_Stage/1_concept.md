# Spotlight Stage
PITCH: Stand in the lit spots of the theatre stage to collect the light, while avoiding the other actors, and score points for every perfect cue you complete. It is fun because it feels like a quick, focused arcade challenge with simple, clear movement.
CONTROLS: Use the arrow keys to move in the four directions of the stage.
OBJECTS:
- Spotlight | box w=120 h=60 | colour=gold | acts as the lit area the player must stand in during its cue
- Actor | box w=80 h=80 | colour=red | blocks the player and must not be bumped
- Stage Floor | box w=900 h=600 | colour=black | provides the top-down movement surface for the player
RULES:
- The player moves only with the arrow keys across the stage floor.
- Each spotlight lights up for a short cue, then goes dark.
- The player must stand inside a lit spotlight during its cue to score points.
- Bumping any other actor during a spotlight cue costs one life.
- The game ends when all spotlight cues are completed or the player runs out of lives.
WIN: The score is the number of completed spotlight cues.
LOSE: The player runs out of lives after bumping an actor during a spotlight cue.
NUMBERS: player_speed=150, spotlight_cue_length=30, life_count=3
RISK: Keeping the spotlight lighting timers and actor collision detection accurate for the 1983 wireframe arcade look.

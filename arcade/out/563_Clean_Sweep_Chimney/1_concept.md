# Clean Sweep Chimney
PITCH: Climb a narrow chimney by brushing soot from each ledge while smoke puffs push you upward, scoring clean sweeps for every tidy ledge you clear. It is fun because the simple up-and-down movement creates a steady, focused climb through a dark, wireframe vertical world.
CONTROLS: Use only the up arrow key to move upward and the down arrow key to move downward.
OBJECTS:
- Chimney Ledge | box w=120 h=40 | wireframe grey | acts as a step the player brushes to score clean sweeps
- Soot Puff | box w=60 h=30 | wireframe dark brown | pushes the player upward when it reaches the player's position
- Player | box w=40 h=60 | wireframe light blue | moves up or down with the arrow keys and collects clean sweeps
- Chimney Wall | box w=900 h=600 | wireframe dark grey | forms the fixed vertical structure of the chimney space
RULES:
- The player moves only upward or downward with the arrow keys, staying inside the chimney walls.
- Each time the player brushes a clean soot-covered ledge, a clean sweep score increases by 1.
- Soot puffs spawn from the bottom of the chimney and push the player upward one step per puff.
- A player loses a life if a soot puff catches the player and pushes them out of the chimney.
- The game ends when the player has collected a score equal to the target clean sweeps required for the level.
WIN: The player reaches the target clean sweep score and safely reaches the top of the chimney.
LOSE: A player loses a life when a soot puff catches them and pushes them out of the chimney.
NUMBERS: player_speed=2.5, soot_puff_spawn_rate=1, target_clean_sweeps=10
RISK: Programming the soot puff movement to reliably push the player upward without accidentally pushing them out of the chimney while keeping the up-and-down movement smooth.

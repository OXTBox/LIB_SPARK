# Tower Shift
PITCH: Climb a shifting tower of square rooms by following moving stairs to the top before the tower rotates and traps you. It is fun because the constant movement keeps your reactions sharp and every level adds more floors to chase.
CONTROLS: Use the arrow keys to move and Space to activate stairs.
OBJECTS:
- Tower | box 900,600 | wireframe cyan | the rotating stack of square rooms that traps the player when it turns
- Stairs | box 60,120 | wireframe magenta | the moving path to climb through to reach the top room
- Player | box 40,40 | wireframe yellow | the single player who navigates the tower by following stairs
- Doors | box 80,100 | wireframe orange | the walls that shift to new positions with each tower rotation
RULES:
- The tower rotates a quarter every 20 seconds, moving doors to new walls in each room.
- Climb by using the stairs to reach the top room before the next rotation traps you.
- Score 100 points for each room you successfully reach.
- Lose a life if the tower rotation traps you in a room with no exit.
- Each level adds one floor to the tower and increases rotation speed.
WIN: Reach the top room of the final level before the tower traps you.
LOSE: Lose all lives when the tower rotation traps you with no path to the top room.
NUMBERS: tower_floors=3, rotation_speed=1.5, score_per_room=100, lives=3, steps_per_second=30
RISK: Programming the dynamic door repositioning logic that adapts to tower rotations and level floor increases without trapping the player.

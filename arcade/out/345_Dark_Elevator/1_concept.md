# Dark Elevator
PITCH: Ride the dark elevator up a tall building, matching the blinking floor light to reach the top before the light fades out. It is fun because every step feels like a tense, quiet arcade climb with clear, simple movement.
CONTROLS: Up and down keys only.
OBJECTS:
- elevator shaft | box 900,300 | wireframe cyan | moves the player up or down between floors
- floor light | box 100,10 | wireframe yellow | blinks to signal the target floor
- floor switch | box 50,20 | wireframe orange | opens the lift when pressed
- building wall | box 900,600 | wireframe dark grey | blocks movement past the building edges
RULES:
- The player moves only up or down the elevator shaft.
- Reaching the floor with the blinking light scores 100 points per floor.
- Moving past the target floor wastes 5 seconds of game time.
- The light goes out after 30 seconds of inactivity.
- The player loses a life if the light goes out before reaching the target floor.
WIN: The player reaches the floor with the blinking light before it goes out.
LOSE: The player fails to reach the target floor before the light goes out.
NUMBERS: player_speed=15, floor_light_blink_rate=2, target_floor=10, game_time=30, lives=3
RISK: Keeping the blinking floor light active and synchronized with the player's movement while managing time costs accurately across all elevator positions.

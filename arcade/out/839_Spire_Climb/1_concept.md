# Spire Climb
PITCH: The player navigates a tall wire tower using arrow keys, stepping into alcoves to let rolling balls pass, reaching the top before the clock runs out. It is fun because the fast, ever-changing climb creates constant challenge and clear progress toward the summit.
CONTROLS: Use the arrow keys to move and Space to trigger actions.
OBJECTS:
- Spiral Ramp | box 900x600 | wire cyan | the path the player climbs around the tower
- Rolling Ball | box 40x40 | wire orange | moves down the ramp and must be stepped over
- Alcove | box 120x80 | wire magenta | a safe space to pause and let balls pass
- Clock | box 100x60 | wire yellow | counts down the time remaining for the level
- Player | box 30x30 | wire green | the character moving along the ramp
RULES:
- The player moves only along the spiral ramp using arrow keys.
- Rolling balls descend the ramp at increasing speed each level.
- Stepping into an alcove lets rolling balls pass safely.
- The score increases by 10 points for each ball safely passed.
- Losing one life occurs when the clock reaches zero or the player falls off the ramp.
- Each level raises the ramp height and ball speed, making the climb harder.
WIN: Reach the top of the tower before the clock runs out.
LOSE: The clock reaches zero or the player falls off the spiral ramp.
NUMBERS: ramp_height=50, ball_speed=2.5, clock_duration=180, lives=3, score=0
RISK: Programming the dynamic spiral ramp geometry and real-time ball collision detection with the player's movement along the arc.

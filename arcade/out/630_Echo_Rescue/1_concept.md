# Echo Rescue
PITCH: Players navigate a dark wire maze, ping walls along the shortest path to survivors, and guide them back to the start pad to rescue them. It is fun because the fast, precise pinging and the growing challenge of maze levels create a tense, focused arcade experience.
CONTROLS: Use arrow keys to move, press Space to ping walls.
OBJECTS:
- Survivor | box w=40 h=60 | colour=teal | calls out in the dark so players can locate them
- Wall | box w=900 h=600 | colour=blue | blocks movement and defines the maze path
- Start Pad | box w=120 h=120 | colour=green | acts as the final destination for rescued survivors
- Sentry | box w=30 h=30 | colour=orange | roams the maze and sends survivors home if touched
- Ping Effect | box w=100 h=100 | colour=purple | flashes walls along the shortest path to a survivor for one second
RULES:
- Players move with arrow keys through the wire maze walls.
- Press Space to ping walls along the shortest path to the nearest survivor.
- Touching a survivor guides them back to the start pad for a score.
- Survivors call out for one step before moving toward the player.
- Fewer pings and more sentries increase each level's difficulty.
- Sentries send survivors home when touched, costing a life.
- Each level adds more survivors to increase rescue challenge.
WIN: The player rescues all survivors in the current level to complete the level.
LOSE: The player loses a life when a sentry touches a survivor, or when lives reach zero.
NUMBERS: survivors=3, pings=5, sentries=2, player_speed=120, sentry_speed=80, survivor_speed=60, start_pad_x=450, start_pad_y=300
RISK: Programming the real-time shortest-path wall flashing and dynamic sentry survival tracking in the xTalk script for the 1983 wireframe arcade look.

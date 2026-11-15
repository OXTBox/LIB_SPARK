# Wire Sentries
PITCH: Navigate a top-down maze while dodging sentry patrols to reach hidden data cores, using quick keyboard moves to stay unseen and score points before sentries catch you. It is fun because the constant chase for safety creates a tense, focused arcade experience with clear goals and escalating challenges.
CONTROLS: Use arrow keys to move through the maze and Space to activate core collection.
OBJECTS:
- Sentry | box w=40 h=20 | colour=blue | walks fixed loops and sees in straight lines down corridors
- Data Core | box w=30 h=30 | colour=green | awards points when reached safely
- Checkpoint Pad | box w=50 h=50 | colour=purple | resets your position to the last safe spot when seen
- Maze Wall | box w=900 h=600 | colour=black | defines the fixed top-down play area
RULES:
- Sentries move along fixed loops at a steady speed.
- Collecting a Data Core adds 100 to your score.
- Moving into a straight line of sight from a sentry costs one life.
- Being seen by a sentry sends you back to the last checkpoint pad.
- Each level adds more sentries and longer sight lines.
- Reach all data cores in a level to unlock the next level.
- Losing all lives ends the game.
WIN: The player reaches all data cores in the final level without losing all lives.
LOSE: The player loses all lives while trying to reach data cores.
NUMBERS: sentry_speed=1.5, core_count=3, lives=3, score=0, level=1
RISK: Programming sentry sight-line detection and accurate positional tracking for the top-down maze without missing or over-detecting line of sight.

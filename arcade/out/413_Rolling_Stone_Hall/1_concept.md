# Rolling Stone Hall
PITCH: Walk the long hall with arrow keys while stone balls roll toward you, using safe alcoves and timed doors to clear each level for a score. It is fun because the fast-moving stones create constant pressure and every step of the path tests your timing and planning.
CONTROLS: Arrow keys only.
OBJECTS:
- Stone Ball | box w=40, h=40 | wireframe grey | rolls toward the player and blocks movement
- Side Alcove | box w=120, h=60 | wireframe light blue | acts as a safe zone where stones stop rolling
- Hall Door | box w=80, h=100 | wireframe dark green | opens only when no stone is rolling
- Player | box w=30, h=50 | wireframe white | moves through the hall and interacts with stones and doors
RULES:
- Stone balls roll continuously toward the player at a fixed speed.
- Collecting a stone ball increases the score by 100 points.
- Entering a stone ball or a rolling stone costs one life.
- Doors at the far end open only when no stone is currently rolling.
- Each level increases the number of rolling stone balls.
WIN: Clear the final level with all stones collected and the far-end doors opened.
LOSE: Lose all lives before clearing the final level.
NUMBERS: stones=3, lives=3, score=0, ball_speed=120, alcove_count=2, door_count=1, level_length=900
RISK: Timing the far-end doors to open only when no stone is rolling while managing the rolling stones' positions in real time.

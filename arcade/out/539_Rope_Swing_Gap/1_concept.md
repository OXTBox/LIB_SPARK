# Rope Swing Gap
PITCH: The player swings across a dark cave using ropes to cross dangerous gaps, feeling the natural rhythm of each swing to reach the next ledge. It is fun because every move feels controlled and the challenge comes from timing your release perfectly to land safely.
CONTROLS: Left, Right, and Up keys to grab ropes and swing.
OBJECTS:
- rope | box w=20 h=40 | colour=teal | grabs the player and initiates a swing
- ledge | box w=120 h=20 | colour=slate | provides a stable landing surface for the player
- pit | box w=300 h=100 | colour=black | an empty gap that costs a life if the player misses a ledge
- key | box w=10 h=10 | colour=orange | required to unlock the next swing path
RULES:
- The player moves left, right, or grabs a rope with Up to start a swing.
- Each successful swing to the next ledge adds 100 to the score.
- Missing a ledge drops the player back to the last safe ledge and costs 1 life.
- The game ends when all required keys are collected and the final ledge is reached.
WIN: The player reaches the final ledge with all keys collected to complete the game.
LOSE: The player runs out of lives and cannot reach the final ledge.
NUMBERS: score=0, lives=3, swingSpeed=120, ledgeSpacing=400
RISK: Timing the exact moment to let go of a rope to land safely on the next ledge without overshooting the gap.

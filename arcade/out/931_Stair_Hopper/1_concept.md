# Stair Hopper
PITCH: Climb a rising tower through water gaps while dodging drifting blue ledges to score points and survive the rising tide. It is fun because every step tests your timing and reflexes against a fast-moving, ever-higher challenge.
CONTROLS: Use arrow keys to move up and down, Space to jump over gaps.
OBJECTS:
- floor | box w=900 h=10 | colour=teal | provides stable ground to climb on
- ceiling | box w=900 h=10 | colour=teal | forms the upper boundary of each floor
- gap | box w=120 h=80 | colour=white | allows safe passage between floors
- floating_ledge | box w=80 h=40 | colour=blue | drifts sideways to avoid
- rising_water | box w=900 h=600 | colour=blue | rises upward to reach the player
RULES:
- Player moves up and down with arrow keys, jumps over gaps with Space.
- Score 10 points for each successful gap jump completed.
- Water reaching the player costs one life.
- Floating ledges drift sideways at increasing speed each level.
- Each level raises the water speed and adds more drifting ledges.
- Player loses all lives when water reaches the bottom of the tower.
WIN: Win the game by reaching the top floor of the tower before the water reaches the bottom.
LOSE: Lose the game when all lives are lost to the rising water reaching the player.
NUMBERS: starting_lives=3, base_water_speed=2, base_ledge_speed=1, level_count=5, score_per_jump=10
RISK: Programming the dynamic drift and rising speed adjustments for floating ledges and water across multiple increasing levels while keeping the wireframe rendering consistent.

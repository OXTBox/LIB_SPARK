# Cross Traffic
PITCH: The player hops upward through horizontal lanes of moving traffic, dodging fast vehicles to reach the top of the screen and score points. It is fun because the constant challenge of timing each lane hop against unpredictable traffic creates a fast, focused arcade experience.
CONTROLS: Use the arrow keys to move up and Space to hop between lanes.
OBJECTS:
- Lane | box w=900 h=20 | colour=light blue | defines the horizontal path the player hops through
- Vehicle | box w=80 h=40 | colour=orange | moves left or right at varying speeds within the lane
- Player | box w=30 h=50 | colour=green | hops upward one lane at a time from the bottom to the top of the screen
- Score | box w=120 h=30 | colour=white | displays the current points earned by reaching the top of the screen
- Life | box w=40 h=40 | colour=red | tracks remaining lives lost when hitting moving traffic
OBJECTS: 5
RULES:
- Lanes are fixed horizontal bands across the screen, each containing moving vehicles.
- The player moves upward one lane at a time using the arrow keys.
- Pressing Space triggers a hop to the next higher lane.
- Reaching the top of the screen scores one point.
- Hitting a moving vehicle costs one life.
- Vehicles move left or right at speeds that change between lanes.
- The game ends when all lives are lost.
WIN: The player reaches the top of the screen with at least one life remaining to score a final high score.
LOSE: The player loses all lives while dodging traffic in the lanes.
NUMBERS: player_speed=1, vehicle_speed_left=2, vehicle_speed_right=3, score_start=0, life_start=3, lane_count=5
RISK: Programming the dynamic lane transitions and variable vehicle movement speeds to ensure smooth player hops and consistent dodging challenges without causing collisions is the hardest part to program.

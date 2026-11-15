# Echo Chamber
PITCH: The player navigates a dark round chamber, turning and walking to collect glowing targets before they disappear, creating a fast-paced, focused arcade challenge. It is fun because every step brings immediate visual rewards and tight time pressure that keep the gameplay engaging.
CONTROLS: Use left and right arrow keys to turn, up arrow to walk.
OBJECTS:
- target | box w=120 h=60 | colour=light cyan | lights up one after another around the wall; face it within two seconds to score
- wall | box w=900 h=600 | colour=dark grey | forms the fixed round chamber boundary for all movement
- player | box w=40 h=60 | colour=light yellow | moves through the chamber based on arrow key inputs
- score | box w=150 h=40 | colour=white | displays the current accumulated score
- life | box w=100 h=40 | colour=light red | tracks remaining lives for the player
- ring | box w=900 h=300 | colour=light blue | forms the second ring of targets above the main wall
RULES:
- The player turns left or right with the left and right arrow keys, and walks up with the up arrow.
- Targets light up sequentially around the wall and above in the second ring.
- Face each target within two seconds to score one point.
- Each level adds more targets, shortens the time limit, and adds the second ring of targets.
- Losing all lives costs the player a life and resets progress to the current level.
- The time limit runs out when the player fails to collect all targets in the level.
WIN: The player collects all targets in the level before the time limit expires to complete the level.
LOSE: The player runs out of lives or fails to collect all targets within the time limit.
NUMBERS: player_speed=120, target_life=1.5, level_time=30, target_count=5, lives=3, score_start=0
RISK: Programming the sequential target lighting and timed collection mechanics around the round chamber wall while managing the increasing level constraints and time limits.

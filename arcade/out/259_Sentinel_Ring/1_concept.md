# Sentinel Ring
PITCH: Player circles the arena edge to collect ring pickups while dodging a slow sentinel, creating a tense wireframe arcade challenge. It is fun because every move matters and the screen stays focused on fast-paced dodging and collection.
CONTROLS: Left and right arrow keys to circle the arena edge.
OBJECTS:
- sentinel | box w=120,h=120 | colour #4a6b8a | turns to face the player and fires slow pulses
- pickup | box w=40,h=40 | colour #7ec8e3 | can be collected by walking into it
- ring | box w=900,h=600 | colour #2a3a4a | defines the arena boundary for circling
RULES:
- The player moves left or right to circle the arena edge continuously.
- Collecting a pickup adds 100 to the score.
- The sentinel fires pulses that cost 1 life if the player is hit.
- The game ends when the player loses all lives.
WIN: The player collects all ring pickups and stays alive to complete the level.
LOSE: The player loses all lives while dodging the sentinel's pulses.
NUMBERS: score_start=0, lives_start=3, pickup_count=5, sentinel_speed=1.5, pickup_speed=0.8
RISK: Programming the sentinel's dynamic facing and pulse targeting to stay consistent with the player's circling movement.

# Rope Bridge Builder
PITCH: The player builds a safe rope bridge by moving planks between the pile and the ravine, keeping the hero standing on every plank without falling. It is fun because every step counts and each successful connection tightens the bridge toward a safe crossing.
CONTROLS: Arrow keys move the hero left or right; TAB swaps the hero between the planer and the carrier.
OBJECTS:
- hero | box w=10 h=20 | wireframe blue | the player who moves planks and stands on the bridge
- planer | box w=15 h=10 | wireframe green | the hero who carries planks from the pile
- carrier | box w=15 h=10 | wireframe orange | the hero who ties planks onto the bridge
- plank | box w=80 h=10 | wireframe yellow | a movable bridge piece that must be tied to support the hero
- pile | box w=60 h=30 | wireframe grey | the storage area for untied planks
- rope | box w=100 h=5 | wireframe red | the connection that holds planks together on the bridge
RULES:
- The hero moves only with the arrow keys and swaps roles with TAB.
- The planer carries one plank at a time from the pile to the bridge.
- The carrier ties one plank onto the bridge with the rope.
- The hero falls back if standing on an untied plank.
- Each successful tie adds 10 to the score.
- Each fall costs 1 life.
- The try ends when the player has 0 lives or the move count reaches 30.
WIN: The player ties enough planks to build a fully supported bridge and reach the far side safely.
LOSE: The player falls off the bridge, runs out of lives, or exhausts the move count.
NUMBERS: hero_speed=150, planer_speed=120, carrier_speed=120, plank_speed=80, rope_speed=60, lives=3, move_count=30
RISK: Keeping the hero standing on every untied plank while coordinating the planer and carrier movements without losing balance is the hardest part to program.

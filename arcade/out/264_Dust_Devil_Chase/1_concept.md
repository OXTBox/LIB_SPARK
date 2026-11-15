# Dust Devil Chase
PITCH: The player chases small whirlwinds through a desert top-down map, collecting stolen gems to stop the whirlwinds from escaping the screen. It is fun because the fast, unpredictable chase keeps your focus sharp and every gem earned feels rewarding.
CONTROLS: Arrow keys only.
OBJECTS:
- Whirlwind | box w=120 h=60 | colour #8B7355 | wanders slowly, picks up gems it touches, and moves toward the map edge when unattended.
- Gem | box w=40 h=40 | colour #FFD700 | is stolen by a whirlwind, can be collected by the player, and restores one life when returned.
- Desert | box w=900 h=600 | colour #D2B48C | forms the top-down map area where the player and whirlwinds move, with edges that end the chase.
- Switch | box w=60 h=60 | colour #CD853F | stops nearby whirlwinds from moving toward the map edge, allowing the player to safely collect gems.
RULES:
- Whirlwinds wander slowly through the desert and pick up gems they touch.
- The player moves with arrow keys to chase whirlwinds and collect stolen gems.
- Collecting a gem adds one to the score.
- Whirlwinds that reach the map edge cost one life.
- The player has three lives at the start.
WIN: The player collects all stolen gems before any whirlwind reaches the map edge.
LOSE: A whirlwind reaches the map edge, ending the current try.
NUMBERS: lives=3, score=0, whirlwind_speed=1.5, gem_value=100, switch_delay=2
RISK: Programming the dynamic whirlwind pathfinding and edge-detection logic to keep whirlwinds wandering unpredictably while respecting the map boundaries.

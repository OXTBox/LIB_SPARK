# Sock Sorter
PITCH: Walk through the top-down laundry room with arrows to collect socks and place each one on its matching pair on the line, creating a simple and satisfying sorting challenge. It is fun because the goal is clear and every step brings you closer to a clean, organized laundry space.
CONTROLS: Use the arrow keys to move through the laundry room; pressing an arrow moves you one step in that direction.
OBJECTS:
- Sock | box w=80 h=40 | wireframe cyan | a collectible item that can be carried or placed on the matching line
- Matching Sock | box w=80 h=40 | wireframe magenta | the target item that must be paired with the carried sock on the line
- Laundry Line | box w=900 h=20 | wireframe yellow | the fixed path where paired socks must be placed
- Player | box w=20 h=60 | wireframe white | the moving figure that walks through the room to collect socks
RULES:
- Socks are picked up by walking into them and can be carried at most two at a time.
- Each correctly placed matching pair on the laundry line increases the score by 10 points.
- Carrying an unmatched sock onto the line costs one life.
- The game ends after 3 lives are lost.
WIN: The score reaches 100 points by placing all required matching pairs on the line.
LOSE: The game ends after 3 lives are lost.
NUMBERS: player_speed=120, sock_speed=0, matching_sock_speed=0, laundry_line_speed=0, lives=3, score=0, max_carried=2
RISK: Programming the matching logic to correctly identify paired socks and enforce the carrying limit without breaking the top-down movement system.

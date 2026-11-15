# Neon Drift Wastes
PITCH: The player controls a hover car sliding through three neon lanes, collecting data cassettes to score while dodging static walls and falling chrome pillars in a vaporwave wasteland. It is fun because the slow, glitchy drive feels relaxed and the colorful neon environment keeps every drive engaging.
CONTROLS: Use the arrow keys to move between lanes and press Space to jump.
OBJECTS:
- data cassette | box w=60, h=40 | teal | adds 100 points to the score
- static wall | box w=120, h=40 | pink | costs 1 life if touched
- chrome pillar | box w=40, h=120 | purple | costs 1 life if touched
- chill pickup | box w=80, h=80 | cyan | slows the game speed temporarily
RULES:
- The hover car moves automatically forward through the three lanes at a slowly increasing speed.
- Collect data cassettes to increase the player's score as the car travels.
- Static walls and falling chrome pillars move toward the player and cost one life when touched.
- The chill pickup reduces the current game speed for a short period.
- The game continues until the player runs out of lives.
WIN: The player continues driving indefinitely without losing all lives.
LOSE: The player loses all lives and the game ends.
NUMBERS: speed=1.2, score=0, lives=3, lanes=3, steps_per_second=30
RISK: Programming the smooth lane transitions and dynamic falling chrome pillar movement while maintaining the relaxed vaporwave visual style.

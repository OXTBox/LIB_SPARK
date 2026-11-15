# Bounce Rally
PITCH: You drive a small car along a scrolling top-down road, using jumps and side bumps to collect points and crush enemies. The fast, unpredictable bumping action creates a fast-paced, exciting arcade experience.
CONTROLS: Use the arrow keys to move and Space to jump.
OBJECTS:
- player car | box w=40 h=80 | colour=blue | moves along the road and can jump over obstacles
- road car | box w=60 h=100 | colour=red | bumps sideways into rocks or ditches for points
- rock | box w=30 h=30 | colour=green | acts as a scoring target when bumped into
- water | box w=900 h=20 | colour=blue | costs a life when landed in
- enemy car | box w=50 h=90 | colour=purple | can be crushed for points when landed on
RULES:
- The road scrolls upward continuously at a steady speed.
- Bumping a road car or rock into the road adds 100 points to your score.
- Pressing Space makes the player car jump over gaps, rivers and broken bridges.
- Landing on an enemy car destroys it and adds 200 points to your score.
- Landing in water reduces your lives by 1.
- Cars bump sideways off the road and can push back against tougher cars.
WIN: The game ends when all levels are completed with a full score.
LOSE: The game ends when your lives reach zero.
NUMBERS: speed=120, lives=3, score=0, level=1
RISK: Programming the dynamic side-bumping mechanics between road cars and obstacles to ensure consistent scoring and life costs.

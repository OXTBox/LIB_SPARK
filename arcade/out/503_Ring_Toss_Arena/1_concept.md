# Ring Toss Arena
PITCH: Players throw rings at moving posts to score points, using fast throws to catch rings on sliding posts for double points. It is fun because the fast-moving targets create a quick, focused arcade challenge.
CONTROLS: Arrow keys to move, Space to throw rings.
OBJECTS:
- ring | box w=120 h=120 | wireframe cyan | scores 1 point when landed on a post
- post | box w=40 h=300 | wireframe amber | slides along the floor and holds rings for double points
- arena | box w=900 h=600 | wireframe black | defines the play area for all game actions
RULES:
- Rings are thrown upward from the player's position using the Space key.
- Rings land on posts to score points, with rings on moving posts awarding double points.
- Posts slide slowly along the floor at each level, speeding up as levels progress.
- Each level contains fewer rings than the previous level, increasing challenge.
- Landing a ring on the arena floor costs one life.
WIN: Win the game by clearing all rings in the final level.
LOSE: Lose all lives and the game ends.
NUMBERS: rings=5, lives=3, post_speed=1.5, arena_steps=30
RISK: The precise collision detection between thrown rings and sliding posts to ensure fair scoring and correct double-point triggers.

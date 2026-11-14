# Jai Alai Block
PITCH: The player runs along an arena floor, hurls a ball upward at a block ceiling, and clears the blocks by catching the ball before it falls. It is fun because the fast, precise movements mirror real jai alai action while the falling blocks create a tense, reactive challenge.
CONTROLS: Use the arrow keys to move and Space to throw the ball.
OBJECTS:
- runner | box w=40 h=60 | wireframe cyan | moves along the arena floor and holds the scoop for catching the ball
- ball | box w=20 h=20 | wireframe magenta | is hurled upward by the player and falls back when not caught
- ceiling | box w=900 h=200 | wireframe orange | holds the blocks that must be cleared to finish the level
- falling_block | box w=30 h=30 | wireframe yellow | falls from the ceiling when hit and threatens the runner
- scoop | box w=80 h=40 | wireframe blue | catches the ball when the runner holds it
RULES:
- The runner moves only along the arena floor with arrow keys.
- Pressing Space hurls the ball upward at the ceiling.
- Hitting a ceiling block makes it fall from the top of the arena.
- Catching the ball in the scoop scores one point per catch.
- A falling block landing on the runner costs one life.
- The ball hitting the floor costs one life.
- Clearing all ceiling blocks finishes the current level.
WIN: Clear every block on the ceiling to complete the level.
LOSE: Lose all lives when a block lands on the runner or the ball hits the floor.
NUMBERS: runner_speed=120, ball_speed=240, falling_block_speed=90, lives=3, score=0, level_blocks=10
RISK: Programming the precise collision detection between the hurled ball and the ceiling blocks, and the timing of the falling blocks to avoid landing on the runner or the ball.

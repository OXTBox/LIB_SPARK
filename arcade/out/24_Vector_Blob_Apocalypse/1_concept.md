# Vector Blob Apocalypse
PITCH: The player spins and shoots to destroy jittery vector jelly blobs while surviving their swarm, turning chaotic blob waves into a fast-paced arcade battle. It is fun because every shot and spin creates instant visual chaos with simple, direct controls.
CONTROLS: Use arrow keys to spin and move, and press Space to fire bullets.
OBJECTS:
- player | box w=40 h=40 | cyan | the central character who spins, moves, and absorbs bullets
- bullet | box w=10 h=10 | yellow | fast projectiles that destroy jelly blobs on contact
- jelly_blob | box w=60 h=60 | magenta | jittery swarm blobs that move toward the player and split into smaller blobs when hit
- wave_zone | box w=900 h=600 | black | the full top-down screen area where all game actions occur
RULES:
- Jelly blobs drift and jitter from all screen edges toward the player at varying speeds.
- Shooting a jelly blob awards 100 points to the player's score.
- Jelly blobs split into smaller blobs when hit, increasing the swarm density.
- Losing one life occurs when a jelly blob touches the player.
- The player gains a new level after surviving the current wave.
WIN: The player survives all waves and clears the final wave to complete the level.
LOSE: The player runs out of all lives before clearing the final wave.
NUMBERS: player_lives=3, score=0, wave_level=1, bullet_speed=220, jelly_blob_speed=140, split_blob_size=30
RISK: Programming the dynamic splitting and jittering behavior of the jelly blobs to maintain balanced swarm density and collision detection while keeping the wireframe visuals clean.

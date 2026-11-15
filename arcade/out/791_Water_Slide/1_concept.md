# Water Slide
PITCH: You ride a wireframe water slide down a winding path, collecting glowing rings while keeping your balance on every bend to stay safe. It is fun because the fast, twisting ride feels like a real arcade water coaster with simple, satisfying controls.
CONTROLS: Use only the left and right arrow keys: the left key moves the slide left, the right key moves the slide right.
OBJECTS:
- Ring | box w=40 h=40 | colour=teal | collects 100 points and adds a small speed boost
- Slide Edge | box w=100 h=600 | colour=cyan | the boundary of the slide path; crossing it costs a life
- Water Stream | box w=900 h=20 | colour=blue | the flowing water background that moves with the slide
RULES:
- The slide moves continuously in the direction of the arrow keys, following the winding path.
- Collecting a ring adds 100 points to the score and increases slide speed by 1 unit per second.
- Crossing the slide edge reduces the player's lives by 1.
- The slide speed increases as the player collects more rings.
- A life is lost when the player crosses the slide edge or falls off the path.
WIN: The score reaches 1000 points before losing all lives.
LOSE: A life is lost when the player crosses the slide edge or falls off the path.
NUMBERS: score=0, lives=3, ring_collects=100, slide_speed=2, step_count=30
RISK: Keeping the player's balance on the winding slide bends while controlling only left and right movement to avoid crossing the edge is the hardest part to program.

# Draw Bridge Duel
PITCH: The player cranks the drawbridge to turn the knight away, letting a running hero cross safely across the castle bridge. It is fun because you must time the bridge movement perfectly to avoid the knight catching the hero.
CONTROLS: Use the arrow keys to move the hero, and press TAB to swap the hero with the knight.
OBJECTS:
- hero | box w=120 h=80 | wireframe blue | the player who runs across the bridge
- knight | box w=100 h=100 | wireframe red | the stationary guard who blocks the bridge
- drawbridge | box w=400 h=20 | wireframe green | the bridge that lifts when the hero cranks it
- castle | box w=900 h=600 | wireframe brown | the fixed castle structure on the screen
RULES:
- The hero moves forward with the arrow keys until the bridge lifts.
- The knight stays still and blocks the bridge until the hero cranks the bridge away.
- Press TAB to swap the hero and knight positions so the hero can cross.
- The hero scores one point for each safe crossing across the bridge.
- A life is lost if the hero runs into the knight while the bridge is closed.
WIN: The score reaches the target number of safe crossings.
LOSE: A life is lost when the hero collides with the knight on the closed bridge, or when the hero runs off the castle edge.
NUMBERS: hero_speed=150, knight_speed=0, drawbridge_speed=30, target_score=5
RISK: Timing the exact bridge lift and swap sequence to prevent the hero from colliding with the knight during the crossing.

# Two Hand Crane
PITCH: You pilot a dockside crane arm while a second hand guides a load on the ground, dropping crates onto the ship's marked spots to win the job. It is fun because the two hands must work together in perfect sync to clear every crate without wasting a life.
CONTROLS: Arrow keys move the crane arm, TAB swaps control between the arm and the ground guide.
OBJECTS:
- crane arm | box w=300 h=10 | colour=wireframe cyan | moves the lifting arm along the dockside track
- ground guide | box w=200 h=40 | colour=wireframe magenta | moves the load on the ground toward the target spots
- crate | box w=60 h=60 | colour=wireframe yellow | the load being dropped onto the ship's marked spots
- ship spot | box w=100 h=100 | colour=wireframe green | the marked target positions for the crates
- PROMPT | box w=200 h=80 | colour=wireframe blue | the dock marker guiding the ground guide's movement
- GLAZE | box w=150 h=150 | colour=wireframe white | the ship surface where crates must land safely
RULES:
- The crane arm moves forward or backward with the arrow keys, the ground guide follows with TAB.
- Drop each crate onto the green ship spot to score one point per successful drop.
- Swap control with TAB to adjust the arm and guide movements for better sync.
- A crate that falls off the dock edge or lands outside the ship spot costs one life.
- The game ends when all crates are successfully dropped or the player runs out of lives.
WIN: The score reaches the target number of successful crate drops.
LOSE: The player runs out of lives after a crate falls off the dock edge or lands outside the ship spot.
NUMBERS: crane arm speed=120, ground guide speed=90, crate drop speed=45, ship spot count=6, lives=3
RISK: Keeping the crane arm and ground guide movements perfectly synchronized to drop crates exactly on the ship spots without missing the target.

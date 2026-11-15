# Ghost Train
PITCH: lean the wire cart left or right through winding tracks to avoid scary signs, and keep the cart balanced to survive the dark bends. It is fun because every lean decision keeps the ride tense and the score grows with each safe pass.
CONTROLS: use only the left and right arrow keys: left moves the cart left, right moves the cart right.
OBJECTS:
- Ghost Sign | box w=120 h=80 | colour #4a3a5a | a scary sign that appears when the cart passes its path and costs a life if touched
- Wire Track | box w=900 h=600 | colour #2a2a3a | the winding path the cart travels along
- Cart | box w=100 h=60 | colour #6a6a8a | the player-controlled wire cart that moves with the arrow keys
RULES:
- The cart moves along the wire track using the left and right arrow keys.
- The cart leans left or right with each key press to stay balanced on bends.
- A score of 10 points is added for every safe bend passed.
- Touching a ghost sign costs one life.
- The cart tips over if it leans too far into a bend, costing one life.
WIN: the score reaches 100 points.
LOSE: touching a ghost sign or tipping the cart over.
NUMBERS: track width=900, track height=600, cart speed=120, score start=0, lives start=3
RISK: balancing the cart on sharp wire bends while tracking the ghost sign positions without causing a tip is the hardest part to program.

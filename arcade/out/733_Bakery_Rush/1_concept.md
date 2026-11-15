# Bakery Rush
PITCH: Players rush to carry bread from the ringing oven to the shelf before it burns or a customer leaves, testing quick reflexes and timing in a fast top-down bakery. It is fun because every move matters and the constant pressure keeps the gameplay engaging.
CONTROLS: Use the arrow keys only: up to move toward the oven, down to move toward the shelf, left and right to adjust movement direction.
OBJECTS:
- Bread | box w=120 h=80 | wireframe yellow | the item to carry from the oven to the shelf
- Oven | box w=200 h=120 | wireframe orange | the source of bread that rings a timer when bread is ready
- Shelf | box w=240 h=100 | wireframe green | the destination where bread must be placed safely
- Customer | box w=100 h=100 | wireframe red | a player who leaves if bread is not delivered on time
- Timer | vector text w=150 h=40 | wireframe blue | shows the remaining time for each bread delivery
RULES:
- Bread appears in the oven and rings a timer when it is ready to be picked up.
- Move with the arrow keys to carry bread from the oven to the shelf.
- Bread burns if it stays in the oven past its timer, costing one life.
- Bread is lost if a customer leaves before it reaches the shelf, costing one life.
- Each successful delivery adds 100 to the score.
- Each life lost resets the player position to the oven.
WIN: The score reaches 1000 points.
LOSE: One life is lost when bread burns or a customer leaves.
NUMBERS: bread_speed=120, oven_timer=30, shelf_distance=450, customer_leave_delay=20, score_per_delivery=100, lives=3
RISK: Timing the bread delivery against the customer leave delay and oven timer while moving with arrow keys only.

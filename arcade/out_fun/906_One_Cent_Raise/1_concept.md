# One Cent Raise
PITCH: A tiny worker in a endless warehouse must push boxes into matching rooms to keep the clock running, while dodging delivery towers and saving rare letters.
FUN:
- TOY: Walking into a box and pushing it forward makes the box slide toward the nearest matching storage room.
- CHOICE: You push boxes into matching rooms to save time, or push slow boxes aside to clear delivery towers that block the path.
- SURPRISE: Delivery men drop wobbly coloured box towers in random places, and some boxes hide letters V I B E behind other boxes.
- MOMENT: You push a slow box aside just as a delivery tower blocks the path, the clock pauses for 5 seconds, and the screen flashes PAY RAISE 1 CENT!
- EXTRA: You can walk into a truck bay on the screen edge and push a box out of one side to return to the other side empty-handed.
CONTROLS: Arrow keys only: up, down, left and right move the worker, and pushing into a box pushes it forward.
OBJECTS:
- delivery box | box w=120 h=80 | red | slides toward the nearest red storage room
- delivery box | box w=120 h=80 | blue | slides toward the nearest blue storage room
- delivery box | box w=120 h=80 | green | slides toward the nearest green storage room
- storage room | box w=200 h=150 | red | holds red boxes, clears the clock for 5 seconds when full
- truck bay | box w=300 h=200 | grey | pushes a box out of one edge to return empty-handed
- letter box | box w=60 h=60 | black | holds letters V I B E, line up for a big bonus
RULES:
- The worker moves only with arrow keys and pushes boxes by walking into them.
- Each box earns points divided by the current clock speed.
- Clearing a storage room of its matching colour stops the clock for 5 seconds.
- Delivery towers block the path and must be pushed aside to continue.
- Slow boxes buried behind others must be pushed first to save them for a bad moment.
- Every 10 deliveries cleared, the screen shows PAY RAISE 1 CENT!
WIN: Clear all delivery boxes, match letters V I B E, and reach the end of the warehouse.
LOSE: The clock reaches zero, ending the try.
NUMBERS: worker speed=120 units per step, delivery box speed=80 units per step, storage room clear time=5 seconds, screen width=900, screen height=600, clock speed=30 steps per second.
RISK: Programming the layered box stacking logic and the delivery tower collision detection to keep the warehouse flow stable without blocking the player's path.

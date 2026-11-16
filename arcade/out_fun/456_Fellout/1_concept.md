# Fellout
PITCH: You pilot a UFO carrying abducted stick figures, and must return them to the farm and trailer park before the locals, police and army catch them.
FUN:
- TOY: Spend an action point to hover in the open, and the UFO drifts smoothly while the abductees drift with it.
- CHOICE: Spend action points between moving the UFO, hovering, shielding, and beaming up a person, which pulls against each other as fewer points mean less time to save the figures.
- SURPRISE: A local, police officer or army unit moves into the open during your turn, ready to fire at the UFO and abductees.
- MOMENT: You hover in the open, beam up a figure, and watch it float back into the UFO as the other figures drift safely toward the farm.
- EXTRA: Use leftover action points to shield the UFO from incoming fire while you move or hover.
CONTROLS: Arrow keys move the UFO, Space hovers, X beams up a figure, Shift shields the UFO.
OBJECTS:
- UFO | box w=120 h=80 | wireframe cyan | moves the player's position and carries the abductees
- Abductee | box w=20 h=30 | wireframe orange | drifts with the UFO and can be beamed up
- Shield | box w=140 h=100 | wireframe yellow | blocks incoming fire from nearby units
- Local | box w=40 h=60 | wireframe red | moves and fires at the UFO and abductees
- Police | box w=35 h=55 | wireframe green | moves and fires at the UFO and abductees
- Army | box w=50 h=70 | wireframe purple | moves and fires at the UFO and abductees
RULES:
- The UFO moves one cell per action point, and hovering uses one action point per step.
- Beaming up a figure takes a full round of hovering in the open before the figure returns to the UFO.
- Each round the locals, police and army take their turn and fire at the UFO and abductees.
- Spend all action points each round or lose one life when a figure is caught or falls.
- Each level has a fixed action point count and a move limit; exceeding the move limit ends the try.
WIN: Beam up all abductees and return them to the farm and trailer park before the move limit ends.
LOSE: A figure is caught, falls, or the move limit is exceeded at the end of a round.
NUMBERS: action points=12, lives=3, UFO speed=40 units per step, Abductee speed=15 units per step, Shield speed=20 units per step, Local speed=30 units per step, Police speed=25 units per step, Army speed=35 units per step
RISK: Programming the turn-based action point spending and the timed beaming rounds that must keep the UFO and abductees in sync with the local, police and army turns.

# UFO Wrong Cargo
PITCH: A tiny pilot must hover over a midwest farm to beam wrong cargo back up before the locals, police and army shoot down the UFO.

FUN:
- TOY: Hovering the flight stick keeps the UFO steady, and the screen shows the UFO as a smooth, calm wireframe shape.
- CHOICE: The player trades beam power against speed: a stronger beam saves more people but slows the UFO, while a faster flight saves less people but risks being shot down.
- SURPRISE: A stray cow rolls out of the ranch fence and becomes wrong cargo, forcing the player to choose between saving it or saving the people in the hatch.
- MOMENT: The player beams a stuck figure back up, the hatch closes, and the UFO turns around to say "Damn it, not again!" in a calm wireframe display.
- EXTRA: The player can steer the UFO between the farm, ranch house and trailer park to avoid incoming buggies without changing the beam power.

CONTROLS:
Arrows move the UFO left or right; Space fires the tractor beam to save people.

OBJECTS:
- UFO | box w=120 h=80 | wireframe cyan | the player's flying vehicle that moves with arrow keys
- Tractor Beam | box w=160 h=40 | wireframe magenta | the beam that saves people from the UFO hatch
- Stick Figure | box w=30 h=50 | wireframe orange | a person tumbling out of the UFO hatch that the beam saves
- Cow | box w=40 h=30 | wireframe brown | wrong cargo that costs points when the beam hits it
- Ranch House | box w=180 h=120 | wireframe green | a local structure that shoots at the UFO with a wireframe weapon
- Police Buggie | box w=100 h=60 | wireframe blue | a squad vehicle that drives in to rescue people and shoots at the UFO

RULES:
- Use the arrow keys to move the UFO left or right over the farm, ranch house and trailer park.
- The tractor beam saves people from the UFO hatch and costs no lives.
- A cow caught by the beam costs 100 points and does not save anyone.
- Each shot from the locals, police or army costs 1 life.
- The try ends when the UFO is shot down, a life runs out, or the level timer reaches zero.

WIN: The player beams all the people out of the UFO hatch before the UFO is shot down or the timer ends.
LOSE: The UFO is shot down by the locals, police or army, or the level timer reaches zero.

NUMBERS:
UFO speed=120, beam speed=200, screen width=900, screen height=600, level timer=120 steps

RISK: Programming the tractor beam to distinguish people from wrong cargo while handling the varying shooter positions of the locals, police and army without breaking the wireframe rendering.

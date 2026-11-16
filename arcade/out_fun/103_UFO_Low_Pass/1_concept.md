# UFO Low Pass
PITCH: A tiny farmer tries to use a tractor beam to save their low-flying UFO before the UFO’s guns catch them.
FUN:
- TOY: Steering the UFO with the arrow keys makes the wireframe UFO smoothly glide over the farm and trailer park. The screen shows the UFO as a glowing wireframe box that follows your movement exactly.
- CHOICE: You must climb higher to reach the tractor beam, but climbing brings you closer to the UFO’s guns; you can also stay low to avoid the guns, but the beam will not reach.
- SURPRISE: Power lines and water towers rise between the farm and the beam, blocking your path until you find a gap to pass through.
- MOMENT: You climb past the water tower, the tractor beam arcs over the line, and the UFO’s lights dim as the beam pulls it back into the farm.
- EXTRA: You can use the arrow keys to steer the UFO around obstacles while waiting for the beam to activate, giving you extra time to plan your path.
CONTROLS: Arrow keys steer and climb the UFO; Space activates the tractor beam.
OBJECTS:
- UFO | box w=120 h=80 | wireframe cyan | the flying object the player chases and tries to save
- Tractor Beam | box w=200 h=40 | wireframe gold | the device that pulls the UFO back to safety
- Power Line | box w=30 h=200 | wireframe red | an obstacle that blocks the tractor beam path
- Water Tower | box w=60 h=120 | wireframe blue | an obstacle that blocks the tractor beam path
RULES:
- The UFO moves forward slowly while you steer with the arrow keys.
- The tractor beam activates only when you press Space, pulling the UFO toward the farm.
- Climbing with the up arrow increases your beam reach but lowers your safety distance from the UFO.
- Each power line or water tower you pass through costs one life.
- The UFO catches the player when the beam fails to reach it before the UFO reaches the farm.
WIN: The tractor beam successfully pulls the UFO back into the farm before the UFO catches the player.
LOSE: The UFO catches the player, or the UFO reaches the farm without the beam reaching it.
NUMBERS: beam_reach=400, ufo_speed=12, climb_speed=3, step_rate=30
RISK: Programming the dynamic obstacle collision between the climbing UFO, the tractor beam path, and the power lines and water towers to keep the beam reachable without letting the player get caught.

# Hollow Mountain
PITCH: A tiny miner with a flashlight climbs a hollow mountain, trying to escape a ghost and reach the diamond before falling into the glitched world below.
FUN:
- TOY: Pressing the flashlight key makes a bright beam sweep across the screen, pushing the drifting ghost away from the walls and floors.
- CHOICE: The flashlight beam scares the ghost but drains the battery, so the player must choose between using it to clear the path or saving battery for climbing.
- SURPRISE: Spiders hang silently on threads inside the holes, waiting to catch the miner if they are not careful.
- MOMENT: The miner presses the flashlight, the bright beam pushes the ghost straight out of the mountain, and the miner exhales in relief.
- EXTRA: The miner can walk slowly through the mountain floors while the flashlight stays on, exploring the holes and threads without risking the battery.
CONTROLS: Arrows move the miner left or right; Arrows plus Drop drop the miner through the holes; Space toggles the flashlight on and off.
OBJECTS:
- Diamond | box w=10, h=10 | cyan | the goal the miner must reach to climb back out of the mountain
- Ghost | box w=40, h=40 | white | drifts through walls and floors, pushed away by the flashlight beam
- Spiders | box w=20, h=20 | dark grey | hang on threads in the holes, catching the miner if touched
- Flashlight | box w=30, h=30 | yellow | a beam that scares the ghost but drains the battery
RULES:
- The miner moves one step per arrow press, and drops one step per Drop press.
- The flashlight beam pushes the ghost away from the walls and floors, but each use drains one battery unit.
- The miner loses a life if caught by a spider or falls through the bottom floor into the glitched world.
- The diamond is reached when the miner stands on the bottom floor, and the miner climbs back out by pressing Drop.
- The miner scores 10 points for every step climbed back out of the mountain.
WIN: The miner reaches the diamond on the bottom floor and climbs back out of the mountain.
LOSE: The miner is caught by a spider, falls through the bottom floor into the glitched world, or runs out of battery to keep the ghost away.
NUMBERS: flashlight battery=10, miner speed=1.5, ghost speed=0.8, spider speed=0.5, diamond points=100
RISK: Programming the ghost's path through the horizontal floors and walls while keeping the flashlight beam aligned with the mountain structure.

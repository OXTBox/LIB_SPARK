# Beacon Boats
PITCH: Walk the pier lighting beacons so harbour boats steer safely between them, and avoid unlit stretches that let drifting boats crash onto the rocks. It is fun because every step of the harbour depends on your careful lighting choices.
CONTROLS: Use the arrow keys to move along the pier; left and right arrows light or dim the selected beacons.
OBJECTS:
- pier | box 900,20 | wireframe blue | the walkable surface where the player moves and beacons are placed
- beacon | box 40,40 | wireframe amber | a light that guides boats between safe harbour paths
- harbour boat | box 120,60 | wireframe teal | a boat that steers toward lit beacons and drifts into unlit zones
- rock | box 80,80 | wireframe grey | an obstacle that catches drifting boats, costing a life
RULES:
- The player moves along the pier using arrow keys only.
- Beacons light up when the player selects them with left or right arrows.
- Harbour boats steer toward lit beacons and drift into unlit pier stretches.
- Drifting boats crash into rocks, losing one life.
- The score increases by 1 point for every safe harbour boat that reaches the harbour.
- Each try has a limited number of lives; losing all lives ends the try.
WIN: All boats safely reach the harbour with no rocks hit.
LOSE: Losing all lives from drifting boats hitting rocks ends the try.
NUMBERS: player_speed=150, beacon_light_speed=30, harbour_boat_speed=80, rock_life_cost=1, lives=3, score=0
RISK: Programming the dynamic steering logic for harbour boats to respond accurately to changing beacon lighting states on the pier.

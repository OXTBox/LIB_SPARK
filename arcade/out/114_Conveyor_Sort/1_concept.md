# Conveyor Sort
PITCH: Walk along the conveyors to flip junctions and guide coloured boxes to their matching bins, solving the factory sorting puzzle through careful route planning. It is fun because every move affects the whole track, making each turn a quick puzzle decision.
CONTROLS: Arrow keys only. Walking onto a junction flips it, pushing boxes along the conveyor paths.
OBJECTS:
- Conveyor track | box w=900 h=600 | black | moves coloured boxes along the path and accepts flipped junctions
- Red box | box w=40 h=40 | red | travels along the track until it reaches the red bin
- Green box | box w=40 h=40 | green | travels along the track until it reaches the green bin
- Blue box | box w=40 h=40 | blue | travels along the track until it reaches the blue bin
- Red bin | box w=60 h=60 | red | collects the red box when it arrives
- Green bin | box w=60 h=60 | green | collects the green box when it arrives
- Blue bin | box w=60 h=60 | blue | collects the blue box when it arrives
RULES:
- Boxes move automatically along their assigned conveyor paths after being pushed.
- Each correctly delivered box adds 100 to the score.
- Walking onto a junction flips its direction, changing the path of all boxes on that track.
- Each incorrect box delivery costs 1 life.
- The game ends when all boxes reach their matching bins for a full level.
WIN: The player completes all three box deliveries to their matching bins to clear the level.
LOSE: The player runs out of lives after incorrect box deliveries, ending the game.
NUMBERS: track_speed=30, box_speed=15, score_start=0, lives_start=3, level_steps=90
RISK: Programming the dynamic junction flipping logic that updates all box paths in real time without breaking the automatic conveyor movement.

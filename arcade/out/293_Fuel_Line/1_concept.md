# Fuel Line
PITCH: Race along a highway while grabbing fuel cans between traffic to keep your tank full, and outrun traffic swerves and oil spots before the tank runs dry. It is fun because the race only ends when fuel runs out, so every move matters and every can you grab directly extends your race.
CONTROLS: Use the arrow keys to steer, and press Space to grab fuel cans.
OBJECTS:
- fuel_can | box w=40 h=40 | colour=green | adds 50 fuel to the player's tank
- oil_spot | box w=60 h=60 | colour=orange | forces the player to spin and risks losing a life
- traffic_car | box w=80 h=80 | colour=blue | moves forward and may swerve into the player's lane
- finish_line | box w=900 h=100 | colour=white | marks the end of the race
RULES:
- Fuel drops continuously from the tank, decreasing by 2 units per step.
- Fuel cans appear randomly between traffic lanes and can be grabbed with Space.
- Traffic cars move forward at varying speeds and may swerve into the player's lane on purpose.
- Oil spots appear in the player's lane and force a spin, costing one life if the player hits them.
- Grabbing a fuel can adds 50 fuel to the tank, extending the race.
- Reaching the finish line with at least 10 fuel completes the race successfully.
- Losing all lives ends the game immediately.
WIN: The player reaches the finish line with at least 10 fuel in the tank.
LOSE: The player runs out of all lives before reaching the finish line.
NUMBERS: fuel_start=100, lives_start=3, speed_start=120, oil_spot_rate=1, traffic_swerve_rate=0.5
RISK: Programming the dynamic fuel drop, traffic swerve behavior, and oil spot collision detection to keep the race balanced and fair for the player.

# Lighthouse Keeper
PITCH: You steer a lighthouse beam to guide approaching ships safely through rocky reefs while keeping the lamp bright. It is fun because every ship requires a precise, quick adjustment to the beam to avoid danger.
CONTROLS: Left and right arrow keys to turn the lamp beam.
OBJECTS:
- Lighthouse lamp | box 80,120 | wireframe cyan | provides the rotating beam for guiding ships
- Ship | box 60,40 | wireframe amber | moves toward the lighthouse and needs the beam to steer clear
- Rock | box 100,80 | wireframe grey | blocks the path and creates hazards for the beam
- Beam | box 120,40 | wireframe white | the rotating light that guides the approaching ships
RULES:
- Ships approach the lighthouse from all sides at a steady speed.
- Each ship must stay inside the beam long enough to be steered safely away from rocks.
- A ship that stays in the beam too long without being guided away costs one life.
- The lamp rotates automatically to track the ship unless the player turns it with the arrow keys.
- The score increases by one point for each ship successfully guided clear of the rocks.
- The game ends when all lives are lost.
WIN: The score reaches the target number of successfully guided ships.
LOSE: All lives are used after a ship is caught by a rock or the beam misses the ship.
NUMBERS: ships=3, lives=3, score=0, beam_speed=2.5, ship_speed=1.2
RISK: Balancing the exact rotation speed of the lamp beam against the varying approach angles of ships from all sides to ensure fair steering.

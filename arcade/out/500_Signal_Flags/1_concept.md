# Signal Flags
PITCH: Walk along the quay to match the flag colour of incoming ships, then stand on each marker to wave them in for a score. It is fun because the harbour rhythm keeps your eyes and hands moving fast.
CONTROLS: Arrow keys only.
OBJECTS:
- Quay | box 900,600 | wireframe cyan | the path you walk along to reach ship berths
- Flag Marker | box 40,40 | wireframe magenta | the standing spot where you wave in matching flag colours
- Incoming Ship | box 120,80 | wireframe yellow | arrives showing a flag colour and needs its matching marker
- Berth | box 100,60 | wireframe green | the safe docking spot for a successfully waved ship
RULES:
- Ships move along the quay at fixed speeds matching their flag colour.
- Standing on the matching flag marker waves the ship in and adds 100 to the score.
- Each ship that is not waved in costs one life.
- The quay is one continuous path with no obstacles to block movement.
- The game ends after three lives are lost.
WIN: The score reaches 500 points by docking all incoming ships.
LOSE: Lose all three lives by failing to wave in incoming ships.
NUMBERS: quay_speed=120, marker_wave_delay=30, ship_arrival_interval=60, lives=3, score_start=0
RISK: Timing the exact standing position on flag markers to match incoming ship flag colours without missing the wave window.

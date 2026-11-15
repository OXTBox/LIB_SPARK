# Fare Dash
PITCH: The player drives a taxi through a neon city, picking up waiting fares and delivering them to their marked destinations to earn time and tips. It is fun because every second of the clock matters and near misses reward extra points.
CONTROLS: Use the arrow keys to move the taxi and Space to accelerate.
OBJECTS:
- Taxi | box w=120 h=60 | colour=cyan | the player's vehicle that moves along the city streets
- Fare | box w=80 h=40 | colour=magenta | a waiting passenger who needs a ride to their destination
- Destination | box w=60 h=40 | colour=yellow | the target point the fare wants to reach
- Clock | box w=100 h=40 | colour=lime | the time counter that increases as fares are delivered
- Tip | box w=60 h=30 | colour=orange | a bonus marker earned for near misses or successful deliveries
RULES:
- The taxi moves only along the arrow keys and accelerates with Space.
- Delivering a fare to its destination adds time to the clock and earns base points.
- Near misses and precise jumps award extra tips that increase the score.
- The clock counts down each step; failing to deliver fares before it reaches zero costs a life.
- Each life lost resets the clock to its starting value and clears remaining fares.
WIN: The player delivers all waiting fares before the clock reaches zero and earns a high score.
LOSE: The player loses all lives when the clock reaches zero without delivering any fares.
NUMBERS: clock_start=120, taxi_speed=180, fare_count=3, tip_multiplier=1.5, life_start=3
RISK: Programming the precise timing of near-miss detection and dynamic clock progression while keeping the wireframe rendering consistent across all moving objects.

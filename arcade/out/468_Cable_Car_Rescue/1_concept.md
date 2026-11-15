# Cable Car Rescue
PITCH: Run the winch and open the doors to lower stranded hikers from mountain stations while keeping cable cars apart on every span. It is fun because you manage tight timing and careful spacing to save every hiker without breaking the cable.
CONTROLS: Left and right arrows run the winch, Up arrow opens the doors.
OBJECTS:
- Hiker | box w=40 h=60 | colour #FFE060 | gets lowered from the station by the winch
- Cable Car | box w=120 h=80 | colour #80C0FF | moves along the span under the winch control
- Winch | box w=60 h=40 | colour #FF8030 | controls the lowering speed and car movement
- Station | box w=80 h=100 | colour #808080 | holds the stranded hiker waiting for lowering
RULES:
- The winch lowers hikers from stations at a steady speed controlled by the player.
- Hikers reach the ground safely when the winch reaches the bottom of the mountain.
- Each hiker lowered safely adds 100 to the score.
- Two cable cars meeting on the same span costs one life.
- A hiker that falls off the mountain before reaching the ground costs one life.
WIN: The score reaches 500 points by lowering all stranded hikers safely.
LOSE: One life is lost when two cable cars meet on the same span or a hiker falls off the mountain.
NUMBERS: winch_speed=30, hiker_lower_speed=15, car_move_speed=20, hiker_score=100, lives=3, steps_per_second=30
RISK: Keeping cable cars from colliding on spans while precisely timing the winch to lower hikers without letting them fall requires tight coordination of movement and timing logic.

# Ring Road
PITCH: Control your car along the ring road by changing lanes to keep other cars from braking, and score points by safely navigating the shifting road. It is fun because the constant lane changes create a fast, tense driving challenge that rewards quick, precise decisions.
CONTROLS: Left and right arrow keys change your car's lane on the ring road.
OBJECTS:
- Player Car | box w=40 h=80 | colour #00AAFF | moves along the ring road and changes lanes with the arrow keys
- Road | box w=900 h=600 | colour #003366 | forms the top-down ring road surface for movement
- Other Car | box w=50 h=80 | colour #FFAA00 | drives along the ring road and may brake if you change lanes incorrectly
- Brake Sign | box w=60 h=40 | colour #FF0000 | indicates a car has braked and must be avoided
RULES:
- Cars move along the ring road automatically at set speeds.
- Press left or right to change your car's lane to avoid braking other cars.
- Each safe lane change scores 10 points.
- Three braked cars being caught end the current shift.
WIN: The player completes the ring road shift with a score higher than the target score.
LOSE: Three braked cars being caught ends the current shift.
NUMBERS: player_car_lane=0, other_car_count=3, score_start=0, lives=3, shift_length=30
RISK: Coordinating the automatic movement of multiple cars along the ring road while accurately tracking lane changes to prevent braking collisions is the hardest part to program.

# Dropping Rooms
PITCH: Walk down a tower of rooms through moving holes to reach the bottom before the rooms fill with smoke. It is fun because every step feels like a quick, tense vertical chase with clear goals.
CONTROLS: Arrows only.
OBJECTS:
- Hole | box w=120 h=60 | colour=light blue | moves vertically to let the player pass through to the next room
- Room | box w=900 h=400 | colour=dark grey | acts as a floor section that fills with smoke if the player does not pass through the hole in time
- Key | box w=40 h=40 | colour=gold | can be picked up by walking into it, then pushed to press switches
- Switch | box w=60 h=60 | colour=orange | activates when a key is placed on it to open the next room's hole
- Smoke | box w=900 h=400 | colour=white | fills the room slowly, ending the room if it reaches full coverage
WIN: Reach the bottom room of the tower and collect the final key.
LOSE: The room fills completely with smoke before the player passes through the hole to the next room.
NUMBERS: hole_speed=120, room_fill_speed=30, smoke_fill_speed=45, move_count=300
RISK: The synchronized vertical movement of the holes and the smoke fill across stacked rooms is the hardest part to program.

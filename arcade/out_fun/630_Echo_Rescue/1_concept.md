# Echo Rescue
PITCH: A tiny survivor walks a haunted hallway of doors, trying to find the door that follows them home.
FUN:
- TOY: Pressing the arrow keys moves the survivor through the wireframe hallway. The screen shows the survivor as a moving wireframe box, and the hallway walls shift with their movement.
- CHOICE: The survivor wants to reach the door that follows them home, but wandering into wrong doors costs lives, so they choose between exploring new rooms and risking their lives.
- SURPRISE: Every door in the hallway leads to an unexpected room, and the sentry and survivor pop out of the door in a different place than where they entered.
- MOMENT: The survivor walks into a door, pops out in a new room, and sees the door that follows them still waiting, then presses the arrow to walk toward it.
- EXTRA: The player can watch the wandering survivors and sentries move through the rooms without pressing any arrow keys, so the hallway stays alive on its own.
CONTROLS: Arrow keys move the survivor through the hallway.
OBJECTS:
- survivor | box w=40 h=40 | wireframe cyan | moves through the hallway with arrow keys
- door | box w=60 h=80 | wireframe gold | leads the survivor home when walked into
- sentry | box w=30 h=30 | wireframe red | patrols the hallway and moves survivors back
- hallway | box w=900 h=600 | wireframe dark grey | the top-down haunted room space
RULES:
- The survivor moves only with the arrow keys, one step at a time.
- Every door the survivor enters changes their location to an unexpected room in the hallway.
- The sentry patrols the hallway and moves each wandering survivor back to where they were found.
- Touching the sentry costs one life.
- The survivor reaches the door that follows them home to win the level.
WIN: The survivor reaches the door that follows them home and exits the hallway.
LOSE: The survivor touches a sentry and loses a life, or the survivor runs out of lives to continue.
NUMBERS: survivor_speed=2, sentry_speed=1, door_speed=0, lives=3, steps_per_second=30
RISK: Making the sentry and survivor follow the player through unexpected doors while keeping their movement consistent across all rooms.

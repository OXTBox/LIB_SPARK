# Two Key Doors
PITCH: You are a tiny player trapped in a maze, forced to guide two heroes through the level by swapping them with TAB.
FUN:
- TOY: Swapping the two heroes with TAB lets the other hero follow, and the screen instantly moves both heroes toward the nearest open door.
- CHOICE: You want both heroes to reach their matching doors, but swapping them delays one hero while letting the other pass, so the two goals pull against each other.
- SURPRISE: A pressure plate opens a door for either hero, but once one hero stands on it, the other hero can still walk through it.
- MOMENT: You swap the heroes just as the red hero steps into the red door, and the blue hero instantly follows through the blue door, clearing the level in one move.
- EXTRA: You can stand still on a pressure plate to hold a door open while the other hero passes through it, adding a small pause to the maze.
CONTROLS: Use the arrow keys to move the current hero, and use TAB to swap the two heroes so the other hero follows.
OBJECTS:
- red hero | box w=40 h=40 | red | moves with the arrow keys, opens the red door when it walks into it
- blue hero | box w=40 h=40 | blue | moves with the arrow keys, opens the blue door when it walks into it
- red door | box w=80 h=120 | red | opens when the red hero walks into it, stays open until the red hero leaves
- blue door | box w=80 h=120 | blue | opens when the blue hero walks into it, stays open until the blue hero leaves
- pressure plate | box w=60 h=30 | yellow | holds a door open while either hero stands on it, allowing the other hero to pass
- white exit | box w=100 h=100 | white | requires both heroes to reach it to complete the level
RULES:
- The arrow keys move the current hero one step in the chosen direction.
- TAB swaps the two heroes so the other hero follows the current hero's movement.
- A red door opens when the red hero walks into it, and a blue door opens when the blue hero walks into it.
- A pressure plate holds a door open while either hero stands on it, letting the other hero pass through.
- Level 3 introduces timed doors that close after 30 steps if neither hero stands on the pressure plate.
- The white exit is only cleared when both heroes reach it.
- Scores increase by 1 point for each step a hero moves toward the exit.
WIN: Both heroes reach the white exit and the level is cleared.
LOSE: Nothing: the score is moves against par, and there are no lives to lose.
NUMBERS: hero_speed=150, door_speed=0, plate_speed=0, score_par=0
RISK: Timed doors from level 3 that close automatically if neither hero stands on the pressure plate while they are open.

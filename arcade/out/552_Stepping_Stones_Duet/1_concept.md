# Stepping Stones Duet
PITCH: Two players leapfrog across a sinking river by standing on rising stones, creating a fast, tense duet of timing and movement.
CONTROLS: Arrow keys move the player, TAB swaps the two players.
OBJECTS:
- player | box w=20 h=30 | colour=blue | moves along the river with arrow keys
- player | box w=20 h=30 | colour=green | moves along the river with arrow keys
- stone | box w=100 h=20 | colour=white | rises when a player stands on it, sinks when nobody does
RULES:
- Each player moves one step per arrow key press.
- Players gain points for each successful leap across a stone.
- A player loses a life if they fall into the river without standing on a stone.
WIN: The first player reaches the far end of the river with a full life.
LOSE: A player falls into the river and loses a life.
NUMBERS: player=1 life, stone speed=1 unit per step, player speed=1 unit per step
RISK: Keeping the two players' positions and stone states synchronized across both players during continuous movement.

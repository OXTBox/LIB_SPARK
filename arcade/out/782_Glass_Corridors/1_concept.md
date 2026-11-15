# Glass Corridors
PITCH: Navigate a maze of glass walls while avoiding one-way doors to reach the central crystal, scoring by the number of steps taken. It is fun because the hidden route forces careful observation and quick reflexes in a retro wireframe arcade setting.
CONTROLS: Use arrow keys to move, Space to activate one-way doors.
OBJECTS:
- Glass Wall | box 450,300 | cyan | blocks movement but lets the player see through it
- One-way Door | box 120,200 | magenta | only opens when Space is pressed, closes after one step
- Central Crystal | box 100,100 | gold | the level goal, visible from most areas
- Step Counter | box 80,40 | white | records the player's step count as score
- Secondary Crystal | box 100,100 | green | the next level goal, hidden behind glass
RULES:
- Player moves one step per arrow key press, counted as one score point each.
- Glass walls block movement but remain fully visible to the player.
- One-way doors open only when Space is pressed and close automatically after one step.
- Each level adds more glass walls and one-way doors to increase difficulty.
- Losing all lives ends the game and resets the player to the first level.
WIN: Reach the central crystal to complete the current level.
LOSE: Lose all lives while navigating the maze.
NUMBERS: lives=3, score=0, steps=0, level=1, crystal_count=1
RISK: Programming the hidden route logic for the central crystal while ensuring glass walls remain visible without blocking player movement.

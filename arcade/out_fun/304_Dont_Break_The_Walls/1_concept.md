# Dont Break The Walls
PITCH: A clumsy player in a dark glass maze smashes through walls to reach the stone, hoping to avoid breaking the stone of a glass house.
FUN:
- TOY: Breaking a wall with the arrow keys creates a satisfying crash of glass and adds a point to the score.
- CHOICE: The player chooses between breaking walls to move faster and saving lives by staying still, as bigger mushrooms cost more walls to break.
- SURPRISE: Bigger mushrooms in the maze break two walls at once, letting the player pass through without extra crashes.
- MOMENT: The player hits the stone at the maze end and the glass shatters in a bright flash, ending the level with a sense of relief.
- EXTRA: The player can slow down or speed up the maze movement to time their wall breaks and avoid unnecessary damage.
CONTROLS: Arrow keys move the player; arrow up slows the maze, arrow down speeds the maze.
OBJECTS:
- player | box w=20 h=20 | colour=light grey | moves through the maze by breaking walls
- wall | box w=40 h=40 | colour=dark blue | breaks with a glass crash and costs one point
- stone | box w=30 h=30 | colour=gold | the goal at the maze end
- mushroom | box w=30 h=30 | colour=green | breaks two walls at once when touched
RULES:
- The player moves only with the arrow keys and breaks any wall they bump into.
- The score starts at the total number of walls in the maze and increases by one for every broken wall.
- Bigger mushrooms let the player break two walls at once instead of one.
- Breaking the stone ends the level successfully.
- Each unbroken wall costs one life if the player bumps into the stone without reaching it.
WIN: Reaching the stone at the end of the maze to complete the level.
LOSE: Breaking the stone by bumping into it without reaching the stone, or running out of lives.
NUMBERS: walls=40, mushroom_count=3, speed_up=1.5, speed_down=0.5
RISK: Programming the limited wall visibility and the dynamic wall breaking logic for the clumsy player movement.

# Fold Map Room
PITCH: Walk through a top-down map that folds to open hidden paths, using arrow keys to reach the exit and F to fold the left half over the right. It is fun because solving each fold reveals new routes and challenges your spatial planning.
CONTROLS: Arrow keys to move, F to fold the left half over the right.
OBJECTS:
- fold line | box w=450 h=10 | colour=blue | folds the left half of the map over the right half
- exit portal | box w=80 h=80 | colour=green | marks the goal area to reach
- key | box w=30 h=30 | colour=purple | opens a locked wall when picked up
- wall | box w=120 h=120 | colour=red | blocks movement until a fold opens a path
- switch | box w=40 h=40 | colour=orange | activates when folded to open a new path
WIN: Reach the exit portal after solving all fold lines in the level.
LOSE: Lose a life when you collide with a locked wall without picking up a key, or when the level move count is exceeded.
NUMBERS: moves=50, lives=3, fold_lines=2, keys=1
RISK: Programming the dynamic wall collision and fold logic that changes the map layout in real time.

# Kitten Rescue
PITCH: Climb a tree with the left, right, and up keys to reach kittens, carry them down one at a time, and save them before thin branches crack. It is fun because every step tests your timing while you protect the kittens from falling.
CONTROLS: Left and right move you along the tree branches, up climbs to higher branches.
OBJECTS:
- branch | box w=120 h=20 | colour=green | the path you climb on the tree
- kitten | box w=40 h=40 | colour=yellow | a rescued item you carry down to the base
- thin_branch | box w=80 h=10 | colour=orange | a branch that cracks if you stand on it
- player | box w=30 h=50 | colour=blue | the climber moving along branches
RULES:
- Left and right shift your position along the current branch.
- Up moves you to the next higher branch.
- Carrying a kitten prevents you from climbing higher branches.
- Standing on a thin branch reduces its strength by one step.
- Each rescued kitten adds 100 to the score.
- Standing on a cracked thin branch costs one life.
WIN: Rescue all kittens and carry them down to the base.
LOSE: Falling off the tree or losing all lives ends the try.
NUMBERS: player_speed=150, kitten_carry_speed=100, thin_branch_crack_rate=30, score_per_kitten=100, lives=3
RISK: Managing the thin branches so they crack only after the player stands on them too long while carrying kittens is the hardest part to program.

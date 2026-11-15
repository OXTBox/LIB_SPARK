# Twin Keys Vault
PITCH: Players swap two vault locks in the same second using arrow keys and TAB to open the vault, while guards walk between the locks to keep the swap fast and safe. It is fun because the quick timing challenge creates constant tension with every movement.
CONTROLS: Arrow keys to move, TAB to swap the two locks, Space to activate the vault door.
OBJECTS:
- Vault Door | box 900,600 | wireframe cyan | opens the vault when both locks are swapped in the same second
- Lock One | box 120,120 | wireframe magenta | acts as the first vault lock to be swapped
- Lock Two | box 120,120 | wireframe magenta | acts as the second vault lock to be swapped
- Guard | box 80,120 | wireframe orange | walks between the locks to block the swap
- PROMPT | box 200,60 | wireframe blue | shows the swap instruction to the player
- GLAZE | box 150,150 | wireframe green | acts as the final vault lock to be swapped
RULES:
- The player moves with arrow keys and swaps locks with TAB.
- Guards walk slowly between the two locks at a fixed pace.
- Each successful same-second swap increases the player's score by 100.
- A guard touching the player costs one life.
- The vault opens after both locks are swapped in the same second.
- The game ends when the player runs out of lives.
WIN: The player opens the vault after swapping both locks in the same second.
LOSE: The player runs out of lives while guards block the swap.
NUMBERS:
- guard_speed=1.5
- player_speed=2.0
- score_start=0
- lives_start=3
- steps_per_second=30
- screen_width=900
- screen_height=600
RISK: Programming the precise same-second lock swap logic while handling guard movement and collision detection in real time.

# Cargo Crawler
PITCH: Walk through a top-down warehouse grid with arrow keys to pull crates behind you like a train, then guide the chain to the loading dock without it crossing itself. It is fun because the puzzle comes from tight aisles and a fixed forklift loop, making every step feel like a real warehouse challenge.
CONTROLS: Arrow keys to move, Space to pull the crate chain.
OBJECTS:
- player | box w=20 h=20 | wireframe cyan | moves through the warehouse grid with arrow keys
- crate | box w=30 h=30 | wireframe orange | pulled behind the player by the chain, forms the cargo train
- forklift | box w=40 h=40 | wireframe yellow | drives a fixed loop through the warehouse on its own
- loading dock | box w=120 h=60 | wireframe green | the target area where the crate chain must be placed
RULES:
- The player moves only with arrow keys, pulling crates behind them as a connected chain.
- Each crate successfully placed at the loading dock adds 100 to the score.
- The forklift moves along its fixed loop automatically, blocking paths and aisles.
- The crate chain loses 1 life if it crosses itself or touches the forklift.
- The player loses a life if they leave the warehouse grid or fail to reach the dock in time.
WIN: The crate chain is fully placed at the loading dock without any self-crossing or forklift contact.
LOSE: The player runs out of lives before placing the complete crate chain at the loading dock.
NUMBERS: player_speed=150, crate_speed=120, forklift_speed=90, score_start=0, lives_start=3, steps_per_second=30
RISK: Programming the forklift's fixed loop interaction with the crate chain to prevent self-crossing while maintaining safe warehouse paths.

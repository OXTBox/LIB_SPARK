# Signal Relay
PITCH: Guide the signal through a maze of relay pads using arrow keys and swaps, passing the signal step by step to reach the final pad pair. It is fun because every path requires careful navigation and quick key swaps to avoid losing your lives.
CONTROLS: Use the arrow keys to move, press Space to swap the hero, and press TAB to swap the hero.
OBJECTS:
- Signal Pad | box w=120 h=60 | colour=blue | acts as a relay pad that holds and passes the signal to the next visible pad
- Signal Pad | box w=120 h=60 | colour=green | acts as a relay pad that receives the signal from the previous visible pad
- Hero | box w=40 h=40 | colour=red | moves through the maze and can swap positions with the signal pad
- One-way Window | box w=80 h=80 | colour=purple | allows the signal to pass only in one direction through the corridor
RULES:
- The signal moves only between relay pads that can see each other down straight corridors.
- Arrow keys move the hero through the maze to reach the next relay pad pair.
- Press Space to swap the hero with the current relay pad to pass the signal forward.
- The score increases by 10 points for each successful signal relay.
- Losing all lives costs a life and resets the hero to the start of the current level.
- One-way windows block the signal from passing backward through the corridor.
WIN: Reach the final relay pad pair to complete the level and unlock the next level.
LOSE: Lose all lives and the game ends with no remaining lives to continue.
NUMBERS: hero_speed=120, signal_speed=80, lives=3, score=0, level=1
RISK: Programming the one-way window logic to correctly restrict signal direction while ensuring the hero can still navigate the maze without interference.

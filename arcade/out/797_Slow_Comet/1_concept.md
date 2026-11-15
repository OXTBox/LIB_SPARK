# Slow Comet
PITCH: You steer your probe rightward through slow comets while dodging their drifting tails, and reach the space station dock to score points. It is fun because the slow movement creates a calm, focused arcade feel with simple, satisfying movement.
CONTROLS: Use only the up and down keys: up moves the probe upward, down moves the probe downward.
OBJECTS:
- probe | box w=10 h=20 | colour=light cyan | moves rightward through space, controlled by up and down keys
- comet | box w=80 h=40 | colour=deep purple | drifts slowly leftward, its tail pushes the probe slightly leftward
- comet tail | box w=120 h=20 | colour=dark magenta | trails behind the comet, pushes the probe leftward when touched
- space station dock | box w=150 h=60 | colour=bright yellow | the goal location to reach for scoring points
RULES:
- The probe moves rightward automatically at a steady speed.
- Up and down keys adjust the probe's vertical position to dodge comets and their tails.
- Reaching the space station dock scores 100 points per attempt.
- Touching a comet tail costs one life.
WIN: Reach the space station dock to complete a successful scoring attempt.
LOSE: Lose all lives when touched by a comet tail, ending the current try.
NUMBERS: probe_speed=15, comet_speed=3, tail_push_speed=2, dock_score=100, lives=3
RISK: Programming the precise leftward push from comet tails while keeping the probe's rightward movement stable and accurate.

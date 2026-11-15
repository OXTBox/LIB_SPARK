# Bell Ringer
PITCH: Walk through the bell tower ropes with arrows to ring bells in the exact tune order, and match the melody to keep the score high. It is fun because the rhythm of the bells feels like a living arcade challenge.
CONTROLS: Use the arrow keys to move forward through the tower ropes; no other keys are needed.
OBJECTS:
- Bell | box w=120 h=80 | colour #FFD700 | rings when stepped on to play the next note of the tune
- Rope | box w=60 h=400 | colour #8B4513 | blocks movement until the correct bell is rung in sequence
- Tune Sequence | box w=900 h=200 | colour #FFA500 | shows the required bell order for the current level
- Score | box w=300 h=60 | colour #00FF00 | tracks the number of bells rung correctly
- Lives | box w=200 h=60 | colour #FF0000 | shows remaining attempts to complete the tune
RULES:
- Move forward with the arrow keys through the tower ropes only.
- Ringing a bell in the correct tune order adds one point to the score.
- Ringing a bell out of order restarts the tune sequence and costs one life.
- The tune sequence advances automatically after each bell is rung.
- Complete the full tune to unlock the next level.
WIN: The player completes the full tune sequence with all lives remaining to unlock the next tower level.
LOSE: The player runs out of lives after a wrong bell rings, ending the current try.
NUMBERS: score=0, lives=3, level=1, tune_steps=5, move_speed=120
RISK: Programming the automatic tune sequence progression and detecting bell order correctness in real time while handling wrong bell restarts.

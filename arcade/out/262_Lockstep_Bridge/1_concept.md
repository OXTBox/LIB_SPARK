# Lockstep Bridge
PITCH: Walk both bridges together to cross the gaps, and keep the PROMPT and GLAZE aligned to pass every challenge. It is fun because the two bridges must move in perfect sync to survive.
CONTROLS: Left and right arrow keys move both heroes at the same time.
OBJECTS:
- PROMPT | box w=120 h=40 | wireframe cyan | triggers the bridge switch to activate the crossing gap
- GLAZE | box w=140 h=50 | wireframe magenta | blocks the path and must be crossed when the other hero stands on solid ground
- Bridge A | box w=900 h=20 | wireframe steel blue | the left bridge with gaps that must be crossed
- Bridge B | box w=900 h=20 | wireframe steel blue | the right bridge with gaps that must be crossed
RULES:
- Both heroes move together with the left and right keys, never separately.
- The PROMPT triggers the bridge switch to open the crossing gap on either bridge.
- Gaps on both bridges must be crossed when the other hero is on solid ground.
- The score increases by 10 points for each successful gap crossing.
- A life is lost if either hero steps into a solid obstacle instead of a gap.
WIN: The player crosses all gaps on both bridges in perfect sync.
LOSE: The player steps into an obstacle on either bridge, losing a life.
NUMBERS: hero_speed=150, gap_width=80, score_start=0, lives_start=3, steps_per_second=30
RISK: Keeping the two bridges perfectly synchronized while managing the timing of the GLAZE gaps without timing errors.

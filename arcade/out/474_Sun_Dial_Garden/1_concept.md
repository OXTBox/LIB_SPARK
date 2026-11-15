# Sun Dial Garden
PITCH: The player moves through hot sand by staying under the sweeping shadow of a garden pillar, collecting flowers to score points while protecting their score from the rising heat. It is fun because the clock-like shadow creates a simple, rhythmic challenge that keeps the top-down garden feel alive.
CONTROLS: Use the arrow keys to move the player in four directions on the garden screen.
OBJECTS:
- Garden Pillar | box w=400 h=600 | wireframe green | creates a sweeping shadow that provides safe zones to cross hot sand
- Hot Sand | box w=900 h=600 | wireframe orange | blocks the player from moving freely and costs a life if the player stays outside the pillar's shadow
- Flower | box w=30 h=30 | wireframe pink | adds 100 points to the player's score when touched
- Player | box w=20 h=20 | wireframe blue | moves with the arrow keys and must stay inside the pillar's shadow to survive
RULES:
- The pillar's shadow sweeps around the screen in a clock-like pattern every 30 steps.
- Touching a flower increases the player's score by 100 points.
- Staying outside the pillar's shadow for more than 30 steps costs one life.
- The game ends when all lives are lost or the player collects the required number of flowers to win.
WIN: The player collects the required number of flowers to complete the garden level.
LOSE: The player loses all lives by staying outside the pillar's shadow for too many steps.
NUMBERS: player_speed=150, flower_score=100, life_cost_steps=30, required_flowers=5
RISK: Programming the dynamic, sweeping shadow of the pillar to accurately track the player's safe zones while maintaining the 1983 arcade wireframe visual style.

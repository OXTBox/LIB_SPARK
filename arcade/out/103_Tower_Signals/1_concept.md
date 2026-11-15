# Tower Signals
PITCH: Walk across the hills to light signal towers in a chain, keeping the message visible until every tower is lit. It is fun because each step tests your timing and chain logic against the fading signal.
CONTROLS: Arrow keys move the player; walking into a tower lights it.
OBJECTS:
- Player | box w=20 h=20 | wireframe cyan | moves through the hills and lights towers when entering them
- Signal Tower | box w=40 h=40 | wireframe orange | lights when the player walks into it, then holds the signal for the next tower
- Fading Signal | box w=100 h=100 | wireframe yellow | fades after the last tower is lit, ending the chain
RULES:
- The player moves only with arrow keys across the top-down hills.
- Each tower lights when the player enters its area.
- The signal chain must connect each tower to the next one before it fades.
- The score increases by 10 points for each successfully lit tower.
- The signal fades after the final tower is lit, ending the chain.
WIN: The signal chain reaches the last tower and holds until it fades.
LOSE: The signal fades before all towers are lit.
NUMBERS: player_speed=120, tower_life=90, score_per_tower=10
RISK: Keeping the fading signal timing and chain visibility logic synchronized across multiple towers in the top-down view.

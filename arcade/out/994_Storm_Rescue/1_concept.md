# Storm Rescue
PITCH: Guide stranded villagers up the hilltop while the rising sea floods the low cells, using precise keyboard moves to survive the growing storm. It is fun because every step of the climb feels urgent and your quick reactions directly protect the villagers from the flood.
CONTROLS: Use the arrow keys to move, press Space to climb uphill.
OBJECTS:
- Villager | box w=40 h=40 | colour=teal | acts as a stranded cell the player must guide upward
- Hilltop | box w=600 h=200 | colour=blue | the final safe destination where rescued villagers rest
- Sea | box w=900 h=100 | colour=cyan | rises one height step every 30 seconds, flooding low cells
- Flood | box w=900 h=40 | colour=red | destroys villagers and unlocks faster sea rise
RULES:
- The sea rises one height step every 30 seconds, flooding lower cells over time.
- Move villagers upward using arrow keys to reach the hilltop before flooding.
- Press Space to climb villagers uphill when they are positioned on a valid climb path.
- Villagers rescued at the hilltop add 100 to the score.
- Flooding a cell costs 1 life, ending the player's current level attempt.
- Bridges wash away after 2 steps, forcing villagers to find new climb paths.
WIN: Reach the hilltop with all villagers safely rescued before the sea floods the climb path.
LOSE: The sea floods the climb path or the player loses all lives before rescuing all villagers.
NUMBERS: sea_rise_steps=1, villager_count=3, climb_speed=2, bridge_life=2, score_per_rescue=100, lives=3
RISK: Programming dynamic bridge washing and real-time sea rise synchronization to keep the 1983 arcade wireframe visuals consistent with the gameplay logic.

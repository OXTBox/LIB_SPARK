# Fuse Runner
PITCH: You walk forward through a glowing wire corridor while a lit fuse burns behind you, reaching switches to cut it before it catches you and starting a new fuse each time. It is fun because every step is a tense race against the burning wire, with quick keyboard moves keeping you on the edge of danger.
CONTROLS: Arrow keys only.
OBJECTS:
- player | box w=20 h=40 | colour=light cyan | moves forward along the wire corridor
- fuse | box w=120 h=20 | colour=orange | burns along the floor behind the player, catching the player if it reaches them
- switch | box w=30 h=30 | colour=yellow | cuts the active fuse and starts a new fuse ahead
RULES:
- The player moves forward one step per arrow key press, never backward.
- Each switch cut adds 100 to the score.
- A life is lost when the burning fuse reaches the player.
WIN: The player cuts all active fuses before they catch you and reach the end of the corridor.
LOSE: The burning fuse catches the player, ending the game.
NUMBERS: player_speed=150, fuse_speed=120, switch_score=100, lives=3, steps_per_second=30, screen_width=900, screen_height=600
RISK: Timing the fuse burn progression and switch activation to match the player's forward movement without causing unfair collision or missing cut opportunities.

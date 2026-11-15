# Firefly Jar
PITCH: Walk through the dark meadow at night and catch blinking fireflies only when they are lit, building a score by collecting them safely. It is fun because the timing of the night is a playful challenge that rewards quick, careful movement.
CONTROLS: Arrow keys only.
OBJECTS:
- Firefly | box w=10 h=10 | cyan | blinks on and off, can be caught only when lit
- Meadow ground | box w=900 h=600 | dark green | provides the walking surface for the player
- Switch | box w=20 h=20 | orange | opens paths to new meadow areas
RULES:
- Fireflies blink on and off automatically in the meadow.
- Catch a lit firefly by walking into it to add 10 to the score.
- Dark fireflies cannot be caught and pass through the player without effect.
- Each missed lit firefly costs 1 life.
- The game ends when all lives are lost.
WIN: The score reaches 100 to complete the meadow challenge.
LOSE: All lives are lost after missing lit fireflies.
NUMBERS: player_speed=120, firefly_blink_speed=45, switch_open_delay=30
RISK: Timing the exact moment to walk into lit fireflies without missing dark ones while navigating the meadow paths.

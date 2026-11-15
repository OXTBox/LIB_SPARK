# Tunnel Lights
PITCH: Player navigates a dark tunnel network by switching lights at crossings to light the path ahead, racing to reach the exit before every light's 20-second glow runs out. It is fun because every step depends on quick, precise light decisions in a tense, immersive arcade setting.
CONTROLS: Arrow keys only: Left and Right move the player along the tunnel, Up switches the current crossing light on or off.
OBJECTS:
- Player | box w=10 h=10 | wireframe cyan | moves through the tunnel network using arrow keys
- Crossing Light | box w=30 h=20 | wireframe amber | lights the tunnel ahead for 20 seconds when switched on
- Tunnel | box w=900 h=600 | wireframe dark grey | the first-person play area where the player travels
- Exit | box w=50 h=50 | wireframe bright green | the goal the player must reach to complete a level
RULES:
- The player moves one step per arrow key press along the tunnel network.
- Switching a crossing light on activates its 20-second glow, lighting the tunnel ahead for that duration.
- The score increases by 1 point for each successful crossing completed with the light active.
- Each light can only be used once per level; using it without the glow active costs one life.
- The player loses a life if the light is switched off before its 20-second glow expires.
WIN: Reach the exit box while the current crossing light is still glowing.
LOSE: The player runs out of lives, or the light glow expires before the player reaches the exit.
NUMBERS: player_speed=1, light_glow_seconds=20, screen_width=900, screen_height=600, level_par=10
RISK: Programming the dynamic light glow state and tunnel path navigation that requires real-time state tracking per crossing while keeping the 1983 arcade wireframe visual style.

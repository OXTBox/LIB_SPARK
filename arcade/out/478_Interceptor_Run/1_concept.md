# Interceptor Run
PITCH: You pilot an armed agent car up a scrolling highway, shooting or ramming enemy vehicles while protecting civilian cars, and unlock stronger weapons by driving into supply trucks. It is fun because the fast top-down action stays tight and every drive brings a new tactical upgrade.
CONTROLS: Use the arrow keys to steer and Space to shoot.
OBJECTS:
- Agent Car | box 180,120 | wireframe cyan | the player vehicle that moves and shoots
- Enemy Car | box 160,100 | wireframe red | a hostile vehicle that moves toward the player and can be rammed
- Civilian Car | box 140,90 | wireframe white | a safe vehicle that must not be hit to avoid losing points
- Supply Truck | box 200,140 | wireframe orange | a vehicle that gives the player a new weapon when driven into
- Bomb Helicopter | box 120,80 | wireframe dark gray | a helicopter that drops bombs and must be avoided
RULES:
- Enemy cars scroll upward at increasing speed while civilian cars stay on the road.
- Shooting or ramming enemy cars adds to the score; hitting civilian cars costs points.
- Driving into the back of a supply truck grants a new weapon: oil slick, smoke screen, or missiles.
- The car transforms into a boat when reaching the water at the road end.
- Losing all lives ends the game.
WIN: The player reaches the end of the road with a positive score and all lives remaining.
LOSE: The player runs out of lives before reaching the end of the road.
NUMBERS: player_lives=3, score=0, enemy_count=5, speed=120, screen_width=900, screen_height=600
RISK: Programming the dynamic weapon upgrades and smooth vehicle-to-boat transformation while keeping the scrolling top-down movement stable for all vehicle types.

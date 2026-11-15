# Wire Walker
PITCH: The player leans left or right to steer along a high wire while dodging wind gusts, keeping their balance to reach the next section of the wire. It is fun because every movement feels responsive and the wire's tipping clearly shows your balance in real time.
CONTROLS: Left key leans the player left, right key leans the player right, up key steps forward along the wire.
OBJECTS:
- Wire | box w=900 h=20 | colour=wireframe cyan | the path the player walks along to reach the next section
- Wind Gust | box w=120 h=60 | colour=wireframe orange | pushes the player's lean, making the wire tip
- Player | box w=40 h=60 | colour=wireframe green | the character who walks along the wire and must stay balanced
- Pole | box w=100 h=400 | colour=wireframe yellow | the vertical support that shows the player's lean
- Score Text | box w=200 h=40 | colour=wireframe white | displays the current score and progress
RULES:
- The player moves forward automatically when the up key is pressed, stepping one section of the wire at a time.
- Wind gusts appear periodically and push the player's lean, causing the wire to tip away from the gust direction.
- Pressing left or right adjusts the player's lean to counteract the wind gust's push.
- The score increases by 1 point for each successful step without falling.
- A fall costs one life, ending the current try.
- Each try has a fixed move count of 30 steps; using all moves ends the try.
WIN: The player reaches the final section of the wire with a positive score.
LOSE: A fall or using all 30 moves ends the try.
NUMBERS: player_speed=10, wind_speed=5, step_count=30, score_start=0, lives_start=3
RISK: Keeping the player's lean perfectly balanced against shifting wind gusts while maintaining smooth wire movement in real time.

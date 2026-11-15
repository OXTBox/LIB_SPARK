# Chalk Line
PITCH: You walk across the black top-down playground with arrows, drawing a chalk line behind you. Enclosing marbles inside your chalk loop is fun because it tests your timing and spatial awareness in a simple, focused arcade setting.
CONTROLS: Use the arrow keys to move your chalk line forward and backward across the screen.
OBJECTS:
- chalk line | box w=900 h=20 | colour=white | draws a continuous line behind the player as they move
- player | box w=20 h=20 | colour=white | follows the arrow key movements to walk across the playground
- marble | box w=15 h=15 | colour=white | sits inside the chalk loop to be enclosed
RULES:
- The chalk line moves exactly with your arrow key movements, leaving a continuous trail behind you.
- Walking over your own chalk line erases that section of the line.
- Enclose all marbles inside your chalk loop to complete the current level.
- Each successful level completion adds 100 to the score.
- Falling outside the screen boundary costs 1 life.
WIN: The score reaches 300 points to complete the game.
LOSE: Falling outside the screen boundary ends the try.
NUMBERS: player_speed=150, marble_speed=0, chalk_line_speed=150, lives=3, score=0
RISK: Keeping the chalk line trail accurate and ensuring marbles stay safely inside the loop without accidental erasure is the hardest part to program.

# Courier Run
PITCH: A tiny courier with a broken delivery bag must run through a city maze, dodging dogs while chasing missed parcels before the clock runs out.
FUN:
- TOY: Pressing the arrow keys moves the courier through the wireframe city streets, and the screen shows the courier as a bright wireframe box travelling along the streets.
- CHOICE: The player chooses between picking up a numbered parcel for a quick tip or saving time by skipping it, while also choosing whether to return a wrong parcel to the warehouse or sell it at the pawn shop.
- SURPRISE: Dogs appear from the city streets and chase the courier at unpredictable intervals, forcing the player to dodge through the maze.
- MOMENT: The player picks up a fast parcel, walks into its numbered door, and sees the tip coins and score appear on the screen as the delivery is confirmed.
- EXTRA: The player can walk into the pawn shop to sell unwanted parcels for extra points instead of returning them to the warehouse.
CONTROLS: Use the arrow keys to move the courier left, right, up, and down through the city streets.
OBJECTS:
- Courier | box w=20 h=20 | wireframe blue | the player who moves through the city maze
- Parcel | box w=15 h=15 | wireframe green | a numbered delivery item the player picks up for a tip
- Dog | box w=30 h=30 | wireframe red | a chasing animal that moves after the courier
- Door | box w=20 h=20 | wireframe yellow | a numbered door that confirms a parcel delivery and awards a tip
- Warehouse | box w=100 h=60 | wireframe grey | a location where the player returns wrong parcels for points
- Pawn Shop | box w=80 h=50 | wireframe orange | a location where the player sells unwanted parcels for extra points
RULES:
- The courier moves only with the arrow keys through the wireframe city streets.
- Picking up a numbered parcel and walking into its numbered door awards a tip score.
- Fast deliveries increase the tip score earned for the parcel.
- Each wrong parcel returned to the warehouse or sold at the pawn shop adds a few points to the score.
- Each time the courier is caught by a dog or the clock runs out, the player loses a life.
WIN: The player completes all numbered parcels before the clock runs out and reaches a high total score.
LOSE: The player is caught by a dog, falls behind the clock, or runs out of lives.
NUMBERS: courier_speed=120, parcel_speed=90, dog_speed=100, clock_speed=30, tip_coins=5, lives=3, parcels=5
RISK: Programming the dog chase AI to move unpredictably through the city maze while keeping the courier movement smooth and responsive on the keyboard.

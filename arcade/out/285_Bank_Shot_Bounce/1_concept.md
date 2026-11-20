# Bank Shot Bounce
PITCH: A tiny pool player with one pocketed ball and a sticky table must clear the numbered balls in order before the table gets worse and worse.

FUN:
- TOY: Drag back from the ball to aim, and the longer the drag, the harder the shot sends the ball.
- CHOICE: Choose a long drag for a powerful shot, or a short drag for a precise tap that risks missing the numbered balls.
- SURPRISE: Bumper balls and pockets that slide along the rails can send the ball in unexpected directions you did not predict.
- MOMENT: You release the long drag, the ball sails past the numbered balls and lands cleanly in the pocket, and you shout one more try.
- EXTRA: Use the extra keys to reset the table after a missed shot, or adjust the felt slickness before a level starts.

CONTROLS:
- Left and Right arrows: move the aiming pointer back and forth.
- Up arrow: release the shot with the chosen drag.

OBJECTS:
- Aim Pointer | box w=120 h=20 | colour=light grey | moves with the arrow keys to position the shot
- Ball | box w=20 h=20 | colour=white | the main ball that must be sunk in order
- Numbered Ball | box w=20 h=20 | colour=blue | the target balls that must be sunk in sequence for points
- Bumper | box w=40 h=40 | colour=orange | bounces the ball off its surface to change the shot path
- Pocket | box w=60 h=60 | colour=purple | catches the ball when it enters the pocket area
- Slick Felt | box w=900 h=600 | colour=light green | changes the ball movement speed based on its slickness

RULES:
- The main ball must be sunk before any numbered ball can be sunk.
- Sinking numbered balls in order earns one point each.
- Sinking your own main ball costs one life.
- Balls bounce off the cushions, bumpers, and each other automatically.
- Each level changes the table shape, adds bumpers, or alters the felt slickness.
- A level ends when all numbered balls are sunk in order.
- A life is lost when the main ball is sunk, ending the current level.

WIN: Sink all numbered balls in order to complete the level and earn the final score.
LOSE: Sink your own main ball, which costs one life and ends the current level.

NUMBERS:
- Aim Pointer speed=120 | Ball speed=250 | Numbered Ball speed=200 | Bumper speed=180 | Pocket speed=150 | Slick Felt speed=30

RISK: Programming the variable felt slickness and sliding pockets to keep the ball moving predictably without missing the numbered balls.

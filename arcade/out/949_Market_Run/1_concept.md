# Market Run
PITCH: Walk through a top-down street market on arrows to buy the required items in order before the market closes, and avoid the moving shoppers to score points. It is fun because it combines quick street navigation with a tight, time-driven shopping challenge.
CONTROLS: Arrows only. Walking into a stall buys the item, pushes items and presses switches.
OBJECTS:
- shopping list | box w=400 h=20 | colour #4A90E2 | holds the required items to buy in order before closing
- market stalls | box w=120 h=80 | colour #7B5EA0 | sells the listed items when walked into
- walking shoppers | box w=60 h=60 | colour #E04050 | move along the street and block the player's path
- score counter | box w=200 h=40 | colour #2E8B57 | shows the player's accumulated points
- market timer | box w=150 h=40 | colour #D9A02E | counts down the time before the market closes
RULES:
- The player moves with arrow keys through the market street.
- Items are bought by walking into the matching stall.
- Items must be bought in the exact order written on the shopping list.
- Moving shoppers block the player's path and cost one life.
- Each correctly bought item adds points to the score.
- The market closes when the timer reaches zero, ending the level.
WIN: Complete all items on the shopping list in order before the market closes to win the level.
LOSE: Bump into a walking shopper or let the market timer reach zero to lose a life.
NUMBERS: shopping list length=3, market speed=120, walker speed=80, score start=0, lives start=3, timer start=180, stall count=5
RISK: Programming the timed shopping list logic and collision detection with moving shoppers to prevent path blocking while enforcing strict item order.

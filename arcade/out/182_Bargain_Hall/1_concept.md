# Bargain Hall
PITCH: Walk between stalls in the top-down market hall, trading cheap items for better ones until you collect the gold key that opens the hall door. It is fun because every trade feels like a quick arcade bargain and the market closes on a timer for constant urgency.
CONTROLS: Use arrow keys to move, Space to trade with the current stall.
OBJECTS:
- GLAZE | box 900x600 | cyan | the player who walks between stalls and trades items
- STALL | box 200x150 | yellow | a market stall that wants one item and offers another
- CHEAP_ITEM | box 40x40 | green | the starting cheap item the player begins with
- GOLD_KEY | box 30x30 | gold | the final item that opens the hall door to complete the level
- CLOCK | box 100x60 | orange | a market timer that closes the trading area after a set time
RULES:
- GLAZE moves with arrow keys and trades with the nearest active stall using Space.
- Each trade gives the player the item the stall wants in exchange for the item the stall offers.
- The player scores points for each successful trade that upgrades their item value.
- Trading a high-value item costs one life if the player cannot afford the required trade.
- Stalls become inactive after trading once and disappear from the market.
- The clock counts down and closes the market, ending trading immediately when it reaches zero.
- Each level adds more stalls, single-use traders, and a shorter clock for increasing difficulty.
WIN: Collect the gold key from the final stall to open the hall door and complete the level.
LOSE: Lose all lives when a trade costs a life, or fail to collect the gold key before the clock closes.
NUMBERS: stalls=5, lives=3, clock_steps=120, trade_speed=1.5, stall_speed=0.8
RISK: Programming the dynamic stall trading logic and the clock-based market closure that changes active stalls and trading availability in real time.

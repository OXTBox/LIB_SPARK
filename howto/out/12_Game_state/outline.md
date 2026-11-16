# 12 Game state
Goal: a game shows a score and lives counter, updates them with the keysDown, and lets the player restart with Space.
Needs: 01, 04

1. Add score and lives HUD elements
   Adding: HUD.Set "Score", 0, 20, 120, 14, HUD.Set "Lives", 3, 20, 160, 14
   Makes this happen: the viewport shows a score of 0 and three lives below the engine's top bars.
   Engine calls: HUD.Set
2. Update score and lives each game step
   Adding: on Game.OnUpdate (read the keysDown, add 1 to the score when the right key is pressed, subtract 1 from the lives when the left key is pressed)
   Makes this happen: pressing the right key increases the score, pressing the left key decreases the lives, about 30 updates a second.
   Engine calls: Game.OnUpdate
3. Show win and lose states when conditions are met
   Adding: on Game.OnUpdate (if the score is at least 100, HUD.Set "WIN", 20, 120, 14; if the lives are at most 0, HUD.Set "LOSE", 20, 120, 14)
   Makes this happen: reaching a score of 100 shows a WIN message, running out of lives shows a LOSE message.
   Engine calls: Game.OnUpdate, HUD.Set
4. Restart the game with Space
   Adding: on Game.OnClick (if the Space key is pressed, reset the score to 0, the lives to 3, and remove the WIN and LOSE messages)
   Makes this happen: pressing Space clears the win and lose states and restarts the game with a fresh score and lives.
   Engine calls: Game.OnClick, HUD.Remove
5. Add a State function for notes and tests
   Adding: State function that returns the current score, lives, and win/lose status
   Makes this happen: the game can check its state values for notes and tests without reading the HUD each step.
   Engine calls: Game.OnUpdate

Pitfalls:
- Only Game.OnClick handles the mouse; use the keysDown inside Game.OnUpdate for keyboard input, or the state will never update.
- Resetting score and lives requires updating the HUD values immediately after the Space press, or the old win or lose messages will stay on screen.

Games that show it: Simple_Test1

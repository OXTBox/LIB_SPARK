# 12 Game state
Goal: A small 3D vector game shows a working score, lives, level indicator, and win/lose state with Space to restart.
Needs: none

1. Adding score and lives display
   Adding: Game.OnStart, HUD.Set
   Makes this happen: The game starts and shows a score value and lives count on the screen.
   Engine calls: Game.OnStart, HUD.Set

2. Adding level tracking
   Adding: Game.OnUpdate, HUD.Set
   Makes this happen: Each game update updates the level indicator on screen to reflect the current level.
   Engine calls: Game.OnUpdate, HUD.Set

3. Adding win and lose state detection
   Adding: Game.OnUpdate, HUD.Set
   Makes this happen: When the game reaches a win condition or lose condition, the screen updates to show the win or lose state.
   Engine calls: Game.OnUpdate, HUD.Set

4. Adding Space to restart play again
   Adding: Game.OnClick, HUD.Set
   Makes this happen: Pressing Space restarts the game and clears the current state display to show the initial game state.
   Engine calls: Game.OnClick, HUD.Set

5. Adding State function for notes and tests
   Adding: Game.OnStart, Game.OnUpdate, HUD.Set
   Makes this happen: The State function initializes the game state for notes and tests, updating the screen to show the correct state for the current test or note.
   Engine calls: Game.OnStart, Game.OnUpdate, HUD.Set

Pitfalls:
- Forgetting to clear the previous state display when restarting with Space will leave stale win or lose text on screen after a restart.
- Updating the State function only once at game start will not reflect changes to score, lives, or level during gameplay.

Games that show it: Simple_Test1, Simple_Test2, demo

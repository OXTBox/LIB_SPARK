# 17 Pause, notes and tests
Goal: the game pauses on Escape and shows a pause note on F2, while headless tests can drive the game with TestKeys and read its State.
Needs: 01, 04

1. A game with a loop that runs and can be paused
   Adding: Game.OnStart (with Engine.ResetCamera, Scene.ClearAll, HUD.Clear), Game.OnUpdate (add 0.05 to a script-local angle variable and call SetObjectRotation with it)
   Makes this happen: the game starts, the loop runs about 30 small turns per second, and pressing Escape pauses the game.
   Engine calls: Game.OnStart, Engine.ResetCamera, Scene.ClearAll, HUD.Clear, Game.OnUpdate, SetObjectRotation
2. A pause note on screen
   Adding: HUD.Set "Pause Note","PAUSE ON ESCAPE",20,120,14 in Game.OnStart
   Makes this happen: the pause note appears in the viewport when the game is paused, and disappears when the game resumes.
   Engine calls: HUD.Set
3. A test hook for headless driving
   Adding: Game.OnClick (read the keysDown variable for TestKeys input, call TestKeys.Drive if the TestKeys key is pressed)
   Makes this happen: headless tests can send TestKeys input to the game and trigger the same actions as the mouse and keyboard, without a user pressing a key.
   Engine calls: Game.OnClick, keysDown
4. A State variable for tests to read
   Adding: Game.OnStart (initialize a script-local State variable to 0)
   Makes this happen: headless tests can read the State variable to verify what the game did during a test run.
   Engine calls: Game.OnStart

Pitfalls:
- Only Game.OnClick reads the mouse and TestKeys input; never put the key check in Game.OnUpdate, or headless tests will never trigger the test actions.
- Keep the State variable in a script-local variable; a plain local in Game.OnStart resets every step and tests will read stale values.

Games that show it: Simple_Test1

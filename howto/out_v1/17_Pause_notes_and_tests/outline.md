# 17 Pause, notes and tests
Goal: A small 3D vector game that pauses with Escape, shows notes with F2, and runs headless tests that drive the game with TestKeys and read State.
Needs: none

1. Set up the game script foundation with pause, notes, and test hooks
   Adding: Game.OnStart, Game.OnUpdate, Game.OnClick, Game.OnKill, Game.OnPause, Game.OnNotes, TestKeys, State
   Makes this happen: The game script loads with handlers for starting, updating, clicking, killing, pausing, showing notes, and test key driving, so the game can pause, display notes, and run headless tests.
   Engine calls: Game.OnStart, Game.OnUpdate, Game.OnClick, Game.OnKill, Game.OnPause, Game.OnNotes, TestKeys, State

2. Implement the Escape pause handler to stop game updates
   Adding: Game.OnPause
   Makes this happen: Pressing Escape triggers the pause handler, which halts the game's normal updates so the scene freezes while the player can still interact with the pause state.
   Engine calls: Game.OnPause

3. Implement the F2 notes handler to display game notes on screen
   Adding: Game.OnNotes
   Makes this happen: Pressing F2 triggers the notes handler, which shows the game notes in the on-screen HUD so the learner can read the instructions and state information.
   Engine calls: Game.OnNotes, HUD.Set

4. Add the headless test driver that feeds TestKeys and reads State
   Adding: TestKeys, State
   Makes this happen: The test driver registers the TestKeys input source and State reader, enabling automated headless tests that drive the game with test keys and read the game's current state.
   Engine calls: TestKeys, State

5. Verify the pause, notes, and test functionality works end to end
   Adding: Game.OnStart, Game.OnUpdate, Game.OnClick, Game.OnKill, Game.OnPause, Game.OnNotes, TestKeys, State
   Makes this happen: Running the game with the test driver confirms that Escape pauses the game, F2 shows the notes, and TestKeys correctly drive the game while State reflects the current state.
   Engine calls: Game.OnStart, Game.OnUpdate, Game.OnClick, Game.OnKill, Game.OnPause, Game.OnNotes, TestKeys, State

Pitfalls:
- Forgetting to register the TestKeys input source will cause headless tests to have no input to drive the game, so tests will not progress even though the game runs normally.
- Adding the pause or notes handler without the corresponding Game.OnPause or Game.OnNotes hook will cause the handlers to be ignored, so Escape and F2 will have no effect.
- Using the wrong State reader or not reading it after driving the game with TestKeys will leave the test results empty, so the learner cannot verify the game's state changes.

Games that show it: Simple_Test1, Simple_Test2, demo

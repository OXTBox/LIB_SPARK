# 09 HUD and text
Goal: a working score line and help text appear on screen below the engine's top bars.
Needs: 01, 04

1. Clear the HUD before adding text
   Adding: HUD.Clear
   Makes this happen: the viewport shows no leftover score lines, messages, or help text, giving a clean slate for the new text.
   Engine calls: HUD.Clear
2. Add a score line at the top of the HUD
   Adding: HUD.Set "Score", "100", 20, 120, 14
   Makes this happen: a cyan score line showing 100 appears below the engine's top bars.
   Engine calls: HUD.Set
3. Add a help message below the score line
   Adding: HUD.Set "Help", "Click to move", 20, 140, 14
   Makes this happen: a help message showing "Click to move" appears below the score line, keeping text organized below the top bars.
   Engine calls: HUD.Set
4. Remove the score line when the game stops
   Adding: on Game.OnStop (HUD.Remove "Score")
   Makes this happen: press Stop, then Play another game: the old score line is gone and only the help message remains.
   Engine calls: Game.OnStop, HUD.Remove

Pitfalls:
- HUD.Set only places text on screen; nothing appears until the call is made, so a missing HUD.Set leaves no visible text.
- Do not add the same HUD.Set call twice as a separate step; each step must add a new type of text (score line, message, help text) to show a new result.

Games that show it: Simple_Test1

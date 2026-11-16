# 09 HUD and text
Goal: A working HUD with a score line, a message, and help text displayed below the top bars on screen.
Needs: none

1. Setting up the HUD base layer
   Adding: HUD.Set
   Makes this happen: A blank HUD layer is created and placed below the top bars so it can hold score lines, messages, and help text.
   Engine calls: HUD.Set

2. Adding the score line
   Adding: HUD.Set
   Makes this happen: A score line is added to the HUD layer and appears at the top of the display area.
   Engine calls: HUD.Set

3. Adding the message text
   Adding: HUD.Set
   Makes this happen: A message text is added to the HUD layer and appears below the score line.
   Engine calls: HUD.Set

4. Adding the help text
   Adding: HUD.Set
   Makes this happen: Help text is added to the HUD layer and appears below the message text, keeping all HUD content below the top bars.
   Engine calls: HUD.Set

5. Clearing the HUD layer to reset it
   Adding: HUD.Clear
   Makes this happen: The HUD layer is cleared so all previously added score lines, messages, and help text are removed, leaving a clean HUD ready for new content.
   Engine calls: HUD.Clear

Pitfalls:
- Adding HUD content above the top bars: This places text in the wrong area and makes the score line, message, or help text overlap with the top bars instead of staying below them.
- Forgetting to clear the HUD layer after adding content: This leaves stale score lines, messages, or help text from earlier steps visible, confusing the learner about what the current game state shows.

Games that show it: Simple_Test1, demo, VectorBlobApocalypse

Wait, let me check the requirements. The format must be EXACTLY this format and nothing else. Let me recount steps: 5 steps, which is between 4 and 7. Good.

Wait, step 5 is clearing the HUD layer. But the topic covers HUD.Set, HUD.Remove, HUD.Clear. Oh right, I forgot HUD.Remove. Let me adjust to include HUD.Remove. Let me make 6 steps? Or adjust step 5 to use HUD.Remove and HUD.Clear? Wait, let's see: the topic covers HUD.Set, HUD.Remove, HUD.Clear. So I need to include HUD.Remove somewhere.

Let me revise:

1. Setting up the HUD base layer
   Adding: HUD.Set
   Makes this happen: A blank HUD layer is created and placed below the top bars so it can hold score lines, messages, and help text.
   Engine calls: HUD.Set

2. Adding the score line
   Adding: HUD.Set
   Makes this happen: A score line is added to the HUD layer and appears at the top of the display area.
   Engine calls: HUD.Set

3. Adding the message text
   Adding: HUD.Set
   Makes this happen: A message text is added to the HUD layer and appears below the score line.
   Engine calls: HUD.Set

4. Adding the help text
   Adding: HUD.Set
   Makes this happen: Help text is added to the HUD layer and appears below the message text, keeping all HUD content below the top bars.
   Engine calls: HUD.Set

5. Removing the help text to demonstrate HUD.Remove
   Adding: HUD.Remove
   Makes this happen: The help text is removed from the HUD layer, showing that HUD content can be taken away from the display area.
   Engine calls: HUD.Remove

6. Clearing the HUD layer to reset it
   Adding: HUD.Clear
   Makes this happen: The HUD layer is cleared so all remaining HUD content is removed, leaving a clean HUD ready for new content.
   Engine calls: HUD.Clear

That's

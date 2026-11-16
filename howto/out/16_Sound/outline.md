# 16 Sound
Goal: a sound plays when the player presses the mouse to trigger an event, with no leftover visual changes after the game stops.
Needs: 01, 04

1. Set up the game card to run with sound support
   Adding: Game.OnStart, Audio.Init
   Makes this happen: the game card initializes audio and starts running, so a sound can be triggered when an event occurs.
   Engine calls: Game.OnStart, Audio.Init
2. Add a trigger object that the player can interact with
   Adding: Mesh.Define "TriggerCube", MeshBox(30,30,30), Entity.Spawn("TriggerCube",0,0,0,"orange")
   Makes this happen: an orange wire cube sits in the middle of the view, ready to be triggered by the player.
   Engine calls: Mesh.Define, MeshBox, Entity.Spawn
3. Play the sound when the player clicks the trigger object
   Adding: Game.OnClick, Sound.Play
   Makes this happen: pressing the mouse on the orange cube triggers the sound, which the learner can hear immediately.
   Engine calls: Game.OnClick, Sound.Play
4. Clear the sound and any leftover state when the game stops
   Adding: Game.OnStop, Audio.Init
   Makes this happen: pressing Stop stops the game and resets audio, so playing another game starts cleanly with no stale sound state.
   Engine calls: Game.OnStop, Audio.Init

Pitfalls:
- Audio.Init must be called in Game.OnStart before any Sound.Play call, otherwise the sound will not play when the game starts.
- Do not put Sound.Play inside Game.OnUpdate as a new step; only trigger it from Game.OnClick so the sound happens when the player acts, not every frame.

Games that show it: Simple_Test1

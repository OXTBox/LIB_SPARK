# 16 Sound
Goal: A small working 3D vector game that plays a sound when an event occurs on screen.
Needs: none

1. Initialize audio for the game
   Adding: Audio.Init
   Makes this happen: Audio is ready to play sounds for the game.
   Engine calls: Audio.Init
2. Add a clickable object to the scene
   Adding: Entity.Spawn
   Makes this happen: A new object appears in the 3D scene that can be clicked.
   Engine calls: Entity.Spawn
3. Create a sound event handler for clicks
   Adding: Game.OnClick
   Makes this happen: The game now responds to clicks on the scene object.
   Engine calls: Game.OnClick
4. Play a sound when the object is clicked
   Adding: Sound.Play
   Makes this happen: A sound plays each time the scene object is clicked, showing the sound event works.
   Engine calls: Game.OnClick, Sound.Play

Pitfalls:
- Forgetting to initialize Audio before playing sounds will cause the sound to fail to play, so always add the Audio.Init step first.
- Adding Sound.Play without a click handler will not trigger the sound when an event occurs, so ensure a Game.OnClick handler is in place before playing the sound.

Games that show it: Simple_Test1, demo, VectorPong3D

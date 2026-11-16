# 11 Effects
Goal: A visible particle effect appears on screen after a trigger event, showing feedback from an action.
Needs: none

1. Initializing the effects system and clearing existing particles
   Adding: FX.Sparks, Particles.Clear
   Makes this happen: All existing particles on the screen are removed, leaving a clean scene for the new effect.
   Engine calls: FX.Sparks, Particles.Clear
2. Spawning a small particle effect to demonstrate feedback
   Adding: FX.Sparks
   Makes this happen: A small burst of particles appears on the screen, showing the effects system is active.
   Engine calls: FX.Sparks
3. Triggering the particle effect with a simple event to confirm it responds to input
   Adding: Game.OnClick
   Makes this happen: Clicking the scene causes the particle effect to activate, showing feedback when an action happens.
   Engine calls: Game.OnClick
4. Removing the particle effect after the feedback is shown to keep the scene clean
   Adding: FX.Derez
   Makes this happen: The particle effect disappears once the feedback is displayed, returning the scene to a clean state.
   Engine calls: FX.Derez

Pitfalls:
- Forgetting to clear existing particles before spawning a new effect can cause overlapping or cluttered particle displays that make the effect hard to see.
- Triggering the effect without a corresponding input event means the feedback never appears, so the learner cannot see the effect working.

Games that show it: VectorBlobApocalypse, WallBreaker, demo

# 18 One game, two engines
Goal: a single small 3D vector game that runs identically and works in both the Vibecode3D and xt3d engines
Needs: none

1. Create a minimal working 3D vector game card script
   Adding: Game.OnStart, Scene.ClearAll, Mesh.New, MeshBox, Entity.Spawn, SetObjectPosition
   Makes this happen: a simple 3D vector shape appears on screen with a single positioned object in the scene
   Engine calls: Game.OnStart, Scene.ClearAll, Mesh.New, MeshBox, Entity.Spawn, SetObjectPosition
2. Add a simple update loop to animate the object
   Adding: Game.OnUpdate
   Makes this happen: the object moves along a simple path, showing the game runs continuously in both engines
   Engine calls: Game.OnUpdate
3. Add a click handler to interact with the object
   Adding: Game.OnClick, ScreenToCameraRay, RayCastScene
   Makes this happen: clicking the object triggers a visible interaction effect in both engines
   Engine calls: Game.OnClick, ScreenToCameraRay, RayCastScene
4. Add a collision rule to make the interaction respond to contact
   Adding: Collision.SetGroup, Collision.AddRule
   Makes this happen: the object now reacts to collisions, completing the small working result
   Engine calls: Collision.SetGroup, Collision.AddRule
5. Verify the script runs in both engines with the same simple setup
   Adding: Engine.ResetCamera, Engine.Info
   Makes this happen: the same card script runs successfully in the Vibecode3D and xt3d engines without engine-specific changes
   Engine calls: Engine.ResetCamera, Engine.Info

Pitfalls:
- Adding engine-specific calls or engine-only features in the script: this breaks the requirement that the same script runs in both engines, so remove any engine-specific calls and keep only engine-agnostic setup
- Adding multiple complex features in one step: beginners will not see a clear result after each step, so only add the smallest change needed to complete the current step

Games that show it: Simple_Test1, demo, VectorPong3D

Wait, let me check the format exactly. The user said "Use EXACTLY this format and nothing else". Let me make sure the structure matches:

# 18 One game, two engines
Goal: <one sentence...>
Needs: <...>

1. <step title>
   Adding: <...>
   Makes this happen: <...>
   Engine calls: <...>
2. ...

Pitfalls:
- ...
- ...

Games that show it: <...>

Let me adjust to make sure it's exactly that. Also check engine calls are from the list. Let's verify each:

Step 1: Game.OnStart (card hook, yes), Scene.ClearAll (setup, yes), Mesh.New (shapes, yes), MeshBox (shapes, yes), Entity.Spawn (objects, yes), SetObjectPosition (objects, yes). Good.

Step 2: Game.OnUpdate (card hook, yes). Good.

Step 3: Game.OnClick (card hook, yes), ScreenToCameraRay (input, yes), RayCastScene (input, yes). Good.

Step 4: Collision.SetGroup (collisions, yes), Collision.AddRule (collisions, yes). Good.

Step 5: Engine.ResetCamera (setup, yes), Engine.Info (setup, yes). Good.

Wait, the topic is about same script in two engines, so step 5 is verifying both run. That's fine, 5 steps which is between 4 and 7.

Needs: none, correct since it builds on nothing.

Goal: one sentence: "a single small 3D vector game that runs identically and works in both the Vibecode3D and xt3d engines" - that's one sentence, good.

Pitfalls: two, each one common mistake and how to spot. First: adding engine-specific calls/features in the script, which breaks the

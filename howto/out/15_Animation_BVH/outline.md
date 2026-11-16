# 15 Animation: BVH

Goal: a mesh animates with a BVH motion capture clip, showing walking and idle poses with feet that do not skate.

Needs: 01, 04

1. A game card with the motion capture library loaded
   Adding: Game.OnStart, LIB_MOCAP joints, LIB_MOCAP edges, LIB_MOCAP one line of numbers a frame
   Makes this happen: the motion capture stick clips are loaded and ready to be used in the game.
   Engine calls: Game.OnStart
2. A mesh to animate with BVH motion
   Adding: Mesh.Define "Mesh", MeshBox(40,40,40), Entity.Spawn("Mesh",0,0,0,"blue") in Game.OnStart
   Makes this happen: a blue wire cube is placed in the scene so the motion capture clip can drive its pose.
   Engine calls: Mesh.Define, MeshBox, Entity.Spawn
3. Load the BVH motion capture clip
   Adding: LIB_MOCAP load clip in Game.OnStart
   Makes this happen: the BVH motion capture clip is loaded and ready to drive the mesh's animation.
   Engine calls: Game.OnStart
4. Animate the mesh one frame per update with the BVH clip
   Adding: Game.OnUpdate, LIB_MOCAP one mesh a frame
   Makes this happen: the mesh follows the BVH motion capture clip, updating its pose at about 30 frames per second.
   Engine calls: Game.OnUpdate
5. Show walking and idle poses from the clip
   Adding: LIB_MOCAP walk pose, LIB_MOCAP idle pose in Game.OnUpdate
   Makes this happen: the mesh displays the walking and idle poses from the clip, showing the motion capture animation.
   Engine calls: Game.OnUpdate
6. Ensure the feet do not skate during animation
   Adding: LIB_MOCAP feet no skate in Game.OnUpdate
   Makes this happen: the mesh's feet stay in place during the BVH animation, preventing the feet from sliding or skating.
   Engine calls: Game.OnUpdate

Pitfalls:
- Mesh.Define only names a shape; nothing shows until Entity.Spawn puts it in the scene, so the mesh must be spawned before the animation steps run.
- The BVH motion capture clip must be loaded before the mesh is animated, otherwise the mesh will have no pose to follow and may show a blank or stuck frame.

Games that show it: Simple_Test1

# 15 Animation: BVH
Goal: A single mesh that animates frame-by-frame using a loaded BVH motion capture stick clip with walking and idle poses and stable non-skating feet.
Needs: none

1. Load the BVH motion capture stick clip
   Adding: LIB_MOCAP
   Makes this happen: The motion capture library is attached so the stick clip can be loaded into the scene for animation.
   Engine calls: LIB_MOCAP

2. Load the BVH stick clip into the scene
   Adding: LIB_MOCAP
   Makes this happen: The motion capture stick clip is loaded from the text file, making the animation data available for frame-based mesh updates.
   Engine calls: LIB_MOCAP

3. Create the mesh to animate
   Adding: Mesh.New
   Makes this happen: A new mesh is added to the scene so the motion capture data can be applied to it for animation.
   Engine calls: Mesh.New

4. Apply the BVH clip to the mesh for frame-based animation
   Adding: LIB_MOCAP
   Makes this happen: The loaded BVH motion capture clip is bound to the mesh, enabling one mesh to update its pose with each animation frame.
   Engine calls: LIB_MOCAP

5. Configure the mesh to walk and idle with stable feet
   Adding: Scene.SetBob
   Makes this happen: The mesh's animation behavior is set to walk and idle poses, with the feet configured so they do not skate during motion.
   Engine calls: Scene.SetBob

6. Update the mesh each frame to apply the BVH animation
   Adding: Game.OnUpdate
   Makes this happen: The scene runs each update cycle, applying the loaded BVH clip to the mesh so the walking and idle animation plays continuously.
   Engine calls: Game.OnUpdate

Pitfalls:
- Forgetting to load the LIB_MOCAP library before loading the clip will cause the clip to fail to load, leaving the mesh with no animation.
- Applying the clip to the mesh without setting the walk and idle pose behavior will result in the mesh only playing a single default pose instead of walking and idle states.
- Allowing the feet to use default skating motion will cause the feet to slide during the animation, so the feet must be explicitly configured to avoid skating.

Games that show it: demo:

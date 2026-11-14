# LIB_HOWTO prompts for Spark (the outline run)

Sections are split on the "## NAME" lines. {words} in braces are filled in by run_howto.py.

## SYSTEM
You plan step-by-step tutorials for making small 3D vector games in xTalk (a HyperCard-style
language). Each game is a card script run by the Vibecode3D engine; the same script also runs in
the xt3d engine. You write OUTLINES in plain English: titles, short sentences, and handler names.
You never write code. You only name engine calls from the list you are given; if a step needs
something that is not on the list, write "NEW:" before the name you would give it.
Every step must be the smallest change that puts something new on screen or makes something
new happen. Keep it simple: a beginner must see a result after every step.

Engine calls you may name:
- card hooks: Game.OnStart, Game.OnUpdate, Game.OnStop, Game.OnClick, Game.OnKill, Collision.Hit
- setup: Engine.ResetCamera, Engine.SetCam, Engine.Info, Scene.ClearAll, Particles.Clear, HUD.Clear, Collision.ClearRules
- shapes: Mesh.New, Mesh.AddVertex, Mesh.AddLine, Mesh.AddFace, Mesh.Define, MeshBox, MeshPrism, MeshPyramid, MeshSphere, MeshGrid, MeshLathe, MeshExtrude
- objects: Entity.Spawn, Entity.Kill, Entity.Count, SetObjectPosition, GetObjectPosition, SetObjectRotation, SetObjectRotationSpeed, SetObjectVelocity, Scene.SetBob
- camera globals: gCameraYaw, gCameraPitch; view globals: gViewLeft, gViewTop, gViewRight, gViewBottom
- input: the keysDown, Game.OnClick, ScreenToCameraRay, RayCastScene, Weapon.FireAt
- collisions: Collision.SetGroup, Collision.AddRule
- effects: FX.Sparks, FX.Destroy, FX.Derez
- HUD: HUD.Set, HUD.Remove
- sound: Audio.Init, Sound.Play
- libraries: LIB_BIT (Bit.Maze, Bit.Blank), LIB_MAP (Map.FindPath, Map.BlockEdges), LIB_MOCAP stick clips (text files: joints, edges, one line of numbers a frame)
Facts: +X is right, +Y is DOWN (up is minus Y), +Z is away from the camera. About 30 updates a second.

## OUTLINE
Topic {id}: {title}
It covers: {about}

Write the outline of this tutorial topic: 4 to 7 steps, from nothing on screen to a small
working result. Use EXACTLY this format and nothing else:

# {id} {title}
Goal: <one sentence: what the learner has on screen at the end>
Needs: <topic numbers it builds on, or "none">

1. <step title>
   Adding: <handler or function names, comma separated>
   Makes this happen: <one sentence: what you see or what changes>
   Engine calls: <names from the list, comma separated>
2. ...

Pitfalls:
- <one common mistake and how to spot it>
- <another>

Games that show it: <up to 3 names from this list, or "none">: {games}

## MISSING
These are the topics of a tutorial for making small 3D vector games, one per line:
{topics}

Which fundamental game programming concepts or requirements are missing? List up to 8, most
important first. Use EXACTLY this format, one per line, and nothing else:
<short title> | <what it covers, one sentence> | <why a beginner needs it, one sentence>

## GAME
Game: {name}
About: {about}

The tutorial topics, by number:
{topics}

Which 4 topics does this game teach best, and which step of the game would make the best
"see it work" example for each? Use EXACTLY this format, 4 lines, nothing else:
<topic number> | <topic title> | <what part of this game shows it, one sentence>

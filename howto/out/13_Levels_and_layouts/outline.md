# 13 Levels and layouts
Goal: a repeatable-seeded maze grid appears on screen as a working level layout.
Needs: 01, 04

1. A seeded level table
   Adding: LIB_BIT.Bit.Maze, LIB_MAP.Map.FindPath
   Makes this happen: the level table is loaded with a fixed seed so the maze layout is the same every time the game runs.
   Engine calls: LIB_BIT.Bit.Maze, LIB_MAP.Map.FindPath
2. A level grid on screen
   Adding: Mesh.Define "Grid", MeshGrid(40,40,40), Entity.Spawn("Grid",0,0,0,"gray")
   Makes this happen: a gray grid fills the view, showing the level layout the seeded maze defines.
   Engine calls: Mesh.Define, MeshGrid, Entity.Spawn
3. A maze path on the grid
   Adding: LIB_BIT.Bit.Maze, LIB_MAP.Map.FindPath
   Makes this happen: the maze path from the seeded table is drawn as a visible path on the grid, showing the working level layout.
   Engine calls: LIB_BIT.Bit.Maze, LIB_MAP.Map.FindPath
4. A repeatable layout check
   Adding: LIB_BIT.Bit.Maze, LIB_MAP.Map.FindPath
   Makes this happen: the same seed produces the identical maze layout every time, so the level is repeatable.
   Engine calls: LIB_BIT.Bit.Maze, LIB_MAP.Map.FindPath

Pitfalls:
- A library function only defines or loads the maze data; nothing shows until Entity.Spawn puts the grid shape into the scene.
- Reusing the same maze seed without changing the seed will repeat the exact same layout, so always keep the seed fixed for repeatable levels.

Games that show it: DotMaze, PromptAndGlazeMaze, Simple_Test1

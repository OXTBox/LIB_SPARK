# 13 Levels and layouts
Goal: A repeatable, seeded level table displaying a small grid maze on screen.
Needs: none

1. Setting up the level table
   Adding: Game.OnStart
   Makes this happen: The game starts and a blank level table is initialized on screen with no levels loaded yet.
   Engine calls: Game.OnStart

2. Adding the first level to the table
   Adding: Game.OnStart
   Makes this happen: The first level is added to the level table so the table now contains one level entry.
   Engine calls: Game.OnStart

3. Creating a seeded random level layout
   Adding: LIB_BIT, LIB_MAP
   Makes this happen: A repeatable random seed is used to generate a small grid maze layout that is added to the level table.
   Engine calls: LIB_BIT, LIB_MAP

4. Loading the generated layout into the scene
   Adding: Scene.ClearAll, MeshGrid
   Makes this happen: The generated maze layout is cleared from the scene and a new grid maze shape is added to the scene so the maze appears on screen.
   Engine calls: Scene.ClearAll, MeshGrid

5. Applying the level layout to the current scene
   Adding: Game.OnUpdate
   Makes this happen: The level layout is applied to the current scene so the grid maze remains visible and updates correctly as the game runs.
   Engine calls: Game.OnUpdate

Pitfalls:
- Using a random seed without a fixed value each time will cause the maze layout to change every run, so always pair the seed with a repeatable seed setup to keep the layout consistent.
- Adding a level to the table without generating its layout first will leave the table with an empty entry, so generate the layout before adding it to the table.

Games that show it: DotMaze, PromptAndGlazeMaze, demo

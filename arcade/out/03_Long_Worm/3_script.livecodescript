######################################################################################
## CARD SCRIPT: "Long Worm"  LONG WORM
## A worm moves on a grid. Turn with arrows, Space to move forward.
## Eat food to grow. Hitting walls or its own body costs a life.
## CONTROLS  Left/Right arrows: turn the worm    Up/Down arrows: move forward
## RULES     Each step scores 10; eating food grows the worm by one cell; 3 lives
##          lost means the game ends. Reach the highest level to win.
######################################################################################

global gWormX, gWormY, gWormDX, gWormDY, gWormLen, gWormDir, gWormSegs, gWormSegX, gWormSegY, gWormLives, gWormScore, gWormLevel, gWormOver

local sWormX, sWormY, sWormDX, sWormDY, sWormLen, sWormDir, sWormSegs, sWormSegX, sWormSegY, sWormLives, sWormScore, sWormLevel, sWormOver

constant kZ = 600          -- every object sits at this depth
constant kLeft = -450      -- playfield edges (world units; +Y is DOWN)
constant kRight = 450
constant kTop = -300
constant kBottom = 300
constant kCellW = 10
constant kCellH = 5
constant kSpeed = 1.5
constant kFoodSpeed = 0.5
constant kScorePerStep = 10
constant kMaxLives = 3
constant kGridW = 900
constant kGridH = 600

on Game.OnStart
   Engine.ResetCamera
   Scene.ClearAll
   Particles.Clear
   HUD.Clear
   Collision.ClearRules
   Mesh.Define "Worm.Worm", MeshBox(kCellW, kCellH, 16)
   Mesh.Define "Worm.Food", MeshBox(4, 4, 16)
   Mesh.Define "Worm.Wall", MeshBox(kGridW, kGridH, 16)
   Mesh.Define "Worm.Body", MeshBox(kCellW, kCellH, 16)
   put 0 into sWormX
   put 0 into sWormY
   put 0 into sWormDX
   put 0 into sWormDY
   put 3 into sWormLen
   put 0 into sWormDir
   put 0 into sWormSegs
   put 0 into sWormScore
   put 1 into sWormLevel
   put kMaxLives into sWormLives
   put false into sWormOver
   put Entity.Spawn("Worm.Worm", sWormX, sWormY, kZ, "green") into gWormX
   put Entity.Spawn("Worm.Food", 0, 0, kZ, "orange") into gWormFood
   put Entity.Spawn("Worm.Wall", 0, 0, kZ, "grey") into gWormWall
   Worm.StartLevel 1
end Game.OnStart

on Game.OnUpdate
   if sWormOver then exit Game.OnUpdate
   put the keysDown into tKeys
   if 65361 is among the items of tKeys then
      multiply sWormDX by -1
   end if
   if 65363 is among the items of tKeys then
      multiply sWormDX by -1
   end if
   if 65362 is among the items of tKeys then
      multiply sWormDY by -1
   end if
   if 65364 is among the items of tKeys then
      multiply sWormDY by -1
   end if
   if 65363 is among the items of tKeys then
      add kSpeed to sWormDX
   end if
   if 65361 is among the items of tKeys then
      subtract kSpeed from sWormDX
   end if
   if 65362 is among the items of tKeys then
      add kSpeed to sWormDY
   end if
   if 65364 is among the items of tKeys then
      subtract kSpeed from sWormDY
   end if
   if abs(sWormDX) < 0.1 then
      put 1 into sWormDX
   end if
   if abs(sWormDY) < 0.1 then
      put 1 into sWormDY
   end if
   if sWormDX = 1 then
      put 0 into sWormDY
   end if
   if sWormDY = 1 then
      put 0 into sWormDX
   end if
   if sWormDX = -1 then
      put 0 into sWormDY
   end if
   if sWormDY = -1 then
      put 0 into sWormDX
   end if
   add kSpeed to sWormX
   add kSpeed to sWormY
   SetObjectPosition gWormX, sWormX, sWormY, kZ
   if sWormLen > 3 then
      put sWormX into sWormSegX
      put sWormY into sWormSegY
      add 1 to sWormSegs
   end if
   if sWormLen > 4 then
      SetObjectPosition gWormSegs, sWormSegX, sWormSegY, kZ
   end if
   if sWormLen > 5 then
      SetObjectPosition gWormSegs, sWormSegX, sWormSegY, kZ
   end if
   if sWormLen > 6 then
      SetObjectPosition gWormSegs, sWormSegX, sWormSegY, kZ
   end if
   if sWormLen > 7 then
      SetObjectPosition gWormSegs, sWormSegX, sWormSegY, kZ
   end if
   if sWormLen > 8 then
      SetObjectPosition gWormSegs, sWormSegX, sWormSegY, kZ
   end if
   if sWormLen > 9 then
      SetObjectPosition gWormSegs, sWormSegX, sWormSegY, kZ
   end if
   if sWormLen > 10 then
      SetObjectPosition gWormSegs, sWormSegX, sWormSegY, kZ
   end if
   if sWormLen > 11 then
      SetObjectPosition gWormSegs, sWormSegX, sWormSegY, kZ
   end if
   if sWormLen > 12 then
      SetObjectPosition gWormSegs, sWormSegX, sWormSegY, kZ
   end if
   if sWormLen > 13 then
      SetObjectPosition gWormSegs, sWormSegX, sWormSegY, kZ
   end if
   if sWormLen > 14 then
      SetObjectPosition gWormSegs, sWormSegX, sWormSegY, kZ
   end if
   if sWormLen > 15 then
      SetObjectPosition gWormSegs, sWormSegX, sWormSegY, kZ
   end if
   if sWormLen > 16 then
      SetObjectPosition gWormSegs, sWormSegX, sWormSegY, kZ
   end if
   add kScorePerStep to sWormScore
   Worm.ShowHUD
end Game.OnUpdate

on Worm.StartLevel pLevel
   put 0 into sWormX
   put 0 into sWormY
   put 0 into sWormDX
   put 0 into sWormDY
   put 3 into sWormLen
   put 0 into sWormDir
   put 0 into sWormSegs
   put 0 into sWormSegX
   put 0 into sWormSegY
   put 0 into sWormScore
   put pLevel into sWormLevel
   put kMaxLives into sWormLives
   put false into sWormOver
   if pLevel = 1 then
      put 1 into sWormLevel
   end if
   if pLevel = 2 then
      put 2 into sWormLevel
   end if
   if pLevel = 3 then
      put 3 into sWormLevel
   end if
   if pLevel = 4 then
      put 4 into sWormLevel
   end if
   if pLevel = 5 then
      put 5 into sWormLevel
   end if
   put Entity.Spawn("Worm.Worm", sWormX, sWormY, kZ, "green") into gWormX
   put Entity.Spawn("Worm.Food", 0, 0, kZ, "orange") into gWormFood
   put Entity.Spawn("Worm.Wall", 0, 0, kZ, "grey") into gWormWall
   Worm.ShowHUD
end Worm.StartLevel

on Worm.ShowHUD
   HUD.Set "Worm.Level", "LEVEL" && sWormLevel, 20, 20, 14
   HUD.Set "Worm.Score", "SCORE" && sWormScore, 20, 40, 14
   HUD.Set "Worm.Lives", "LIVES" && sWormLives, 20, 60, 14
end Worm.ShowHUD

on Game.OnStop
   HUD.Remove "Worm.Level"
   HUD.Remove "Worm.Score"
   HUD.Remove "Worm.Lives"
end Game.OnStop

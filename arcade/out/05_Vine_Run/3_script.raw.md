```
######################################################################################
## CARD SCRIPT: "Vine.Run"   VINE RUN
## A player runs right across a jungle floor while dodging pits, logs and water.
## CONTROLS  Arrow keys: move right and jump/swing    Space: jump or swing
## RULES     Collect treasure = +10 score; pit or hazard = lose a life;
##           Reach the right edge with lives left to win.
######################################################################################

global gFloorX, gFloorY, gPlayerX, gPlayerY, gLives, gScore, gLevel, gFloorSpeed, gHazards
global gVineActive, gVineAngle, gVineT

local sFloorX, sFloorY, sPlayerX, sPlayerY, sLives, sScore, sLevel, sFloorSpeed, sHazards
local sVineActive, sVineAngle, sVineT, sOver

constant kZ = 600          -- every object sits at this depth
constant kLeft = -450      -- playfield edges (world units; +Y is DOWN)
constant kRight = 450
constant kTop = -300
constant kBottom = 300
constant kPlayerSpeed = 14
constant kVineSpeed = 3
constant kHazardWidth = 60

on Game.OnStart
   Engine.ResetCamera
   Scene.ClearAll
   Particles.Clear
   HUD.Clear
   Collision.ClearRules
   Mesh.Define "Vine.Floor", MeshBox(900, 600, 16)
   Mesh.Define "Vine.Pit", MeshBox(120, 40, 16)
   Mesh.Define "Vine.Log", MeshBox(80, 60, 16)
   Mesh.Define "Vine.Vine", MeshBox(40, 120, 16)
   Mesh.Define "Vine.Treasure", MeshBox(30, 30, 16)
   put 0 into sFloorX
   put kBottom into sFloorY
   put 0 into sPlayerX
   put kBottom into sPlayerY
   put 3 into sLives
   put 0 into sScore
   put 1 into sLevel
   put 120 into sFloorSpeed
   put 0 into sHazards
   put false into sVineActive
   put 0 into sVineAngle
   put 0 into sVineT
   put false into sOver
   put Entity.Spawn("Vine.Floor", 0, kBottom, kZ, "green") into gFloorX
   put Entity.Spawn("Vine.Pit", 0, kBottom, kZ, "red") into gHazards
   Vine.StartLevel 1
   Vine.ShowHUD
end Game.OnStart

on Game.OnUpdate
   if sOver then exit Game.OnUpdate
   put the keysDown into tKeys
   if 65361 is among the items of tKeys then subtract kPlayerSpeed from sPlayerX
   if 65363 is among the items of tKeys then add kPlayerSpeed to sPlayerX
   if 65362 is among the items of tKeys then add 1 to sVineT
   if sVineActive then
      add kVineSpeed to sVineAngle
      if sVineAngle >= 6.2831853 then
         multiply sVineAngle by -1
      end if
   end if
   put max(kLeft, min(kRight, sPlayerX)) into sPlayerX
   SetObjectPosition sPlayerX, sPlayerX, sPlayerY, kZ
   add sFloorSpeed to sFloorX
   SetObjectPosition sFloorX, sFloorX, sFloorY, kZ
   if sVineActive then
      SetObjectPosition gVineActive, sPlayerX, sPlayerY, kZ
   end if
   if sVineActive then
      if sVineT >= 1.5 then
         Vine.EndSwing
      end if
   end if
   Vine.CheckHazards
   Vine.CollectTreasures
   Vine.ShowHUD
end Game.OnUpdate

on Vine.StartLevel pLevel
   put pLevel into sLevel
   put 0 into sHazards
   put 0 into sVineActive
   put 0 into sVineAngle
   put 0 into sVineT
   put 120 into sFloorSpeed
   if pLevel = 1 then
      put 1 into sHazards[1]
      put 1 into sHazards[2]
   end if
   if pLevel = 2 then
      put 2 into sHazards[1]
      put 2 into sHazards[2]
      put 1 into sHazards[3]
   end if
   if pLevel = 3 then
      put 2 into sHazards[1]
      put 3 into sHazards[2]
      put 3 into sHazards[3]
   end if
   if pLevel = 4 then
      put 2 into sHazards[1]
      put 3 into sHazards[2]
      put 3 into sHazards[3]
      put 1 into sHazards[4]
   end if
   if pLevel = 5 then
      put 3 into sHazards[1]
      put 3 into sHazards[2]
      put 4 into sHazards[3]
      put 4 into sHazards[4]
      put 1 into sHazards[5]
   end if
end Vine.StartLevel

on Vine.ShowHUD
   HUD.Set "Vine.Score", "SCORE" && sScore, 20, 20, 14
   HUD.Set "Vine.Lives", "LIVES" && sLives, 20, 40, 14
   HUD.Set "Vine.Level", "LEVEL" && sLevel, 20, 60, 14
end Vine.ShowHUD

on Vine.CheckHazards
   if sLives <= 0 then
      put true into sOver
      HUD.Set "Vine.Over", "GAME OVER", 300, 200, 24
   end if
   for i = 1 to sHazards[1]
      if abs(sPlayerX - sHazards[i]) <= kHazardWidth then
         subtract 1 from sLives
         if sLives <= 0 then
            put true into sOver
            HUD.Set "Vine.Over", "GAME OVER", 300, 200, 24
         end if
         put 0 into sVineActive
         put 0 into sVineAngle
         put 0 into sVineT
      end if
   end for
end Vine.CheckHazards

on Vine.CollectTreasures
   if sVineActive then
      put false into sVineActive
      put 0 into sVineAngle
      put 0 into sVineT
   end if
   if abs(sPlayerX - 450) <= 30 then
      add 10 to sScore
   end if
end Vine.CollectTreasures

on Vine.EndSwing
   put false into sVineActive
end Vine.EndSwing

on Game.OnStop
   HUD.Remove "Vine.Score"
   HUD.Remove "Vine.Lives"
   HUD.Remove "Vine.Level"
   HUD.Remove "Vine.Over"
end Game.OnStop
```

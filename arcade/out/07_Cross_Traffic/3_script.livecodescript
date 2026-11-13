######################################################################################
## CARD SCRIPT: "Cross Traffic"   CROSS TRAFFIC
## A player hops upward through lanes of moving traffic. Dodge vehicles to reach the top.
## CONTROLS  Arrow Up: move up one lane    Arrow Left/Right: move horizontally
##                   Space: hop to the next higher lane
## RULES    Reach the top of a lane: +1 score. Hit a vehicle: -1 life.
##           All lives lost: game over. Reach the top with lives left: final score.
######################################################################################

global gObjectTransforms, gSceneObjects
global bPaused, bPlaying

local sLevel = 1
local sScore = 0
local sLives = 3
local sPlayerX = 0
local sPlayerY = -300
local sPlayerDx = 0
local sPlayerDy = 0
local sPlayerSpeed = 1
local sVehicleLeft = 2
local sVehicleRight = 3
local sLaneCount = 5
local sCarsPerLane = 2
local sCarSpeed = 2
local sCarDir = 1
local sCarX = 0
local sCarY = 0
local sCarDx = 0
local sCarDy = 0
local sCarSpeedBase = 2
local sCarSpeedMod = 0
local sTopReached = false
local sOver = false
local sKeys
local sKeysDown
local sHopPending = false
local sLaneIndex = 0
local sLaneY = -300
local sLaneHalfHeight = 10
local sLaneWidth = 900
local sVehicleHalfWidth = 40
local sVehicleHalfHeight = 20
local sPlayerHalfWidth = 15
local sPlayerHalfHeight = 25
local sScoreHUD, sLifeHUD, sTopHUD, sOverHUD
local sHighScore
local sLevelNames

constant kZ = 600
constant kLeft = -450
constant kRight = 450
constant kTop = -300
constant kBottom = 300
constant kLaneStep = 20
constant kPlayerSpeed = 1
constant kVehicleSpeedLeft = 2
constant kVehicleSpeedRight = 3
constant kScoreStart = 0
constant kLifeStart = 3
constant kLaneCount = 5
constant kCarsPerLane = 2
constant kTimeLimit = 60

on Game.OnStart
   Engine.ResetCamera
   Scene.ClearAll
   Particles.Clear
   HUD.Clear
   Collision.ClearRules
   Mesh.Define "Cross.Lane", MeshBox(900, 20, 16)
   Mesh.Define "Cross.Vehicle", MeshBox(80, 40, 16)
   Mesh.Define "Cross.Player", MeshBox(30, 50, 16)
   Mesh.Define "Cross.Score", MeshBox(120, 30, 16)
   Mesh.Define "Cross.Life", MeshBox(40, 40, 16)
   put 0 into sPlayerX
   put kBottom into sPlayerY
   put 0 into sPlayerDx
   put 0 into sPlayerDy
   put kPlayerSpeed into sPlayerSpeed
   put kVehicleSpeedLeft into sVehicleLeft
   put kVehicleSpeedRight into sVehicleRight
   put kScoreStart into sScore
   put kLifeStart into sLives
   put kLaneCount into sLaneCount
   put kCarsPerLane into sCarsPerLane
   put kCarSpeed into sCarSpeed
   put 1 into sCarDir
   put 0 into sCarX
   put kBottom into sCarY
   put 0 into sCarDx
   put 0 into sCarDy
   put 2 into sCarSpeedBase
   put 0 into sCarSpeedMod
   put false into sTopReached
   put false into sOver
   put false into sHopPending
   put 0 into sLaneIndex
   put kBottom into sLaneY
   put 10 into sLaneHalfHeight
   put 900 into sLaneWidth
   put 40 into sVehicleHalfWidth
   put 20 into sVehicleHalfHeight
   put 15 into sPlayerHalfWidth
   put 25 into sPlayerHalfHeight
   put 0 into sScoreHUD
   put 0 into sLifeHUD
   put 0 into sTopHUD
   put 0 into sOverHUD
   put 0 into sHighScore
   put 0 into sLevelNames
   put Entity.Spawn("Cross.Player", sPlayerX, sPlayerY, kZ, "green") into sPlayer
   put Entity.Spawn("Cross.Score", 20, 20, kZ, "white") into sScoreHUD
   put Entity.Spawn("Cross.Life", 20, 40, kZ, "red") into sLifeHUD
   put Entity.Spawn("Cross.Top", 20, 10, kZ, "cyan") into sTopHUD
   put Entity.Spawn("Cross.Over", 20, 10, kZ, "magenta") into sOverHUD
   Cross.StartLevel 1
end Game.OnStart

on Game.OnUpdate
   if sOver then exit Game.OnUpdate
   put the keysDown into sKeysDown
   if 65362 is among the items of sKeysDown then
      if sHopPending then
         Cross.HopPlayer
      end if
   end if
   if 65361 is among the items of sKeysDown then
      add -1 to sPlayerDx
   end if
   if 65363 is among the items of sKeysDown then
      add 1 to sPlayerDx
   end if
   add sPlayerSpeed into sPlayerX
   add sPlayerDx into sPlayerX
   put max(kLeft, min(kRight, sPlayerX)) into sPlayerX
   SetObjectPosition sPlayer, sPlayerX, sPlayerY, kZ
   if sHopPending then
      add kLaneStep into sPlayerY
      put false into sHopPending
      if sPlayerY >= kTop then
         add 1 to sScore
         put true into sTopReached
         put false into sHopPending
      end if
   end if
   if sLaneIndex < sLaneCount - 1 then
      if sPlayerY >= sLaneY + sLaneHalfHeight then
         add kLaneStep into sLaneY
         add 1 to sLaneIndex
         Cross.UpdateLanes sLaneIndex
      end if
   end if
   Cross.UpdateVehicles sLaneIndex
   if sPlayerX > sCarX + sVehicleHalfWidth then
      add 1 to sLives
   end if
   if sPlayerX < sCarX - sVehicleHalfWidth then
      add 1 to sLives
   end if
   if sPlayerY > sCarY + sVehicleHalfHeight then
      add 1 to sLives
   end if
   if sPlayerY < sCarY - sVehicleHalfHeight then
      add 1 to sLives
   end if
   if abs(sPlayerX - sCarX) <= sVehicleHalfWidth and abs(sPlayerY - sCarY) <= sVehicleHalfHeight then
      subtract 1 from sLives
      if sLives <= 0 then
         put true into sOver
         HUD.Set "Cross.Over", "GAME OVER", 20, 10, 24
      end if
   end if
   if sLives < kLifeStart then
      HUD.Set "Cross.Life", sLives, 40, 24
   end if
   if sTopReached and sLives > 0 then
      Cross.ShowHUD
   end if
end Game.OnUpdate

on Cross.StartLevel pLevel
   put pLevel into sLevel
   put kScoreStart into sScore
   put kLifeStart into sLives
   put kLaneCount into sLaneCount
   put kCarsPerLane into sCarsPerLane
   put kCarSpeed into sCarSpeed
   put kVehicleSpeedLeft into sVehicleLeft
   put kVehicleSpeedRight into sVehicleRight
   put 1 into sCarDir
   put 0 into sCarX
   put kBottom into sCarY
   put 0 into sCarDx
   put 0 into sCarDy
   put 2 into sCarSpeedBase
   put 0 into sCarSpeedMod
   put false into sTopReached
   put false into sOver
   put false into sHopPending
   put 0 into sLaneIndex
   put kBottom into sLaneY
   put 10 into sLaneHalfHeight
   put 900 into sLaneWidth
   put 40 into sVehicleHalfWidth
   put 20 into sVehicleHalfHeight
   put 15 into sPlayerHalfWidth
   put 25 into sPlayerHalfHeight
   put 0 into sScoreHUD
   put 0 into sLifeHUD
   put 0 into sTopHUD
   put 0 into sOverHUD
   put 0 into sHighScore
   put 0 into sLevelNames
   if sLevel = 1 then
      put "Cross Traffic Start" into sLevelNames
   end if
   if sLevel = 2 then
      put "Cross Traffic Easy" into sLevelNames
   end if
   if sLevel = 3 then
      put "Cross Traffic Medium" into sLevelNames
   end if
   if sLevel = 4 then
      put "Cross Traffic Hard" into sLevelNames
   end if
   if sLevel = 5 then
      put "Cross Traffic Expert" into sLevelNames
   end if
   if sLevel >= 2 then
      put 3 into sCarsPerLane
   end if
   if sLevel >= 3 then
      put 3 into sCarSpeed
   end if
   if sLevel >= 4 then
      put 3 into sCarSpeed
   end if
   if sLevel >= 5 then
      put 4 into sCarSpeed
   end if
   if sLevel >= 5 then
      put 6 into sCarsPerLane
   end if
   Cross.ShowHUD
end Cross.StartLevel

on Cross.HopPlayer
   if sHopPending then
      put false into sHopPending
   end if
end Cross.HopPlayer

on Cross.UpdateLanes pLaneIndex
   put pLaneIndex into sLaneIndex
   put kBottom into sLaneY
   put 10 into sLaneHalfHeight
   put 900 into sLaneWidth
   if sLaneIndex < sLaneCount - 1 then
      add kLaneStep into sLaneY
   end if
end Cross.UpdateLanes

on Cross.UpdateVehicles pLaneIndex
   put pLaneIndex into sLaneIndex
   put 0 into sCarX
   put kBottom into sCarY
   put 0 into sCarDx
   put 0 into sCarDy
   put 2 into sCarSpeedBase
   put 0 into sCarSpeedMod
   if sLaneIndex < sLaneCount - 1 then
      if sLaneIndex >= 1 then
         if sLaneIndex = 1 then
            put 2 into sCarSpeed
         end if
         if sLaneIndex = 2 then
            put 3 into sCarSpeed
         end if
         if sLaneIndex = 3 then
            put 3 into sCarSpeed
         end if
         if sLaneIndex = 4 then
            put 4 into sCarSpeed
         end if
      end if
   end if
   if sCarsPerLane > 2 then
      put 3 into sCarsPerLane
   end if
   if sCarsPerLane > 5 then
      put 5 into sCarsPerLane
   end if
   if sCarsPerLane > 6 then
      put 6 into sCarsPerLane
   end if
   if sCarDir = 1 then
      put sCarSpeedLeft into sCarDx
   else
      put sCarSpeedRight into sCarDx
   end if
   add sCarDx into sCarX
   put max(kLeft, min(kRight, sCarX)) into sCarX
   if sCarX >= kRight then
      subtract sCarDx into sCarX
   end if
   if sCarX <= kLeft then
      add sCarDx into sCarX
   end if
   if sCarSpeedMod < 1 then
      add 1 to sCarSpeedMod
   end if
   if sCarSpeedMod >= 1 then
      put 0 into sCarSpeedMod
   end if
   if sCarSpeedBase < 2 then
      add 1 to sCarSpeedBase
   end if
   if sCarSpeedBase > 4 then
      subtract 1 from sCarSpeedBase
   end if
end Cross.UpdateVehicles

on Cross.ShowHUD
   if sScoreHUD is not nil then
      HUD.Set "Cross.Score", sScore, 20, 20, 14
   end if
   if sLifeHUD is not nil then
      HUD.Set "Cross.Life", sLives, 40, 20, 14
   end if
   if sTopHUD is not nil then
      HUD.Set "Cross.Top", "REACHED", 20, 10, 14
   end if
   if sOverHUD is not nil then
      HUD.Set "Cross.Over", "GAME OVER", 20, 10, 24
   end if
end Cross.ShowHUD

on Game.OnStop
   HUD.Remove "Cross.Score"
   HUD.Remove "Cross.Life"
   HUD.Remove "Cross.Top"
   HUD.Remove "Cross.Over"
end Game.OnStop

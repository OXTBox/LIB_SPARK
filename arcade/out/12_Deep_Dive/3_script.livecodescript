######################################################################################
## CARD SCRIPT: "Deep Dive"   DEEP DIVE
## A diver swims through the dark sea, collecting pearls and dodging fish.
## CONTROLS  Left/Right arrows: move the diver    Up/Down arrows: move the diver
##           Space: refill air at the surface
## RULES    Collect a pearl for +1 score; touch a fish or run out of air for -1 life;
##          reach level 5 with all lives left to win.
######################################################################################

global gObjectTransforms, gSceneObjects
global bPaused, bPlaying

local sDiverX, sDiverY, sDiverSpeed = 0, 0, 120
local sPearlX, sPearlY, sPearlCount = 0, 0, 10
local sFishX, sFishY, sFishSpeed, sFishCount = 0, 0, 80, 2
local sAirSteps, sAirLeft, sLives, sScore, sLevel, sOver, sFishTimer
local sPearlTimer, sAirTimer

constant kZ = 600
constant kLeft = -450
constant kRight = 450
constant kTop = -300
constant kBottom = 300
constant kDiverSpeed = 120
constant kPearlSpeed = 80
constant kFishSpeed = 80
constant kAirRefillSteps = 60
constant kLives = 3
constant kFinalLevel = 5

on Game.OnStart
   Engine.ResetCamera
   Scene.ClearAll
   Particles.Clear
   HUD.Clear
   Collision.ClearRules
   Mesh.Define "Dive.Diver", MeshBox(40, 40, 16)
   Mesh.Define "Dive.Pearl", MeshBox(20, 20, 20)
   Mesh.Define "Dive.Fish", MeshBox(60, 30, 16)
   Mesh.Define "Dive.Air", MeshBox(900, 100, 16)
   put 0 into sDiverX
   put kBottom into sDiverY
   put 0 into sPearlX
   put kTop into sPearlY
   put 0 into sPearlCount
   put 0 into sFishX
   put kTop into sFishY
   put 0 into sFishSpeed
   put 0 into sFishCount
   put 0 into sAirSteps
   put kAirRefillSteps into sAirSteps
   put kAirRefillSteps into sAirLeft
   put kLives into sLives
   put 0 into sScore
   put 1 into sLevel
   put false into sOver
   put 0 into sFishTimer
   put 0 into sPearlTimer
   put Entity.Spawn("Dive.Diver", sDiverX, sDiverY, kZ, "cyan") into sDiver
   put Entity.Spawn("Dive.Pearl", sPearlX, sPearlY, kZ, "gold") into sPearl
   put Entity.Spawn("Dive.Fish", sFishX, sFishY, kZ, "blue") into sFish
   Dive.StartLevel 1
   Dive.ShowHUD
end Game.OnStart

on Game.OnUpdate
   if sOver then exit Game.OnUpdate
   put the keysDown into tKeys
   if 65361 is among the items of tKeys then subtract kDiverSpeed from sDiverX
   if 65363 is among the items of tKeys then add kDiverSpeed to sDiverX
   if 65362 is among the items of tKeys then subtract kDiverSpeed from sDiverY
   if 65364 is among the items of tKeys then add kDiverSpeed to sDiverY
   put max(kLeft, min(kRight, sDiverX)) into sDiverX
   put max(kTop, min(kBottom, sDiverY)) into sDiverY
   SetObjectPosition sDiver, sDiverX, sDiverY, kZ
   add sPearlTimer to sPearlTimer
   add sFishTimer to sFishTimer
   add sAirTimer to sAirTimer
   if sPearlTimer >= 10 then
      put 0 into sPearlTimer
      if sPearlCount > 0 then
         put 0 into sPearlX
         put kTop into sPearlY
         put Entity.Spawn("Dive.Pearl", sPearlX, sPearlY, kZ, "gold") into sPearl
         add 1 to sPearlCount
      end if
   end if
   if sFishTimer >= 10 then
      put 0 into sFishTimer
      if sFishCount > 0 then
         put random(kRight - kLeft) + kLeft into sFishX
         put kTop into sFishY
         put random(kFishSpeed) + kFishSpeed into sFishSpeed
         put Entity.Spawn("Dive.Fish", sFishX, sFishY, kZ, "blue") into sFish
         add 1 to sFishCount
      end if
   end if
   if sAirTimer >= 10 then
      put 0 into sAirTimer
      if sAirLeft >= kAirRefillSteps then
         put kAirRefillSteps into sAirLeft
      end if
   end if
   if sAirLeft <= 0 then
      subtract 1 from sLives
      if sLives <= 0 then
         put true into sOver
         HUD.Set "Dive.Over", "GAME OVER", 300, 200, 24
      end if
   end if
   if sLevel < kFinalLevel then
      add 1 to sLevel
      Dive.StartLevel sLevel
   end if
end Game.OnUpdate

on Dive.StartLevel pLevel
   put pLevel into sLevel
   put 0 into sFishCount
   put 0 into sPearlCount
   put 0 into sAirSteps
   put kAirRefillSteps into sAirSteps
   put kAirRefillSteps into sAirLeft
   put kLives into sLives
   put 0 into sScore
   put 0 into sFishTimer
   put 0 into sPearlTimer
   put 0 into sFishX
   put kTop into sFishY
   put 0 into sFishSpeed
   put Entity.Spawn("Dive.Fish", sFishX, sFishY, kZ, "blue") into sFish
   Dive.ShowHUD
end Dive.StartLevel

on Dive.ShowHUD
   HUD.Set "Dive.Level", "LEVEL" && sLevel, 20, 20, 14
   HUD.Set "Dive.Score", "SCORE" && sScore, 20, 40, 14
   HUD.Set "Dive.Air", "AIR" && sAirLeft && " STEPS", 20, 60, 14
   HUD.Set "Dive.Lives", "LIVES" && sLives, 20, 80, 14
end Dive.ShowHUD

on Game.OnStop
   HUD.Remove "Dive.Level"
   HUD.Remove "Dive.Score"
   HUD.Remove "Dive.Air"
   HUD.Remove "Dive.Lives"
   HUD.Remove "Dive.Over"
end Game.OnStop

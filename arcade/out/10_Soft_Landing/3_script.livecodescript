######################################################################################
## CARD SCRIPT: "Soft Landing"  SOFT LANDING
## A lander falls through the air. Tilt with arrows, fire with Space. Land softly on the pad.
## CONTROLS  Left/Right arrows: tilt the lander    Up/Down arrows: adjust vertical thrust    Space: fire main engine
## RULES    Land slowly on the green pad to score. Fuel runs out after fixed shots. Each level raises the landing speed.
######################################################################################

global gObjectTransforms, gSceneObjects
global bPaused, bPlaying

local sLanderX, sLanderY, sLanderDx, sLanderDy, sFallSpeed
local sFuel, sShots, sScore, sLives, sLevel, sOver, sPadX, sPadY, sPadW, sPadH
local sMaxSpeed, sRequiredSpeed, sLandingSpeed
local sKeys, sFired, sLanding

constant kZ = 600
constant kLeft = -450
constant kRight = 450
constant kTop = -300
constant kBottom = 300
constant kLanderW = 120
constant kLanderH = 60
constant kPadW = 800
constant kPadH = 40
constant kFuelMax = 10
constant kScoreStart = 0
constant kLivesStart = 3
constant kLevelSpeed = 1.0
constant kFallStep = 2.0
constant kThrustStep = 1.0
constant kFuelPerShot = 1
constant kLandingMargin = 20

on Game.OnStart
   Engine.ResetCamera
   Scene.ClearAll
   Particles.Clear
   HUD.Clear
   Collision.ClearRules
   Mesh.Define "Land.Lander", MeshBox(kLanderW, kLanderH, 16)
   Mesh.Define "Land.GroundPad", MeshBox(kPadW, kPadH, 16)
   Mesh.Define "Land.FuelTank", MeshBox(40, 80, 16)
   Mesh.Define "Land.ScoreDisplay", MeshBox(200, 60, 16)
   put Land.StartLevel 1 into sLevel
   Land.StartLevel 1
   put Land.ShowHUD 1 into sShowHUD
   put Entity.Spawn("Land.Lander", 0, kBottom, kZ, "cyan") into sLander
   put Entity.Spawn("Land.GroundPad", 0, kBottom, kZ, "green") into sPad
   put Entity.Spawn("Land.FuelTank", 0, kBottom, kZ, "orange") into sFuelTank
   put Entity.Spawn("Land.ScoreDisplay", 0, kBottom, kZ, "yellow") into sScoreDisplay
end Game.OnStart

on Game.OnUpdate
   if sOver then exit Game.OnUpdate
   if sShowHUD then Land.ShowHUD
   end if
   put the keysDown into sKeys
   if 65361 is among the items of sKeys then subtract kLanderDx from sLanderDx
   if 65363 is among the items of sKeys then add kLanderDx to sLanderDx
   if 65362 is among the items of sKeys then add kThrustStep to sLanderDy
   if 65364 is among the items of sKeys then subtract kThrustStep from sLanderDy
   if 32 is among the items of sKeys then
      add kFuelPerShot to sShots
      add kThrustStep to sLanderDy
      subtract kFuelPerShot from sFuel
      FX.Sparks sLanderX, sLanderY, kZ, 10, "orange"
   end if
   sLanderX = sLanderX + sLanderDx
   sLanderY = sLanderY + sLanderDy
   sFallSpeed = sFallSpeed + kFallStep
   SetObjectPosition sLander, sLanderX, sLanderY, kZ
   if sFuel <= 0 then
      subtract 1 from sLives
      if sLives <= 0 then
         put true into sOver
         HUD.Set "Land.Over", "GAME OVER", 300, 200, 24
      end if
   end if
   if sLanderY >= kBottom - kLandingMargin then
      if abs(sLanderX - sPadX) <= sPadW / 2 and abs(sLanderY - sPadY) <= kPadH / 2 then
         add sFallSpeed * 10 to sScore
         put false into sOver
         HUD.Set "Land.Level", "LEVEL " && sLevel && " COMPLETE", 20, 20, 14
      else
         subtract 1 from sLives
         if sLives <= 0 then
            put true into sOver
            HUD.Set "Land.Over", "GAME OVER", 300, 200, 24
         end if
      end if
   end if
end Game.OnUpdate

on Land.StartLevel pLevel
   sLevel = pLevel
   sFuel = kFuelMax
   sShots = 0
   sScore = kScoreStart
   sLives = kLivesStart
   sOver = false
   sPadX = 0
   sPadY = kBottom
   sPadW = 800
   sPadH = 40
   sMaxSpeed = 1.0
   if sLevel >= 2 then
      sPadW = 900
      sMaxSpeed = 1.5
   end if
   if sLevel >= 3 then
      sPadW = 1000
      sMaxSpeed = 2.0
   end if
   if sLevel >= 4 then
      sPadW = 1100
      sMaxSpeed = 2.5
   end if
   if sLevel >= 5 then
      sPadW = 1200
      sMaxSpeed = 3.0
   end if
   sRequiredSpeed = sMaxSpeed
   sLandingSpeed = sRequiredSpeed
   HUD.Remove "Land.Level"
   HUD.Remove "Land.Over"
end Land.StartLevel

on Land.ShowHUD
   HUD.Set "Land.Score", sScore && "  LIVES" && sLives, 20, 20, 14
   HUD.Set "Land.Landing", "MAX " && sRequiredSpeed, 20, 40, 14
   HUD.Set "Land.Fuel", sFuel, 20, 60, 14
end Land.ShowHUD

on Game.OnStop
   HUD.Remove "Land.Score"
   HUD.Remove "Land.Landing"
   HUD.Remove "Land.Fuel"
   HUD.Remove "Land.Level"
   HUD.Remove "Land.Over"
end Game.OnStop

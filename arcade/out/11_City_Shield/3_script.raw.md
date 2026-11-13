```
######################################################################################
## CARD SCRIPT: "City.Shield"   CITY SHIELD
## Aim the cross at falling streaks and fire bursts to destroy them, protecting the
## city blocks until all streaks are cleared.
## CONTROLS  Left/Right arrows: move the aiming cross    Up/Down arrows: move the cross
##           Space: fire a burst
## RULES     Each streak destroyed by a burst adds 100 to the score; the level ends
##           when all streaks are cleared; the game ends when every city block is
##           destroyed; a city block hit by a streak costs one life
######################################################################################

global gStreaks, gCityBlocks, gLives, gScore, gLevel, gStreakSpeed, gBurstRadius, gBurstSpeed
global gCityBlockKeys, gStreakKeys, gBurstKeys
global sCrossX, sCrossY, sBurstX, sBurstY, sBurstActive, sLevel
global sStreakX, sStreakY, sStreakSpeed, sStreakCount, sCityBlockX, sCityBlockY, sCityBlockState
global sCityBlockKeys, sStreakKeys, sBurstKeys, sKeys, sBurstCooldown

local kZ = 600
local kLeft = -450
local kRight = 450
local kTop = -300
local kBottom = 300
local kCrossW = 40
local kCrossH = 20
local kStreakW = 80
local kStreakH = 30
local kCityW = 150
local kCityH = 120
local kBurstW = 100
local kBurstH = 100
local kScorePerStrreak = 100
local kLivesStart = 3
local kStreakStart = 10
local kCityBlocksStart = 6
local kStreakSpeedBase = 120
local kBurstSpeedBase = 30

constant kLevel1 = 1
constant kLevel2 = 2
constant kLevel3 = 3
constant kLevel4 = 4
constant kLevel5 = 5

on Game.OnStart
   Engine.ResetCamera
   Scene.ClearAll
   Particles.Clear
   HUD.Clear
   Collision.ClearRules
   Mesh.Define "City.Cross", MeshBox(kCrossW, kCrossH, 16)
   Mesh.Define "City.Streak", MeshBox(kStreakW, kStreakH, 30)
   Mesh.Define "City.CityBlock", MeshBox(kCityW, kCityH, 30)
   Mesh.Define "City.Burst", MeshBox(kBurstW, kBurstH, 30)
   put 0 into sCrossX
   put kBottom into sCrossY
   put 0 into sBurstX
   put 0 into sBurstY
   put false into sBurstActive
   put 0 into sBurstCooldown
   put 0 into sStreakCount
   put 0 into sCityBlockState
   put 0 into sCityBlockKeys
   put 0 into sStreakKeys
   put 0 into sBurstKeys
   put 0 into gStreaks
   put 0 into gCityBlocks
   put 0 into gLives
   put 0 into gScore
   put 0 into gLevel
   put 120 into gStreakSpeed
   put 30 into gBurstSpeed
   put 40 into gBurstRadius
   put kLevel1 into sLevel
   City.StartLevel kLevel1
   City.ShowHUD
end Game.OnStart

on Game.OnUpdate
   if sLevel >= 5 then
      if gStreakCount <= 0 and gCityBlockState == 0 then
         put true into sLevel
         HUD.Set "City.Win", "YOU WIN", 300, 200, 24
      end if
   else
      if gStreakCount <= 0 and gCityBlockState == 0 then
         City.StartLevel kLevel5
      end if
   end if
   if sBurstActive then
      add 1 to sBurstCooldown
      if sBurstCooldown >= 15 then
         sBurstActive = false
         sBurstCooldown = 0
      end if
   end if
   if sBurstActive then
      add gBurstSpeed to sBurstY
      SetObjectPosition sBurst, sBurstX, sBurstY, kZ
      if sBurstY >= kBottom - 50 then
         sBurstActive = false
      end if
   end if
   if sBurstCooldown > 0 then
      subtract 1 from sBurstCooldown
   end if
   put the keysDown into sKeys
   if 65361 is among the items of sKeys then subtract kCrossSpeed from sCrossX
   if 65363 is among the items of sKeys then add kCrossSpeed to sCrossX
   if 65362 is among the items of sKeys then add kCrossSpeed to sCrossY
   if 65364 is among the items of sKeys then subtract kCrossSpeed from sCrossY
   if 32 is among the items of sKeys then
      if sBurstCooldown <= 0 then
         sBurstActive = true
         sBurstCooldown = 15
         put random(gBurstRadius) + kLeft into sBurstX
         put random(kTop - kBottom) + kTop into sBurstY
         put Entity.Spawn("City.Burst", sBurstX, sBurstY, kZ, "orange") into sBurstKeys
      end if
   end if
   if sBurstActive then
      SetObjectPosition sBurst, sBurstX, sBurstY, kZ
   end if
   if sCrossX < kLeft then
      put kLeft into sCrossX
   end if
   if sCrossX > kRight then
      put kRight into sCrossX
   end if
   if sCrossY < kTop then
      put kTop into sCrossY
   end if
   if sCrossY > kBottom then
      put kBottom into sCrossY
   end if
   SetObjectPosition sCross, sCrossX, sCrossY, kZ
   if gStreakCount > 0 then
      add gStreakSpeed to sStreakY
      for i = 1 to gStreakCount do
         if sStreakKeys[i] is not nil then
            SetObjectPosition sStreakKeys[i], sStreakX[i], sStreakY[i], kZ
            if sStreakY[i] >= kBottom - 20 then
               if abs(sStreakX[i] - sCrossX) <= gBurstRadius and abs(sStreakY[i] - sCrossY) <= kStreakH / 2 then
                  City.Kill sStreakKeys[i]
                  add 1 to gStreakCount
                  add 100 to gScore
                  FX.Sparks sStreakX[i], sStreakY[i], kZ, 10, "yellow"
               end if
            end if
         end if
      end for
      if gStreakCount <= 0 then
         City.StartLevel sLevel
      end if
   end if
   if gLives <= 0 then
      put true into sLevel
      HUD.Set "City.Lose", "GAME OVER", 300, 200, 24
   end if
end Game.OnUpdate

on City.StartLevel pLevel
   put pLevel into sLevel
   put 0 into gStreaks
   put 0 into gCityBlocks
   put 0 into gLives
   put 0 into gScore
   put pLevel into gLevel
   put 120 into gStreakSpeed
   put 30 into gBurstSpeed
   put 40 into gBurstRadius
   put 0 into sStreakCount
   put 0 into sCityBlockState
   put 0 into sCityBlockKeys
   put 0 into sStreakKeys
   put 0 into sBurstKeys
   put 0 into sBurstCooldown
   put false into sBurstActive
   put 0 into sCrossX
   put kBottom into sCrossY
   put 0 into sBurstX
   put 0 into sBurstY
   put 0 into sStreakX
   put 0 into sStreakY
   put 0 into sCityBlockX
   put 0 into sCityBlockY
   put 0 into gStreakCount
   put 0 into gCityBlockState
   put 0 into gCityBlockKeys
   put 0 into gStreakKeys
   put 0 into gBurstKeys
   put 3 into gLives
   put 0 into gScore
   if pLevel == kLevel1 then
      put 10 into gStreaks
      put 120 into gStreakSpeed
      put 15 into gBurstAllowed
      put 40 into gBurstRadius
   else if pLevel == kLevel2 then
      put 12 into gStreaks
      put 120 into gStreakSpeed
      put 18 into gBurstAllowed
      put 45 into gBurstRadius
   else if pLevel == kLevel3 then
      put 14 into gStreaks
      put 130 into gStreakSpeed
      put 20 into gBurstAllowed
      put 50 into gBurstRadius
   else if pLevel == kLevel4 then
      put 16 into gStreaks
      put 140 into gStreakSpeed
      put 22 into gBurstAllowed
      put 55 into gBurstRadius
   else if pLevel == kLevel5 then
      put 18 into gStreaks
      put 150 into gStreakSpeed
      put 25 into gBurstAllowed
      put 60 into gBurstRadius
   end if
   City.BuildCityBlocks
   City.BuildStreaks
   City.ShowHUD
end City.StartLevel

on City.BuildCityBlocks
   put 6 into gCityBlocks
   put 0 into gCityBlockState
   put 0 into sCityBlockKeys
   local sCityX = -300
   local sCityY = -300
   for i = 1 to 6 do
      put Entity.Spawn("City.CityBlock", sCityX, sCityY, kZ, "blue") into sCityBlockKeys[i]
      put i into sCityBlockState[i]
      put sCityX into sCityBlockX[i]
      put sCityY into sCityBlockY[i]
      add 150 to sCityX
   end for
end City.BuildCityBlocks

on City.BuildStreaks
   put 0 into gStreakKeys
   local sStreakX = 0
   local sStreakY = kTop
   for i = 1 to gStreaks do
      put Entity.Spawn("City.Streak", sStreakX, sStreakY, kZ, "red") into sStreakKeys[i]
      put sStreakX into sStreakX[i]
      put sStreakY into sStreakY[i]
      add 100 to sStreakX
   end for
end City.BuildStreaks

on City.ShowHUD
   HUD.Set "City.Score", "SCORE" && gScore, 20, 20, 14
   HUD.Set "City.Lives", "LIVES" && gLives, 20, 40, 14
   HUD.Set "City.Level", "LEVEL" && gLevel, 20, 60, 14
end City.ShowHUD

on City.Kill pKey
   if pKey is in sCityBlockKeys then
      subtract 1 from gCityBlockState[pKey]
      if gCityBlockState[pKey] == 0 then
         add 1 to gCityBlockKeysCount
      end if
   end if
   if pKey is in sStreakKeys then
      add 1 to gStreakCount
   end if
   if pKey is in sBurstKeys then
      remove pKey from sBurstKeys
   end if
end City.Kill

on Game.OnStop
   HUD.Remove "City.Score"
   HUD.Remove "City.Lives"
   HUD.Remove "City.Level"
   HUD.Remove "City.Win"
   HUD.Remove "City.Lose"
end Game.OnStop
```

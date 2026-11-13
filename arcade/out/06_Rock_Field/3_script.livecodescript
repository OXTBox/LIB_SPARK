######################################################################################
## CARD SCRIPT: "Rock Field"   ROCK FIELD
## A ship steers through drifting rocks and splits them with shots to score points.
## CONTROLS  Left/Right arrows: steer the ship    Up/Down arrows: drift the ship
##           Space: fire a shot    Escape: pause
## RULES     Big rocks drift and can be split into fragments; small rocks add 10 points
##           Firing splits a big rock; hitting a rock costs one life; 500 points wins.
######################################################################################

global gObjectTransforms, gSceneObjects
global bPaused, bPlaying

local sShipX, sShipY, sShipDx, sShipDy, sShipSpeed = 0, 0, 0, 0, 150
local sBigRockX, sBigRockY, sBigRockDx, sBigRockDy, sBigRockSpeed = 0, 0, 0, 0, 80
local sSmallRockX, sSmallRockY, sSmallRockDx, sSmallRockDy, sSmallRockSpeed = 0, 0, 0, 0, 40
local sFragmentX, sFragmentY, sFragmentDx, sFragmentDy, sFragmentSpeed = 0, 0, 0, 0, 20
local sLives, sScore, sTargetScore, sLevel, sOver, sPaused = 3, 0, 500, 1, false, false
local sBigRockCount, sSmallRockPerSplit, sRockSpeed, sFragmentSpeed
local sFragCount, sFragX, sFragY, sFragDx, sFragDy
local tKeys, tRockKey, tFragKey, tShotKey
local kZ, kLeft, kRight, kTop, kBottom, kShipHalfW, kShipHalfH
local kBigRockHalfW, kBigRockHalfH, kSmallRockHalfW, kSmallRockHalfH, kFragHalfW, kFragHalfH
local kShotSpeed = 300

constant kZ = 600          -- every object sits at this depth
constant kLeft = -450      -- playfield edges (world units; +Y is DOWN)
constant kRight = 450
constant kTop = -300
constant kBottom = 300
constant kShipHalfW = 60
constant kShipHalfH = 30
constant kBigRockHalfW = 150
constant kBigRockHalfH = 150
constant kSmallRockHalfW = 60
constant kSmallRockHalfH = 60
constant kFragHalfW = 40
constant kFragHalfH = 40

on Game.OnStart
   Engine.ResetCamera
   Scene.ClearAll
   Particles.Clear
   HUD.Clear
   Collision.ClearRules
   Mesh.Define "Rock.Ship", MeshBox(120, 60, 16)
   Mesh.Define "Rock.BigRock", MeshBox(300, 300, 30)
   Mesh.Define "Rock.SmallRock", MeshBox(120, 120, 30)
   Mesh.Define "Rock.Fragment", MeshBox(80, 80, 30)
   put 1 into sLevel
   put 2 into sBigRockCount
   put 1 into sSmallRockPerSplit
   put 80 into sRockSpeed
   put 20 into sFragmentSpeed
   put 0 into sFragCount
   put 0 into sFragX
   put 0 into sFragY
   put 0 into sFragDx
   put 0 into sFragDy
   put 3 into sLives
   put 0 into sScore
   put false into sOver
   put false into sPaused
   put Entity.Spawn("Rock.Ship", 0, 0, kZ, "cyan") into sShip
   put Entity.Spawn("Rock.BigRock", 0, kTop, kZ, "amber") into sBigRockKey
   put Entity.Spawn("Rock.SmallRock", 0, kTop, kZ, "orange") into sSmallRockKey
   Rock.StartLevel sLevel
end Game.OnStart

on Game.OnUpdate
   if sPaused then exit Game.OnUpdate
   put the keysDown into tKeys
   if sOver then exit Game.OnUpdate
   if 65361 is among the items of tKeys then add -sShipSpeed to sShipDx
   if 65363 is among the items of tKeys then add sShipSpeed to sShipDx
   if 65362 is among the items of tKeys then add -sShipSpeed to sShipDy
   if 65364 is among the items of tKeys then add sShipSpeed to sShipDy
   put max(kLeft, min(kRight, sShipX + sShipDx)) into sShipX
   put max(kTop, min(kBottom, sShipY + sShipDy)) into sShipY
   SetObjectPosition sShip, sShipX, sShipY, kZ
   if 32 is among the items of tKeys then Rock.FireShot
   Rock.UpdateRocks
   Rock.CheckCollisions
   Rock.CheckSmallRocks
   Rock.ShowHUD
end Game.OnUpdate

on Game.OnStop
   HUD.Remove "Rock.Score"
   HUD.Remove "Rock.Lives"
   HUD.Remove "Rock.Level"
   HUD.Remove "Rock.Win"
   HUD.Remove "Rock.Lose"
end Game.OnStop

on Rock.StartLevel pLevel
   local sBigRockX, sBigRockY, sBigRockDx, sBigRockDy
   local sSmallRockX, sSmallRockY, sSmallRockDx, sSmallRockDy
   local sFragX, sFragY, sFragDx, sFragDy
   put pLevel into sLevel
   put 2 into sBigRockCount
   put 1 into sSmallRockPerSplit
   put 80 into sRockSpeed
   put 20 into sFragmentSpeed
   put 0 into sFragCount
   put 0 into sFragX
   put 0 into sFragY
   put 0 into sFragDx
   put 0 into sFragDy
   put 3 into sLives
   put 0 into sScore
   put false into sOver
   put false into sPaused
   put Entity.Kill sBigRockKey
   put Entity.Kill sSmallRockKey
   put Entity.Kill sFragKey
   put Entity.Kill sShip
   put Entity.Spawn("Rock.Ship", 0, 0, kZ, "cyan") into sShip
   put Entity.Spawn("Rock.BigRock", 0, kTop, kZ, "amber") into sBigRockKey
   put Entity.Spawn("Rock.SmallRock", 0, kTop, kZ, "orange") into sSmallRockKey
   local sBigRockX = -300
   local sBigRockY = kTop
   local sBigRockDx = sRockSpeed
   local sBigRockDy = 0
   put sBigRockX into sBigRockX
   put sBigRockY into sBigRockY
   put sBigRockDx into sBigRockDx
   put sBigRockDy into sBigRockDy
   put Entity.Spawn("Rock.BigRock", sBigRockX, sBigRockY, kZ, "amber") into sBigRockKey
   local sSmallRockX = 300
   local sSmallRockY = kTop
   local sSmallRockDx = sSmallRockSpeed
   local sSmallRockDy = 0
   put sSmallRockX into sSmallRockX
   put sSmallRockY into sSmallRockY
   put sSmallRockDx into sSmallRockDx
   put sSmallRockDy into sSmallRockDy
   put Entity.Spawn("Rock.SmallRock", sSmallRockX, sSmallRockY, kZ, "orange") into sSmallRockKey
   if pLevel = 1 then
      put 2 into sBigRockCount
      put 1 into sSmallRockPerSplit
      put 80 into sRockSpeed
      put 20 into sFragmentSpeed
   else if pLevel = 2 then
      put 3 into sBigRockCount
      put 1 into sSmallRockPerSplit
      put 90 into sRockSpeed
      put 20 into sFragmentSpeed
   else if pLevel = 3 then
      put 4 into sBigRockCount
      put 2 into sSmallRockPerSplit
      put 100 into sRockSpeed
      put 20 into sFragmentSpeed
   else if pLevel = 4 then
      put 5 into sBigRockCount
      put 2 into sSmallRockPerSplit
      put 110 into sRockSpeed
      put 20 into sFragmentSpeed
   else
      put 6 into sBigRockCount
      put 3 into sSmallRockPerSplit
      put 120 into sRockSpeed
      put 20 into sFragmentSpeed
   end if
end Rock.StartLevel

on Rock.FireShot
   local sShotX = sShipX
   local sShotY = sShipY
   local sShotDx = kShotSpeed
   local sShotDy = 0
   put sShotX into sShotX
   put sShotY into sShotY
   put sShotDx into sShotDx
   put sShotDy into sShotDy
   put Entity.Spawn("Rock.Fragment", sShotX, sShotY, kZ, "yellow") into sFragKey
   Rock.SplitBigRock
end Rock.FireShot

on Rock.UpdateRocks
   local sBigRockX, sBigRockY, sBigRockDx, sBigRockDy
   local sSmallRockX, sSmallRockY, sSmallRockDx, sSmallRockDy
   local sFragX, sFragY, sFragDx, sFragDy
   put sBigRockX into sBigRockX
   put sBigRockY into sBigRockY
   put sBigRockDx into sBigRockDx
   put sBigRockDy into sBigRockDy
   add sBigRockDx to sBigRockX
   add sBigRockDy to sBigRockY
   put max(kLeft, min(kRight, sBigRockX)) into sBigRockX
   put max(kTop, min(kBottom, sBigRockY)) into sBigRockY
   SetObjectPosition sBigRockKey, sBigRockX, sBigRockY, kZ
   put sSmallRockX into sSmallRockX
   put sSmallRockY into sSmallRockY
   put sSmallRockDx into sSmallRockDx
   put sSmallRockDy into sSmallRockDy
   add sSmallRockDx to sSmallRockX
   add sSmallRockDy to sSmallRockY
   put max(kLeft, min(kRight, sSmallRockX)) into sSmallRockX
   put max(kTop, min(kBottom, sSmallRockY)) into sSmallRockY
   SetObjectPosition sSmallRockKey, sSmallRockX, sSmallRockY, kZ
   put sFragX into sFragX
   put sFragY into sFragY
   put sFragDx into sFragDx
   put sFragDy into sFragDy
   add sFragDx to sFragX
   add sFragDy to sFragY
   put max(kLeft, min(kRight, sFragX)) into sFragX
   put max(kTop, min(kBottom, sFragY)) into sFragY
   SetObjectPosition sFragKey, sFragX, sFragY, kZ
   if sFragCount > 0 then
      local sFragX = sFragX
      local sFragY = sFragY
      local sFragDx = sFragDx
      local sFragDy = sFragDy
      add sFragDx to sFragX
      add sFragDy to sFragY
      put max(kLeft, min(kRight, sFragX)) into sFragX
      put max(kTop, min(kBottom, sFragY)) into sFragY
      SetObjectPosition sFragKey, sFragX, sFragY, kZ
   end if
end Rock.UpdateRocks

on Rock.SplitBigRock
   local sBigRockX, sBigRockY
   put sBigRockX into sBigRockX
   put sBigRockY into sBigRockY
   local sFragX = sBigRockX - 100
   local sFragY = sBigRockY - 50
   local sFragDx = sFragmentSpeed
   local sFragDy = 0
   put sFragX into sFragX
   put sFragY into sFragY
   put sFragDx into sFragDx
   put sFragDy into sFragDy
   put Entity.Spawn("Rock.Fragment", sFragX, sFragY, kZ, "yellow") into sFragKey
   local sFragX = sBigRockX + 100
   local sFragY = sBigRockY + 50
   local sFragDx = sFragmentSpeed
   local sFragDy = 0
   put sFragX into sFragX
   put sFragY into sFragY
   put sFragDx into sFragDx
   put sFragDy into sFragDy
   put Entity.Spawn("Rock.Fragment", sFragX, sFragY, kZ, "yellow") into sFragKey
   add sSmallRockPerSplit to sFragCount
   put Entity.Kill sBigRockKey
   put sBigRockKey into tRockKey
   put sFragKey into tFragKey
   put sShipKey into tShotKey
end Rock.SplitBigRock

on Rock.CheckCollisions
   local sShipX, sShipY
   local sBigRockX, sBigRockY
   local sSmallRockX, sSmallRockY
   put sShipX into sShipX
   put sShipY into sShipY
   put sBigRockX into sBigRockX
   put sBigRockY into sBigRockY
   put sSmallRockX into sSmallRockX
   put sSmallRockY into sSmallRockY
   if abs(sShipX - sBigRockX) <= kBigRockHalfW and abs(sShipY - sBigRockY) <= kBigRockHalfH then
      Rock.HitRock
   end if
   if abs(sShipX - sSmallRockX) <= kSmallRockHalfW and abs(sShipY - sSmallRockY) <= kSmallRockHalfH then
      Rock.HitRock
   end if
end Rock.CheckCollisions

on Rock.CheckSmallRocks
   local sShipX, sShipY
   local sSmallRockX, sSmallRockY
   put sShipX into sShipX
   put sShipY into sShipY

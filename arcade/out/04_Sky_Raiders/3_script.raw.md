```
######################################################################################
## CARD SCRIPT: "Sky Raiders"  SKY RAIDERS
## A cannon at the bottom shoots marching raiders marching down the top.
## Clear each row before they reach the floor.
## CONTROLS  Left/Right arrows: move the cannon    Space: fire
## RULES     Each cleared raider row scores 100; a raider reaching the floor costs one life
##           Raider speed rises by 5 world units per level; clear all rows to win
######################################################################################

global gObjectTransforms, gSceneObjects
global bPaused, bPlaying

local sCannonX, sCannonDx, sCannonDy = 0, 0, 0
local sShotX, sShotY, sShotDx, sShotDy = 0, 0, 0
local sRaiderX, sRaiderY, sRaiderDx, sRaiderDy = 0, 0, 0
local sRaiderSpeed, sShotSpeed, sCannonSpeed, sLives, sScore, sRows, sLevel, sOver, sShields
local sKeys, sShieldKeys

constant kZ = 600          -- every object sits at this depth
constant kLeft = -450      -- playfield edges (world units; +Y is DOWN)
constant kRight = 450
constant kTop = -300
constant kBottom = 300
constant kCannonX = 0
constant kCannonY = 300
constant kCannonSpeed = 2
constant kRaiderSpeed = 10
constant kShotSpeed = 15
constant kLives = 3
constant kScore = 0
constant kRows = 5
constant kShieldCount = 0

on Game.OnStart
   Engine.ResetCamera
   Scene.ClearAll
   Particles.Clear
   HUD.Clear
   Collision.ClearRules
   Mesh.Define "Raid.Cannon", MeshBox(120, 30, 16)
   Mesh.Define "Raid.Raider", MeshBox(80, 100, 16)
   Mesh.Define "Raid.Shot", MeshBox(20, 20, 16)
   put 0 into sCannonX
   put 0 into sCannonDx
   put 0 into sCannonDy
   put 0 into sShotX
   put 0 into sShotY
   put 0 into sShotDx
   put 0 into sShotDy
   put 0 into sRaiderX
   put 0 into sRaiderY
   put 0 into sRaiderDx
   put 0 into sRaiderDy
   put 10 into sRaiderSpeed
   put 15 into sShotSpeed
   put 2 into sCannonSpeed
   put 3 into sLives
   put 0 into sScore
   put 5 into sRows
   put 0 into sLevel
   put 0 into sShields
   put false into sOver
   put Entity.Spawn("Raid.Cannon", kCannonX, kCannonY, kZ, "cyan") into sCannon
   put Entity.Spawn("Raid.Raider", kLeft, kTop, kZ, "red") into sRaider
   Raid.StartLevel 1
   Raid.ShowHUD
end Game.OnStart

on Game.OnUpdate
   if sOver then exit Game.OnUpdate
   put the keysDown into sKeys
   if 65361 is among the items of sKeys then subtract sCannonSpeed from sCannonDx
   if 65363 is among the items of sKeys then add sCannonSpeed to sCannonDx
   put max(kLeft, min(kRight, sCannonX + sCannonDx)) into sCannonX
   SetObjectPosition sCannon, sCannonX, kCannonY, kZ
   if 32 is among the items of sKeys then
      put sCannonX into sShotX
      put kCannonY into sShotY
      put 0 into sShotDx
      put 0 into sShotDy
      put Entity.Spawn("Raid.Shot", sShotX, sShotY, kZ, "yellow") into sShot
      FX.Sparks sShotX, sShotY, kZ, 6, "yellow"
   end if
   add sShotSpeed to sShotY
   SetObjectPosition sShot, sShotX, sShotY, kZ
   if sShotY <= kTop - 20 then
      Entity.Kill sShot
   end if
   if sLevel >= 1 then
      if sLevel < 5 then
         add 5 to sRaiderSpeed
      end if
   end if
   add sRaiderSpeed to sRaiderDx
   SetObjectPosition sRaider, sRaiderX, sRaiderY, kZ
   if sRaiderY >= kBottom - 20 then
      subtract 1 from sLives
      if sLives <= 0 then
         put true into sOver
         HUD.Set "Raid.Over", "GAME OVER", 300, 200, 24
      end if
   end if
   if sLevel >= 1 and sRows > 0 then
      if sRaiderX <= kLeft + 80 and sRaiderY >= kTop + 100 then
         Raid.ClearRow
      end if
   end if
end Game.OnUpdate

on Raid.StartLevel pLevel
   sLevel = pLevel
   sRows = 5
   sShields = 0
   if pLevel = 1 then
      put 0 into sRaiderSpeed
      put 0 into sShotSpeed
      put 0 into sShields
   else if pLevel = 2 then
      put 15 into sRaiderSpeed
      put 0 into sShotSpeed
      put 0 into sShields
   else if pLevel = 3 then
      put 20 into sRaiderSpeed
      put 0.3 into sShotSpeed
      put 1 into sShields
   else if pLevel = 4 then
      put 25 into sRaiderSpeed
      put 0.5 into sShotSpeed
      put 2 into sShields
   else if pLevel = 5 then
      put 30 into sRaiderSpeed
      put 0.7 into sShotSpeed
      put 3 into sShields
   end if
   Raid.ShowHUD
end Raid.StartLevel

on Raid.ShowHUD
   HUD.Set "Raid.Level", "LEVEL" && sLevel, 20, 20, 14
   HUD.Set "Raid.Score", "SCORE" && sScore, 20, 40, 14
   HUD.Set "Raid.Lives", "LIVES" && sLives, 20, 60, 14
   HUD.Set "Raid.Rows", "ROWS" && sRows, 20, 80, 14
   HUD.Set "Raid.Shields", "SHIELDS" && sShields, 20, 100, 14
end Raid.ShowHUD

on Raid.ClearRow
   if sShields > 0 then
      subtract 1 from sShields
   end if
   add 100 to sScore
   if sRows > 1 then
      subtract 1 from sRows
   end if
   if sRows = 0 then
      put true into sOver
      HUD.Set "Raid.Win", "YOU WIN", 300, 200, 24
   end if
end Raid.ClearRow

on Game.OnStop
   HUD.Remove "Raid.Level"
   HUD.Remove "Raid.Score"
   HUD.Remove "Raid.Lives"
   HUD.Remove "Raid.Rows"
   HUD.Remove "Raid.Shields"
   HUD.Remove "Raid.Over"
   HUD.Remove "Raid.Win"
end Game.OnStop
```

```
######################################################################################
## CARD SCRIPT: "Bat Duel"   BAT DUEL
## A bouncing ball between two bats. Move the left bat with arrows, press Space to score.
## CONTROLS  Left/Right arrows: move the left bat up and down
##           Space: score a point
## RULES     The right bat tracks the ball automatically. A point scores every pass.
##            Each life lasts 30 points. Losing all lives ends the game.
##            Score more than 300 points to win.
######################################################################################

global gObjectTransforms, gSceneObjects
global bPaused, bPlaying

local sLevel, sBallSpeed, sRightBatSpeed, sBatHeight, sPointsToWin
local sScore, sLives, sOver, sWin
local sLeftX, sLeftY, sLeftDx, sLeftDy
local sRightX, sRightY, sRightDx, sRightDy
local sBallX, sBallY, sBallDx, sBallDy
local sKeys
local sSpark

constant kZ = 600
constant kLeft = -450
constant kRight = 450
constant kTop = -300
constant kBottom = 300
constant kBatW = 120
constant kBatH = 20
constant kBallW = 20
constant kBallH = 20
constant kHalfBatX = kBatW / 2
constant kHalfBatY = kBatH / 2
constant kHalfBallX = kBallW / 2
constant kHalfBallY = kBallH / 2

on Game.OnStart
   Engine.ResetCamera
   Scene.ClearAll
   Particles.Clear
   HUD.Clear
   Collision.ClearRules
   Mesh.Define "Duel.LeftBat", MeshBox(kBatW, kBatH, 16)
   Mesh.Define "Duel.RightBat", MeshBox(kBatW, kBatH, 16)
   Mesh.Define "Duel.Ball", MeshBox(kBallW, kBallH, 16)
   put 1 into sLevel
   put 30 into sBallSpeed
   put 25 into sRightBatSpeed
   put 100 into sBatHeight
   put 120 into sPointsToWin
   put 0 into sScore
   put 3 into sLives
   put false into sOver
   put false into sWin
   put 0 into sLeftX
   put kBottom - sBatHeight / 2 into sLeftY
   put 0 into sLeftDx
   put 0 into sLeftDy
   put 0 into sRightX
   put 0 into sRightY
   put 0 into sRightDx
   put 0 into sRightDy
   put 0 into sBallX
   put 0 into sBallY
   put 0 into sBallDx
   put 0 into sBallDy
   put Entity.Spawn("Duel.LeftBat", sLeftX, sLeftY, kZ, "blue") into sLeftBat
   put Entity.Spawn("Duel.RightBat", sRightX, sRightY, kZ, "green") into sRightBat
   put Entity.Spawn("Duel.Ball", sBallX, sBallY, kZ, "yellow") into sBall
   Duel.StartLevel 1
   Duel.ShowHUD
end Game.OnStart

on Game.OnUpdate
   if sOver then exit Game.OnUpdate
   if sWin then exit Game.OnUpdate
   put the keysDown into sKeys
   if 65361 is among the items of sKeys then add 1 to sLeftDy
   if 65362 is among the items of sKeys then subtract 1 from sLeftDy
   if 65363 is among the items of sKeys then add 1 to sLeftDx
   if 65364 is among the items of sKeys then subtract 1 from sLeftDx
   if 32 is among the items of sKeys then Duel.ScorePoint
   Duel.UpdateLeftBat
   Duel.UpdateRightBat
   Duel.UpdateBall
   Duel.CheckCollisions
end Game.OnUpdate

on Game.OnStop
   HUD.Remove "Duel.Score"
   HUD.Remove "Duel.Lives"
   HUD.Remove "Duel.Win"
   HUD.Remove "Duel.Level"
end Game.OnStop

on Duel.StartLevel pLevel
   local sL, sBs, sRb, sBh, sPw
   if pLevel = 1 then
      put 1 into sL
      put 30 into sBs
      put 25 into sRb
      put 100 into sBh
      put 120 into sPw
   end if
   if pLevel = 2 then
      put 2 into sL
      put 35 into sBs
      put 30 into sRb
      put 120 into sBh
      put 180 into sPw
   end if
   if pLevel = 3 then
      put 3 into sL
      put 40 into sBs
      put 35 into sRb
      put 140 into sBh
      put 240 into sPw
   end if
   if pLevel = 4 then
      put 4 into sL
      put 45 into sBs
      put 40 into sRb
      put 160 into sBh
      put 300 into sPw
   end if
   if pLevel = 5 then
      put 5 into sL
      put 50 into sBs
      put 45 into sRb
      put 180 into sBh
      put 300 into sPw
   end if
   put sL into sLevel
   put sBs into sBallSpeed
   put sRb into sRightBatSpeed
   put sBh into sBatHeight
   put sPw into sPointsToWin
   put sScore into sScore
   put 3 into sLives
   put false into sOver
   put false into sWin
   put 0 into sLeftX
   put kBottom - sBh / 2 into sLeftY
   put 0 into sLeftDx
   put 0 into sLeftDy
   put 0 into sRightX
   put 0 into sRightY
   put 0 into sRightDx
   put 0 into sRightDy
   put 0 into sBallX
   put 0 into sBallY
   put 0 into sBallDx
   put 0 into sBallDy
   put Entity.Spawn("Duel.LeftBat", sLeftX, sLeftY, kZ, "blue") into sLeftBat
   put Entity.Spawn("Duel.RightBat", sRightX, sRightY, kZ, "green") into sRightBat
   put Entity.Spawn("Duel.Ball", sBallX, sBallY, kZ, "yellow") into sBall
   HUD.Set "Duel.Level", "LEVEL " && sLevel, 20, 20, 14
   HUD.Set "Duel.Score", "SCORE " && sScore, 20, 40, 14
   HUD.Set "Duel.Lives", "LIVES " && sLives, 20, 60, 14
   HUD.Set "Duel.Win", "WIN" && sWin, 20, 80, 14
end Duel.StartLevel

on Duel.UpdateLeftBat
   add sLeftDx to sLeftX
   add sLeftDy to sLeftY
   put max(kLeft, min(kRight, sLeftX)) into sLeftX
   put max(kTop, min(kBottom, sLeftY)) into sLeftY
   SetObjectPosition sLeftBat, sLeftX, sLeftY, kZ
end Duel.UpdateLeftBat

on Duel.UpdateRightBat
   local sTargetY
   sTargetY = sBallY
   if abs(sBallX - sRightX) <= kHalfBallX then
      sTargetY = sLeftY
   end if
   add sRightDx to sRightX
   add sRightDy to sRightY
   put max(kLeft, min(kRight, sRightX)) into sRightX
   put max(kTop, min(kBottom, sRightY)) into sRightY
   SetObjectPosition sRightBat, sRightX, sRightY, kZ
   if abs(sRightY - sTargetY) > 1 then
      add (sTargetY - sRightY) / 2 to sRightDy
   end if
end Duel.UpdateRightBat

on Duel.UpdateBall
   add sBallDx to sBallX
   add sBallDy to sBallY
   if abs(sBallX - sRightX) <= kHalfBallX then
      add sBallDx * -1 to sBallDx
   end if
   if abs(sBallX - sLeftX) <= kHalfBallX then
      add sBallDx * -1 to sBallDx
   end if
   if abs(sBallY - sLeftY) <= kHalfBallY then
      add sBallDy * -1 to sBallDy
   end if
   if abs(sBallY - sRightY) <= kHalfBallY then
      add sBallDy * -1 to sBallDy
   end if
   SetObjectPosition sBall, sBallX, sBallY, kZ
end Duel.UpdateBall

on Duel.CheckCollisions
   if abs(sBallX - sLeftX) <= kHalfBatX + kHalfBallX and abs(sBallY - sLeftY) <= kHalfBatY + kHalfBallY then
      add 1 to sScore
      FX.Sparks sBallX, sBallY, kZ, 6, "yellow"
   end if
   if abs(sBallX - sRightX) <= kHalfBatX + kHalfBallX and abs(sBallY - sRightY) <= kHalfBatY + kHalfBallY then
      add 1 to sScore
      FX.Sparks sBallX, sBallY, kZ, 6, "yellow"
   end if
end Duel.CheckCollisions

on Duel.ScorePoint
   add 1 to sScore
   FX.Sparks sBallX, sBallY, kZ, 8, "yellow"
end Duel.ScorePoint

on Duel.ShowHUD
   HUD.Set "Duel.Level", "LEVEL " && sLevel, 20, 20, 14
   HUD.Set "Duel.Score", "SCORE " && sScore, 20, 40, 14
   HUD.Set "Duel.Lives", "LIVES " && sLives, 20, 60, 14
   HUD.Set "Duel.Win", "WIN" && sWin, 20, 80, 14
end Duel.ShowHUD
```

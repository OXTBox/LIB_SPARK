######################################################################################
## CARD SCRIPT: "Wall.Breaker"   WALL BREAKER
## A bat keeps a ball in play while the ball knocks out rows of bricks at the top.
## CONTROLS  Left/Right arrows: move the bat    Up/Space: launch the ball
## RULES     clear every brick to win; the ball falls past the bat costs one life
######################################################################################

global gObjectTransforms, gSceneObjects
global bPaused, bPlaying

local sLevel = 1
local sBallX, sBallY, sBallVY = 0, -300, 120
local sBatX, sBatY = 0, 100
local sLives = 3
local sBricksLeft = 9
local sOver = false
local sCleared = false
local sBrickHits = 0

constant kZ = 600
constant kLeft = -450
constant kRight = 450
constant kTop = -300
constant kBottom = 300
constant kBatSpeed = 60
constant kBallSpeed = 120

on Game.OnStart
   Engine.ResetCamera
   Scene.ClearAll
   Particles.Clear
   HUD.Clear
   Collision.ClearRules
   Mesh.Define "Wall.Ball", MeshBox(30, 30, 30)
   Mesh.Define "Wall.Bat", MeshBox(40, 20, 16)
   Mesh.Define "Wall.Brick", MeshBox(90, 120, 30)
   put 1 into sLevel
   put 3 into sLives
   put 9 into sBricksLeft
   put false into sOver
   put false into sCleared
   put 0 into sBrickHits
   put Entity.Spawn("Wall.Ball", sBallX, sBallY, kZ, "cyan") into sBall
   put Entity.Spawn("Wall.Bat", sBatX, sBatY, kZ, "magenta") into sBat
   Wall.StartLevel 1
   Wall.ShowHUD
end Game.OnStart

on Game.OnUpdate
   if sOver then exit Game.OnUpdate
   put the keysDown into tKeys
   if 65361 is among the items of tKeys then subtract kBatSpeed from sBatX
   if 65363 is among the items of tKeys then add kBatSpeed to sBatX
   put max(kLeft, min(kRight, sBatX)) into sBatX
   SetObjectPosition sBat, sBatX, sBatY, kZ
   if 32 is among the items of tKeys then
      add kBallSpeed to sBallVY
      SetObjectPosition sBall, sBallX, sBallY, kZ
   end if
   add sBallVY to sBallY
   SetObjectPosition sBall, sBallX, sBallY, kZ
   if sBallY <= kTop + 10 then
      if abs(sBallX - sBatX) <= 15 then
         add 1 to sBrickHits
         if sBrickHits >= 1 then
            subtract 1 from sBricksLeft
            FX.Sparks sBallX, sBallY, kZ, 10, "orange"
            if sBricksLeft <= 0 then
               put true into sCleared
            end if
         end if
      else
         subtract 1 from sLives
         if sLives <= 0 then
            put true into sOver
            HUD.Set "Wall.Over", "GAME OVER", 300, 200, 24
         end if
      end if
   end if
   if sCleared then
      put true into sOver
      HUD.Set "Wall.Win", "LEVEL CLEARED", 300, 150, 24
   end if
end Game.OnUpdate

on Wall.StartLevel pLevel
   put pLevel into sLevel
   put 3 into sLives
   put 9 into sBricksLeft
   put 0 into sBrickHits
   put false into sCleared
   put 0 into sBallX
   put -300 into sBallY
   put 120 into sBallVY
   put 0 into sBatX
   put 100 into sBatY
   put 1 into sOver
   put 0 into sCleared
   put 0 into sBrickHits
   put Entity.Spawn("Wall.Ball", sBallX, sBallY, kZ, "cyan") into sBall
   put Entity.Spawn("Wall.Bat", sBatX, sBatY, kZ, "magenta") into sBat
   if pLevel > 1 then
      put 130 into kBallSpeed
   end if
   if pLevel > 2 then
      put 140 into kBallSpeed
   end if
   if pLevel > 3 then
      put 150 into kBallSpeed
   end if
   if pLevel > 4 then
      put 160 into kBallSpeed
   end if
   if pLevel > 5 then
      put 170 into kBallSpeed
   end if
   put 0 into sBricksLeft
   put 0 into sCleared
   put 0 into sBrickHits
   put false into sOver
end Wall.StartLevel

on Wall.ShowHUD
   HUD.Set "Wall.Score", "BRICKS LEFT" && sBricksLeft, 20, 20, 14
   HUD.Set "Wall.Lives", "LIVES" && sLives, 20, 50, 14
   HUD.Set "Wall.Level", "LEVEL" && sLevel, 20, 80, 14
   HUD.Set "Wall.Win", "WIN" && sCleared, 20, 120, 14
   HUD.Set "Wall.Over", "LOSE" && sOver, 20, 120, 14
end Wall.ShowHUD

on Game.OnStop
   HUD.Remove "Wall.Score"
   HUD.Remove "Wall.Lives"
   HUD.Remove "Wall.Level"
   HUD.Remove "Wall.Win"
   HUD.Remove "Wall.Over"
end Game.OnStop

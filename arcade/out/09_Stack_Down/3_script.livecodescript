######################################################################################
## CARD SCRIPT: "Stack Down"   STACK DOWN
## A falling four-block shape slides through arrows, then drops into the well.
## Clear full rows for score, keep the well from filling to the top.
## CONTROLS  Left/Right arrows: slide and turn the shape    Space: drop it into the well
## RULES     Each drop costs one life if it lands outside the well; a full row of four
##           blocks clears and adds points; the game ends when the well fills to the top
##           or your lives reach zero
######################################################################################

global gObjectTransforms, gSceneObjects
global bPaused, bPlaying

local sShapeX, sShapeY, sShapeDx, sShapeDy, sShapeSpeed = 0, 0, 0, 0, 1.5
local sScore = 0, sLives = 3, sWellTop = -300, sWellBottom = 300, sWellWidth = 900
local sShapeW = 4, sShapeH = 4, sDropStep = 1.5
local sLevel = 1, sRowsToFinish = 4, sJunkRows = 0, sPointsPerRow = 100
local sClearedRows = 0, sOver = false, sDropped = false

constant kZ = 600          -- every object sits at this depth
constant kLeft = -450      -- playfield edges (world units; +Y is DOWN)
constant kRight = 450
constant kWellLeft = -450
constant kWellRight = 450
constant kTop = -300
constant kBottom = 300
constant kShapeSpeed = 14

on Game.OnStart
   Engine.ResetCamera
   Scene.ClearAll
   Particles.Clear
   HUD.Clear
   Collision.ClearRules
   Mesh.Define "Stack.Shape", MeshBox(4, 4, 16)
   Mesh.Define "Stack.Well", MeshBox(900, 600, 16)
   Mesh.Define "Stack.Guide", MeshBox(100, 20, 16)
   Mesh.Define "Stack.Score", MeshBox(200, 40, 16)
   Mesh.Define "Stack.Life", MeshBox(100, 40, 16)
   put 0 into sShapeX
   put kBottom into sShapeY
   put 0 into sShapeDx
   put 0 into sShapeDy
   put 1.5 into sShapeSpeed
   put 0 into sScore
   put 3 into sLives
   put -300 into sWellTop
   put 300 into sWellBottom
   put 900 into sWellWidth
   put 4 into sShapeW
   put 4 into sShapeH
   put 1.5 into sDropStep
   put 1 into sLevel
   put 4 into sRowsToFinish
   put 0 into sJunkRows
   put 100 into sPointsPerRow
   put 0 into sClearedRows
   put false into sOver
   put Entity.Spawn("Stack.Shape", sShapeX, sShapeY, kZ, "cyan") into sShape
   put Entity.Spawn("Stack.Well", 0, kTop, kZ, "amber") into sWell
   put Entity.Spawn("Stack.Guide", 0, kTop, kZ, "blue") into sGuide
   put Entity.Spawn("Stack.Score", 20, 20, kZ, "green") into sScoreObj
   put Entity.Spawn("Stack.Life", 20, 200, kZ, "red") into sLifeObj
   Stack.StartLevel sLevel
   Stack.ShowHUD
end Game.OnStart

on Game.OnUpdate
   if sOver then exit Game.OnUpdate
   put the keysDown into tKeys
   if 65361 is among the items of tKeys then subtract kShapeSpeed from sShapeDx
   if 65363 is among the items of tKeys then add kShapeSpeed to sShapeDx
   put max(kLeft, min(kRight, sShapeX + sShapeDx)) into sShapeX
   add sShapeSpeed to sShapeY
   SetObjectPosition sShape, sShapeX, sShapeY, kZ
   if sShapeY >= kBottom - sShapeH / 2 then
      if sDropped then
         Stack.DropShape
      else
         Stack.DropShape
      end if
   end if
end Game.OnUpdate

on Stack.StartLevel pLevel
   local sTmpLevel = pLevel
   if sTmpLevel = 1 then
      put 1.5 into sDropStep
      put 4 into sRowsToFinish
      put 0 into sJunkRows
      put 100 into sPointsPerRow
   end if
   if sTmpLevel = 2 then
      put 2 into sDropStep
      put 5 into sRowsToFinish
      put 1 into sJunkRows
      put 150 into sPointsPerRow
   end if
   if sTmpLevel = 3 then
      put 2.5 into sDropStep
      put 6 into sRowsToFinish
      put 2 into sJunkRows
      put 200 into sPointsPerRow
   end if
   if sTmpLevel = 4 then
      put 3 into sDropStep
      put 7 into sRowsToFinish
      put 3 into sJunkRows
      put 250 into sPointsPerRow
   end if
   if sTmpLevel = 5 then
      put 3.5 into sDropStep
      put 8 into sRowsToFinish
      put 4 into sJunkRows
      put 300 into sPointsPerRow
   end if
end Stack.StartLevel

on Stack.DropShape
   if sShapeY >= kBottom - sShapeH / 2 then
      put true into sDropped
      SetObjectPosition sShape, sShapeX, kBottom, kZ
      if abs(sShapeX - kWellLeft) <= sWellWidth / 2 and abs(sShapeY - kWellBottom) <= sShapeH / 2 then
         add 1 to sLives
         add sPointsPerRow to sScore
         add 1 to sClearedRows
         FX.Sparks sShapeX, sShapeY, kZ, 10, "cyan"
      else
         subtract 1 from sLives
         if sLives <= 0 then
            put true into sOver
            HUD.Set "Stack.Over", "GAME OVER", 300, 200, 24
         end if
      end if
   end if
end Stack.DropShape

on Stack.ShowHUD
   HUD.Set "Stack.Score", sScore, 20, 20, 14
   HUD.Set "Stack.Life", sLives, 20, 200, 14
   HUD.Set "Stack.Well", sWellTop, 300, 14
end Stack.ShowHUD

on Game.OnStop
   HUD.Remove "Stack.Score"
   HUD.Remove "Stack.Life"
   HUD.Remove "Stack.Well"
   HUD.Remove "Stack.Over"
end Game.OnStop

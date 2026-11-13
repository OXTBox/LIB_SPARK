######################################################################################
## CARD SCRIPT: "Play.Catch"   CATCH  (example)
## A box falls from the top. Slide the bat under it. Each catch scores and speeds it up.
## CONTROLS  Left/Right arrows: move the bat    Escape: pause
## RULES     catch = +10 and the next box is faster; 3 misses = game over
######################################################################################

global gObjectTransforms, gSceneObjects
global bPaused, bPlaying

local sBat, sBox, sBatX = 0, sBoxX = 0, sBoxY = -300, sFall = 4
local sScore = 0, sMisses = 0, sOver = false

constant kZ = 600          -- every object sits at this depth
constant kLeft = -450      -- playfield edges (world units; +Y is DOWN)
constant kRight = 450
constant kTop = -300
constant kBottom = 300
constant kBatSpeed = 14

on Game.OnStart
   Engine.ResetCamera
   Scene.ClearAll
   Particles.Clear
   HUD.Clear
   Collision.ClearRules
   Mesh.Define "Catch.Bat", MeshBox(120, 16, 16)
   Mesh.Define "Catch.Box", MeshBox(30, 30, 30)
   put 0 into sBatX
   put 0 into sScore
   put 0 into sMisses
   put 4 into sFall
   put false into sOver
   put Entity.Spawn("Catch.Bat", sBatX, kBottom, kZ, "cyan") into sBat
   put Entity.Spawn("Catch.Box", 0, kTop, kZ, "yellow") into sBox
   Catch.NewBox
   Catch.ShowScore
end Game.OnStart

on Game.OnUpdate
   if sOver then exit Game.OnUpdate
   put the keysDown into tKeys
   if 65361 is among the items of tKeys then subtract kBatSpeed from sBatX
   if 65363 is among the items of tKeys then add kBatSpeed to sBatX
   put max(kLeft, min(kRight, sBatX)) into sBatX
   SetObjectPosition sBat, sBatX, kBottom, kZ
   add sFall to sBoxY
   SetObjectPosition sBox, sBoxX, sBoxY, kZ
   if sBoxY >= kBottom - 20 then
      if abs(sBoxX - sBatX) <= 75 then
         add 10 to sScore
         add 0.5 to sFall
         FX.Sparks sBoxX, sBoxY, kZ, 8, "yellow"
      else
         add 1 to sMisses
         if sMisses >= 3 then
            put true into sOver
            HUD.Set "Catch.Over", "GAME OVER", 300, 200, 24
         end if
      end if
      Catch.NewBox
      Catch.ShowScore
   end if
end Game.OnUpdate

on Catch.NewBox
   put random(kRight - kLeft) + kLeft into sBoxX
   put kTop into sBoxY
end Catch.NewBox

on Catch.ShowScore
   HUD.Set "Catch.Score", "SCORE" && sScore && "  MISSES" && sMisses, 20, 20, 14
end Catch.ShowScore

on Game.OnStop
   HUD.Remove "Catch.Score"
   HUD.Remove "Catch.Over"
end Game.OnStop

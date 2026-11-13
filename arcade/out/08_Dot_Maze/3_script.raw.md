```
######################################################################################
## CARD SCRIPT: "Dot Maze"   DOT MAZE
## A box navigates a winding corridor maze. Collect glowing dots and dodge fast chasers.
## CONTROLS  Left/Right arrows: move the player    Up/Down arrows: move the player    Space: collect dot
## RULES     Each dot +10 score; touching a chaser costs a life; collect all dots to win
######################################################################################

global gObjectTransforms, gSceneObjects
global bPaused, bPlaying

local sPlayerX, sPlayerY, sPlayerDX, sPlayerDY
local sScore, sLives, sDotsLeft, sDotsTotal
local sChaserX, sChaserY, sChaserDX, sChaserDY
local sChaserSpeed, sPlayerSpeed
local sDotX, sDotY, sDotDX, sDotDY
local sDotSpeed
local sDotIndex
local sChaserIndex
local sChasers
local sDots
local sOver, sWin
local sLevel
local tKeys
local sBrickX, sBrickY
local sBrickCount

constant kZ = 600          -- every object sits at this depth
constant kLeft = -450      -- playfield edges (world units; +Y is DOWN)
constant kRight = 450
constant kTop = -300
constant kBottom = 300
constant kStepDur = 30
constant kDotScore = 10
constant kPlayerSpeed = 60
constant kChaserSpeed = 120
constant kDotSpeed = 60
constant kLives = 3

on Game.OnStart
   Engine.ResetCamera
   Scene.ClearAll
   Particles.Clear
   HUD.Clear
   Collision.ClearRules
   Mesh.Define "Maze.Player", MeshBox(40, 40, 16)
   Mesh.Define "Maze.Dot", MeshBox(20, 20, 16)
   Mesh.Define "Maze.Chaser", MeshBox(30, 30, 16)
   put 0 into sPlayerX
   put kTop into sPlayerY
   put 0 into sScore
   put kLives into sLives
   put 0 into sDotsLeft
   put 0 into sDotsTotal
   put false into sOver
   put false into sWin
   put 1 into sLevel
   put 0 into sChaserIndex
   put 0 into sDotIndex
   put 0 into sBrickCount
   Maze.StartLevel 1
   put Entity.Spawn("Maze.Player", sPlayerX, sPlayerY, kZ, "cyan") into sPlayer
   Maze.ShowHUD
end Game.OnStart

on Game.OnUpdate
   if sOver then exit Game.OnUpdate
   if bPaused then exit Game.OnUpdate
   put the keysDown into tKeys
   if 65361 is among the items of tKeys then
      add kPlayerSpeed to sPlayerDX
   end if
   if 65363 is among the items of tKeys then
      subtract kPlayerSpeed from sPlayerDX
   end if
   if 65362 is among the items of tKeys then
      add kPlayerSpeed to sPlayerDY
   end if
   if 65364 is among the items of tKeys then
      subtract kPlayerSpeed from sPlayerDY
   end if
   add sPlayerDX to sPlayerX
   add sPlayerDY to sPlayerY
   SetObjectPosition sPlayer, sPlayerX, sPlayerY, kZ
   Maze.FollowChasers
   Maze.CollectDots
   Maze.CheckChaserContact
   Maze.CheckLevelEnd
end Game.OnUpdate

on Game.OnStop
   HUD.Remove "Maze.Score"
   HUD.Remove "Maze.Lives"
   HUD.Remove "Maze.DotsLeft"
   HUD.Remove "Maze.Level"
   HUD.Remove "Maze.Win"
end Game.OnStop

on Maze.StartLevel pLevel
   local sChaserCount = 0
   local sDotCount = 0
   local sBrickX = 0
   local sBrickY = 0
   local sBrick = 0
   local sChaser = 0
   local sDot = 0
   local sBrickXArr = []
   local sBrickYArr = []
   local sChaserArr = []
   local sDotArr = []
   local sChaserSpeed = kChaserSpeed
   local sPlayerSpeed = kPlayerSpeed

   if pLevel = 1 then
      sChaserCount = 1
      sDotCount = 5
      sBrickX = 20
      sBrickY = 10
      sBrick = 1
      sChaserSpeed = 120
      sPlayerSpeed = 60
   else if pLevel = 2 then
      sChaserCount = 2
      sDotCount = 7
      sBrickX = 20
      sBrickY = 10
      sBrick = 1
      sBrickXArr[1] = 20
      sBrickYArr[1] = 10
      sBrickXArr[2] = 30
      sBrickYArr[2] = 10
      sChaserSpeed = 120
      sPlayerSpeed = 60
   else if pLevel = 3 then
      sChaserCount = 2
      sDotCount = 9
      sBrickX = 20
      sBrickY = 10
      sBrick = 1
      sBrickXArr[1] = 20
      sBrickYArr[1] = 10
      sBrickXArr[2] = 30
      sBrickYArr[2] = 10
      sChaserSpeed = 130
      sPlayerSpeed = 60
   else if pLevel = 4 then
      sChaserCount = 3
      sDotCount = 11
      sBrickX = 20
      sBrickY = 10
      sBrick = 1
      sBrickXArr[1] = 20
      sBrickYArr[1] = 10
      sBrickXArr[2] = 30
      sBrickYArr[2] = 10
      sBrickXArr[3] = 40
      sBrickYArr[3] = 10
      sChaserSpeed = 140
      sPlayerSpeed = 60
   else if pLevel = 5 then
      sChaserCount = 3
      sDotCount = 13
      sBrickX = 20
      sBrickY = 10
      sBrick = 1
      sBrickXArr[1] = 20
      sBrickYArr[1] = 10
      sBrickXArr[2] = 30
      sBrickYArr[2] = 10
      sBrickXArr[3] = 40
      sBrickYArr[3] = 10
      sChaserSpeed = 150
      sPlayerSpeed = 60
   else
      sChaserCount = 0
      sDotCount = 0
      sBrickX = 0
      sBrickY = 0
      sBrick = 0
      sChaserSpeed = kChaserSpeed
      sPlayerSpeed = kPlayerSpeed
   end if

   put sChaserCount into sChasers
   put sDotCount into sDotsTotal
   put sDotCount into sDotsLeft
   put sChaserSpeed into sChaserSpeed
   put sPlayerSpeed into sPlayerSpeed
   put sBrickX into sBrickX
   put sBrickY into sBrickY
   put sBrick into sBrickCount
   put sBrickXArr into sBrickXArr
   put sBrickYArr into sBrickYArr
   put sChaserArr into sChaserArr
   put sDotArr into sDotArr
   put sChaserSpeed into sChaserSpeed
   put sPlayerSpeed into sPlayerSpeed
   put 0 into sDotIndex
   put 0 into sChaserIndex
   put false into sOver
   put false into sWin
   put pLevel into sLevel
   Maze.ShowHUD
end Maze.StartLevel

on Maze.FollowChasers
   local sStep = 0
   local sChaserX = 0
   local sChaserY = 0
   local sChaserDX = 0
   local sChaserDY = 0
   local sChaser = 0
   local sChaserSpeed = 0
   local sChaserArr = []
   local sChaserIndex = 0
   local sChaserCount = 0
   local sChasers = 0

   if sChasers = 0 then
      put 0 into sChasers
      return
   end if

   repeat with sChaserIndex = 1 to sChasers
      sChaser = sChaserIndex
      sChaserX = sChaserArr[sChaserIndex]
      sChaserY = sBrickYArr[sChaserIndex]
      sChaserDX = 0
      sChaserDY = 0
      sChaserSpeed = sChaserSpeedArr[sChaserIndex]
      put sChaserX into sChaserX
      put sChaserY into sChaserY
      put 0 into sChaserDX
      put 0 into sChaserDY
      put sChaserSpeed into sChaserSpeed
      put sChaser into sChaser
      put sChaserIndex into sChaserIndex
      put sChaserX into sChaserX
      put sChaserY into sChaserY
      put 0 into sChaserDX
      put 0 into sChaserDY
      put sChaserSpeed into sChaserSpeed
      put sChaser into sChaser
      put sChaserIndex into sChaserIndex
      put sChaserX into sChaserX
      put sChaserY into sChaserY
      put 0 into sChaserDX
      put 0 into sChaserDY
      put sChaserSpeed into sChaserSpeed
      put sChaser into sChaser
      put sChaserIndex into sChaserIndex
      put sChaserX into sChaserX
      put sChaserY into sChaserY
      put 0 into sChaserDX
      put 0 into sChaserDY
      put sChaserSpeed into sChaserSpeed
      put sChaser into sChaser
      put sChaserIndex into sChaserIndex
      put sChaserX into sChaserX
      put sChaserY into sChaserY
      put 0 into sChaserDX
      put 0 into sChaserDY
      put sChaserSpeed into sChaserSpeed
      put sChaser into sChaser
      put sChaserIndex into sChaserIndex
      put sChaserX into sChaserX
      put sChaserY into sChaserY
      put 0 into sChaserDX
      put 0 into sChaserDY
      put sChaserSpeed into sChaserSpeed
      put sChaser into sChaser
      put sChaserIndex into sChaserIndex
      put sChaserX into sChaserX
      put sChaserY into sChaserY
      put 0 into sChaserDX
      put 0 into sChaserDY
      put sChaserSpeed into sChaserSpeed
      put sChaser into sChaser
      put sChaserIndex into sChaserIndex
      put sChaserX into sChaserX
      put sChaserY into sChaserY
      put 0 into sChaserDX
      put 0 into sChaserDY
      put sChaserSpeed into sChaserSpeed
      put sChaser into sChaser
      put sChaserIndex into sChaserIndex
      put sChaserX into sChaserX
      put sChaserY into sChaserY
      put 0 into sChaserDX
      put 0 into sChaserDY
      put sChaserSpeed into sChaserSpeed
      put sChaser into sChaser
      put sChaserIndex into sChaserIndex
      put sChaserX into sChaserX
      put sChaserY into sChaserY
      put 0 into sChaserDX
      put 0 into sChaserDY
      put sChaserSpeed into sChaserSpeed
      put sChaser into sChaser
      put sChaserIndex into sChaserIndex
      put sChaserX into sChaserX
      put sChaserY into sChaserY
      put 0 into sChaserDX
      put 0 into sChaserDY
      put sChaserSpeed into sChaserSpeed
      put sChaser into sChaser
      put sChaserIndex into sChaserIndex
      put sChaserX into sChaserX
      put sChaserY into sChaserY
      put 0 into sChaserDX
      put 0 into sChaserDY
      put sChaserSpeed into sChaserSpeed
      put sChaser into sChaser
      put sChaserIndex into sChaserIndex
      put sChaserX into sChaserX
      put sChaserY into sChaserY
      put 0 into sChaserDX
      put 0 into sChaserDY
      put sChaserSpeed into sChaserSpeed
      put sChaser into sChaser
      put sChaserIndex into sChaserIndex
      put sChaserX into sChaserX
      put sChaserY into sChaserY
      put 0 into sChaserDX
      put 0 into sChaserDY
      put sChaserSpeed into sChaserSpeed
      put sChaser into sChaser
      put sChaserIndex into sChaserIndex
      put sChaserX into sChaserX
      put sChaserY into sChaserY
      put 0 into sChaserDX
      put 0 into sChaserDY
      put sChaserSpeed into sChaserSpeed
      put sChaser into sChaser
      put sChaserIndex into sChaserIndex
      put sChaserX into sChaserX
      put sChaserY into sChaserY
      put 0 into sChaserDX
      put 0 into sChaserDY
      put sChaserSpeed into sChaserSpeed
      put sChaser into sChaser
      put sChaserIndex into sChaserIndex
      put sChaserX into sChaserX
      put sChaserY into sChaserY
      put 0 into sChaserDX
      put 0 into sChaserDY
      put sChaserSpeed into sChaserSpeed
      put sChaser into

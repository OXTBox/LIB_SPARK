@echo off
title Spark - game designs (close this window to stop)
rem Spark writes a concept and a 5-level table for each new idea in
rem   \\wsl$\Ubuntu\home\igame3d\projects\LIB_LLMIN\LIB_SPARK\GAME_IDEAS.txt
rem It starts LM Studio and loads Spark by itself. Close this window to stop.
cd /d %USERPROFILE%
wsl.exe -d Ubuntu -- bash /home/igame3d/projects/LIB_SPARK/run_designs.sh
echo.
pause

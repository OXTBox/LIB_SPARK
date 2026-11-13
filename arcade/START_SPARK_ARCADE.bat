@echo off
title Spark - arcade games test (close this window to stop)
rem Double-click to start or resume Spark writing the twelve arcade games.
rem 20 minutes of work, 15 seconds of rest (change pace.txt any time). Close this window to stop.
cd /d %USERPROFILE%
wsl.exe -d Ubuntu -- bash /home/igame3d/projects/LIB_SPARK/arcade/run_arcade.sh
echo.
pause

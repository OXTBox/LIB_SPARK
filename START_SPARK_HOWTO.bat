@echo off
title Spark - LIB_HOWTO outline (close this window to stop)
rem Spark outlines the step-by-step game programming tutorials (LIB_SPARK\howto\topics.tsv)
rem and maps every game to the topics it teaches. Result: LIB_SPARK\howto\OUTLINE.md
rem It starts LM Studio and loads Spark by itself. Close this window to stop; start again to resume.
cd /d %USERPROFILE%
wsl.exe -d Ubuntu -- bash /home/igame3d/projects/LIB_SPARK/howto/run_howto.sh
echo.
pause

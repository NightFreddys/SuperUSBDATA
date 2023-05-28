@echo off 
echo Welcome to SuperUSB! 
echo Try using the "home" command and you're going to the main menu! 
:loop 
set /p commd=SuperUSB Welcome Game: 
if %commd% == home (exit) else (goto loop)

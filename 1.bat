@echo off \n echo Welcome to SuperUSB! \n echo Try using the "home" command and you're going to the main menu! \n :loop \n set /p commd=SuperUSB Welcome Game: \n if %commd% == home (exit) else (goto loop)

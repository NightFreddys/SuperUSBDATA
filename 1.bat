@echo off\necho Welcome to SuperUSB!\necho Try using the "home" command and you're going to the main menu!\n:loop\nset /p commd=SuperUSB Welcome Game:\nif %commd% == home (exit) else (goto loop)

loop = True
well1 = 'Try using the "home" command and you'
well2 = "'re going to the main menu!"
print("Welcome to SuperUSB!")
print(well1+well2)
while loop:
    commd = input("SuperUSB Welcome Game: ")
    if commd=="home":
        loop=False

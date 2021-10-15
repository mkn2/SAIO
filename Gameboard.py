
userInput1 = input("rows vertical (ex.12345678): ")
userInput2 = input("rows horizontal(ex. 8): ")

userInput1 = int(userInput1)
userInput2 = int(userInput2)

for dot in range(userInput1):
    print(".  " * userInput2)




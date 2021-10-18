

import random
n = random.randint(0,10)


Number = n

userInput = ""


while userInput != n:
   userInput = int(input("Input a random number between 0 and 10: "))
   if userInput != n:
    print("Wrong!")
   else:
     print("Congrats!")
     break
   if userInput >= n:
      print("Lower")
   elif userInput <= n:
      print("Higher")
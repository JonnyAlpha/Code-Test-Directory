# Program to test writing all of the values of a variable to a text file
# Tested successfully 10 Dec 23 

import random
randomlist = []
with open("output.txt", "w") as file:
          
    for i in range(0,5):
        number = random.randint(1, 30)
        randomlist.append(number)
        print(randomlist)
        file.write(str(number) + "\n")



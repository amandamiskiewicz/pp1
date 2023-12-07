'''22.	Create a program that writes 50 random integers between 100 and 999 to a text file, 
each number on a separate line.'''

import random
with open("RandomNumbers.txt","w") as file:
    for i in range(50):
        file.write(str(random.randint(100,999)))
        if i!=49:
            file.write("\n")

#30.In many games, the numbers one and six on dice have special meaning. 
#Write a program that displays the number of dice rolled 
#and the value True if the number rolled is 1 or 6. Sample result:
#Dice rolled: 4
#Special number: False

import random
x=random.randrange(1,7)
def dice():
    if x==1 or x==6:
        return True
    else:
        return False

print(f"Dice rolled: {x}\nSpecial number: {dice()}")

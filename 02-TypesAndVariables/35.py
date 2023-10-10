#A tree may be cut down if its diameter is at least 50 cm. 
#Write a program that, based on the circumference of the tree entered from the keyboard, 
#calculates and displays the value True if the tree can be cut down, 
#or display the value False otherwise. Sample result:
#Enter tree circumference: …
#Tree can be cut down: …

import math
pi=math.pi
circumference=float(input("Enter tree circumference: "))
diameter=circumference/pi

def cut():
    if diameter>=50:
        return True
    else:
        return False

print(f"Tree can be cut down: {cut()}")




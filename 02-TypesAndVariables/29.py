#Each programming language provides a set of functions that you can use in your programs. 
#One of them is a function that returns a random number. 
#Write a program that displays results of three dice rolls and the sum of dice rolled. 
#Apply a random number generator:
#https://docs.python.org/3/library/random.html
import random
x=random.randrange(1,7)
y=random.randrange(1,7)
z=random.randrange(1,7)
print(f"rzut 1: {x}, \nrzut 2: {y}, \nrzut 3: {z}, \nsuma: {x+y+z}")

##(a,b-1)
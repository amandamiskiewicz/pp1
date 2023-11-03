'''24. In a separate module, define a function that checks if the number is within the range <x, y>. 
The function returns a boolean value. Then, create a program and use the function you defined. Sample result:
A number: 7
Number 7 in the range <2,15>: yes 
'''
import range
num=int(input("enter number: "))
x=int(input("x value: "))
y=int(input("y value: "))
if range.check_range(x,y,num)==True:
    print(f"Number {num} in the range <{x},{y}>: yes ")
else:
    print(f"Number {num} in the range <{x},{y}>: no ")


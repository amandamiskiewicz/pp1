#39.	The variables a and b contain the dimensions of the sides of the rectangle. 
#Write a program that creates the following rectangle with dimensions a and b. 
#Sample result for a = 4 and b = 15:
#***************
#*             *
#*             *
#***************

a=5
b=112
print(b*"*")
for x in range(a-2):
    print("*"+(b-2)*" "+"*")
print(b*"*")

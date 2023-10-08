#####
# Calculation of circle area and circumference 
##
import math
# determine radius and PI
radius=int(input("podaj r: "))
pi=round(math.pi,2)
# calculate area 
area=pi*radius**2
# calculate circumference 
circumference=2*pi*radius
# display results
print(f"area is {area} and circumference is {circumference}")

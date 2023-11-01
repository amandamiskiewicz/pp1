#31.	Let x and y denote the coordinates of a point on the plane. 
#Write a program that determines in which quadrant of the coordinate system the point P (x, y) 
#is located or on which axis it is located, or that it is located in the position (0,0) of the coordinate system. 
#Sample result:
x = -6
y = 2
#Point P(5,2) is in the first quadrant of the coordinate system

if x>0 and y>0:
    print(f"Point P({x},{y}) is in the first quadrant of the coordinate system")
elif x<0 and y>0:
    print(f"Point P({x},{y}) is in the second quadrant of the coordinate system")    
elif x<0 and y<0:
    print(f"Point P({x},{y}) is in the third quadrant of the coordinate system")    
elif x>0 and y<0:
    print(f"Point P({x},{y}) is in the fourth quadrant of the coordinate system")  
elif x==0 and y==0:
    print(f"Point P({x},{y}) is in the position (0,0)")    
elif x==0:
    print(f"Point P({x},{y}) is on y-axis")    
elif y==0:
    print(f"Point P({x},{y}) is on x-axis")    
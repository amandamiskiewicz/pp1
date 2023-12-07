'''29.	The grades.txt file contains student’s grades. Create the file in any text editor 
with the content as below:
Name: Peter
Grades: 3.5, 4.0, 5.0, 4.5, 3.5, 3.0, 5.0
Then, create a program that calculates the arithmetic mean of student’s grades.
'''

import re

file = open("grades.txt" , "r")
grades = re.findall("\d\.\d",file.read())
sum=0
for i in grades:
    sum+=float(i)
mean = sum/len(grades)
print(f"{round(mean,2)}")
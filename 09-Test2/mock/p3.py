'''(p3.py) A two-dimensional array contains the same number of rows and columns. 
Create a function f(array2D) that, for the given two-dimensional array array2D, 
returns True when the sum of the values in each row of the array is equal to the sum of the values 
in the corresponding column (e.g., the sum of the values in row 3 is equal to the sum of the values in column 3) , 
and False otherwise. Example:
f([[3,7,2],[4,2,5],[5,2,1]])  True
f([[3,7,2],[4,2,5],[9,2,1]])  False
'''

array2D=[[3,7,2],[4,2,5],[5,2,1]]
def f(array2D):
    flag = 0
    index=-1
    sum_row=0
    for row in array2D:
        sum_row=sum(row)
        index+=1
        sum_column=0
        for row in array2D:
            sum_column+=row[index]
        if sum_row==sum_column:
            flag+=1
    if flag==len(array2D):
        return True
    else:
        return False

print(f(array2D))
print(f([[3,7,2],[4,2,5],[9,2,1]]))

        
'''48.	A function create_2d_arr(x,y) creates and returns two dimensional array with values of 0. 
Create a program and the function. Then create a two-dimensional array with dimensions of 3 by 5. 
Display the created array.'''

def create_2d_arr(x,y):
    arr=[]
    for i in range(x):
        ins_arr=[]
        for j in range(y):
            ins_arr.append("0")
        arr.append(ins_arr)
    return arr

print(create_2d_arr(3,5))
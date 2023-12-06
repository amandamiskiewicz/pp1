'''56.	Create a function that convert two-dimensional (2D) array into 1D. 
Then create a program that displays 1D array for the following 2D arrays.
a.	2 3
1 5 
b.	5 0 3 7 5
9 0 9 1 2
c.	2 1
3 5
7 4
2 6
'''

a=[[2,3],
   [1,5]]


res=[]
for i in range(len(a)):
    for j in range(len(a[0])):
        res.append(a[i][j])

print(res)
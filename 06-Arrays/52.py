'''52.	A two-dimensional array of the size 3 by 5 contains integer numbers. 
Create a program that swaps the first and the last column. 
Display array values in rows and columns before and after changes.'''

arr = [
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15]
]

a=[]
b=[]
for i in arr:
    a.append(i[0])
    b.append(i[-1])

print(a)
print(b)

ind=0
for i in arr:
    i[0]=b[ind]
    ind+=1

print(arr)

ind=0
for i in arr:
    i[-1]=a[ind]
    ind+=1

print(arr)
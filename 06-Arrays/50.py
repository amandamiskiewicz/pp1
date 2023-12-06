'''50.	An array contains integer numbers: [[-38, 19], [5,40],[-7,11],[29,16]]. 
Create a program that finds the smallest and largest values in the array 
and in which row and column they are located. '''

arr = [[-38, 19], [5,40],[-7,11],[29,16]]
m=0
for row in arr:
    if max(row)>m:
        m=max(row)
print(m)

s=min(arr[0])
for row in arr:
    if min(row)<s:
        s=min(row)
print(s)
    
r=0
for row in arr:
    if m in row:
        print(r,row.index(m))
    r+=1


r=0
for row in arr:
    if s in row:
        print(r,row.index(s))
    s+=1


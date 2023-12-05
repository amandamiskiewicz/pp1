'''14.	An array contains values: [[2,5,4],[9,0,3]]. Create a program that displays:
a.	the array
b.	size of the array (number of rows and columns)
c.	value 5 from the array
d.	value 3 from the array
e.	second row of the array as below:
9 0 3
Sample result:
[[2,5,4],[9,0,3]]
2 3
5
3
9 0 3
'''

arr=[[2,5,4],[9,0,3]]
print("a: ", arr)
print("b: ", len(arr), len(arr[0]))
print("c: ", arr[0][1])
print("d: ", arr[1][2])
#e 
print("e: ",end="")
for a in arr[1]:
    print(a,end=" ")

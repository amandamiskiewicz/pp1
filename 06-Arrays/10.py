'''10.	An array contains values: 1, 2, 3, 4, 5. Create a program that modifies the array values. Display the array after each change.
a.	subtract one from the first element of the array
b.	increase the last array element by 4
c.	multiple the middle array element by 2
Sample result:
Array: [1,2,3,4,5]
Array: [0,2,3,4,5]
Array: [0,2,3,4,9]
Array: [0,2,6,4,9]
'''

arr=[1,2,3,4,5]
#a
arr[0]-=1
print("a: ", arr)
#b
arr[-1]+=4
print("b: ", arr)
#c
arr[len(arr)//2]*=2
print("c: ", arr)
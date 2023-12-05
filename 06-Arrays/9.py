'''9.	An array contains values: 2, 3, 7, 5, 4. Create a program that displays:
a.	the array
b.	number of elements
c.	first value
d.	second value
e.	last value
f.	last but one value (do not use negative index values)
g.	sum of the first and last value
h.	middle value
i.	all array values separated by a single space (use a loop statement)
Sample result:
Array: [2,3,7,5,4]
No. of elements: 5
First value: 2
Second value: 3
…
…
Tip: to read the last value of an array:
array[len(array)-1] or array[-1]
'''


arr=[2,3,7,5,4]
print("a :",arr) 
print("b :",len(arr)) 
print("c :",arr[0]) 
print("d :",arr[1])
print("e :",arr[-1]) 
print("f :",arr[len(arr)-1]) 
print("g :",arr[0]+arr[-1]) 
print("h :",arr[len(arr)//2]) 
#i
for i in arr:
    print(i, end=" ")


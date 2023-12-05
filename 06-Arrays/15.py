'''15.	An array contains values: [[1,3,5],[8,7,2]]. Write a program that calculates and displays:
a.	Sum of the first element in the first row and the last element in the last row
b.	Sum of the elements in the middle column
c.	Sum of the elements in the last row
Sample result:
3
10
17
'''

arr = [[1,3,5],[8,7,2]]
print("a: " , arr[0][0]+arr[-1][-1])
print("b: ", arr[0][len(arr)//2]+arr[1][len(arr)//2])
#c
sum=0
for a in arr[-1]:
    sum+=a
print("c: ", sum)
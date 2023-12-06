'''39.	Write a program to separate even and odd numbers of a given array of integers. 
Put all even numbers first, and then odd numbers.'''

arr1 = [42, 17, 93, 55, 30, 85, 10, 68, 27, 77]
arr2=[]

for a in arr1:
    if a%2==0:
        arr2.append(a)

for a in arr1:
    if a%2!=0:
        arr2.append(a)

print(arr2)
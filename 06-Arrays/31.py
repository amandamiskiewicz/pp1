'''31.	Create a program that displays all unique elements in an array. Sample result:
Array: 2 3 2 5 8 1 9 8
Unique elements: 3 5 1 9
'''

arr = [2, 3, 2, 5, 8, 1, 9, 8]

res=""
for a in arr:
    if arr.count(a)==1:
        res=res+str(a)+", "

print(res[:-2])

'''12.	An array contains integer numbers: [34,7,19,4,21,8]. 
Create a program that calculates and displays the number of even values in the array. Use the ‘for’ loop statement. Sample result:
arr = [34,7,19,4,21,8]
even = 0
for a in arr:
    if …:
        even = even + 1
print(…)
'''
arr = [34,7,19,4,21,8]
even = 0
for a in arr:
    if a%2==0:
        even = even + 1
print(even)
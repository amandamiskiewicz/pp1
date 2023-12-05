'''20.	An array contains integer numbers: 34,7,19,4,21,8. 
Create a program that calculates and displays the number of even values in the array. 
Use the ‘while’ loop statement'''
arr = [34,7,19,4,21,8]
stop = len(arr)
element = len(arr)-1
sum = 0
while stop>0:
    if arr[element]%2==0:
        sum+=1
    element-=1
    stop-=1

print(sum)
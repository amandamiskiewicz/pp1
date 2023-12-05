'''18.	An array contains values: [[True,False],[True,True],[False,False]]. 
Create a program that changes values of an array to the opposite. Use a loop statement. Sample result:
Before: [[True,False],[True,True],[False,False]]
After:  [[False,True],[False,False],[True,True]]
'''

arr = [[True, False], [True, True], [False, False]]

print("Before:", arr)
# Iterate over the rows and elements of the array
for i in range(len(arr)):
    for j in range(len(arr[i])):
        # Change the boolean value to its opposite
        arr[i][j] = not arr[i][j]

# Display the modified array
print("After:", arr)

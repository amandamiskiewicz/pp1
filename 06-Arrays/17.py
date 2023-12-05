'''17.	An array contains values: [[0,0,0],[0,0,0],[0,0,0]]. 
Create a program that replaces the values of the main diagonal with 1. 
Use proper loop statements. Display the modified array. Sample result:
1 0 0
0 1 0
0 0 1
'''

arr = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Iterate over the indices of the array
for i in range(len(arr)):
    # Set the main diagonal elements to 1
    arr[i][i] = 1

# Display the modified array
for row in arr:
    for element in row:
        print(element, end=' ')
    print()

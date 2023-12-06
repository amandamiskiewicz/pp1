'''49.	An array contains values: [[0,0,0,0,0],0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]. 
Create a program that modifies the array values to create a multiplication table as below. 
Use loop statements. Display the array.
1  2  3  4  5
2  4  6  8 10
3  6  9 12 15
4  8 12 16 20
5 10 15 20 25
'''

arr=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

# Initialize the array
array = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

# Fill in the array with multiplication table values
for i in range(1, 6):
    for j in range(1, 6):
        array[i-1][j-1] = i * j

print(array)

# Display the array
for row in array:
    for element in row:
        print(f"{element:2}", end=" ")  # Format the output to align the numbers
    print()

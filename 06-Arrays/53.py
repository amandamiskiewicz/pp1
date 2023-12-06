'''53.	In mathematics, a matrix is a rectangular array or table of numbers, symbols, or expressions, 
arranged in rows and columns, e.g.:
-7  12 38
41 -19 11
Create a function identity_matrix(n) that returns an identity matrix (2D array) of size n 
(https://en.wikipedia.org/wiki/Identity_matrix). 
Then, create a function that displays a 2D array in rows and columns. 
Finally, create a program that displays three identity matrices with dimensions of 3, 5 and 8. Sample result:
1 0 0 0 0
0 1 0 0 0
0 0 1 0 0
0 0 0 1 0
0 0 0 0 1
'''

def identity_matrix(n):
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            if i == j:
                row.append(1)
            else:
                row.append(0)
        matrix.append(row)
    return matrix

def display_matrix(matrix):
    for row in matrix:
        for element in row:
            print(element, end=" ")
        print()

# Display identity matrices
for size in [3, 5, 8]:
    print(f"Identity Matrix of size {size}:")
    matrix = identity_matrix(size)
    display_matrix(matrix)
    print()

print(identity_matrix(3))
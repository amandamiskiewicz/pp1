'''54.	Create a function transpose_matrix(m) that returns transposed matrix m:
https://en.wikipedia.org/wiki/Transpose 
'''

def transpose_matrix(m):
    rows = len(m)
    cols = len(m[0])

    transposed = []
    for i in range(cols):
        transposed_row = []
        for j in range(rows):
            transposed_row.append(m[j][i])
        transposed.append(transposed_row)

    return transposed

def display_matrix(matrix):
    for row in matrix:
        for element in row:
            print(element, end=" ")
        print()

# Test the function with your array
arr = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]

transposed_arr = transpose_matrix(arr)
print(transposed_arr)

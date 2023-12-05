'''22.	Create a program that computes the second power of each array element. Sample result:
Array: 8 2 5 1 9
2nd power: 64 4 25 1 81
'''

def second_power(arr):
    res = []
    for element in arr:
        # Calculate the second power of each element
        res.append(element ** 2)
    return res

# Test the function with the given array
result = second_power([8, 2, 5, 1, 9])

# Display the results
print("Array:", ' '.join(map(str, [8, 2, 5, 1, 9])))
print("2nd power:", ' '.join(map(str, result)))


print(second_power([8,2,5,1,9]))
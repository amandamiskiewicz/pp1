'''32.	Define a function occurs(number, array) that returns True if a given number is present in an array. 
Then create a program that checks whether the number entered from the keyboard 
is present in the array [15, 38, 7, 23, 14]. Sample result:
Number: 23
Array: 15 38 7 23 14
Result: number 23 appears in the array
'''

def occurs(number, array):
    return number in array

number=int(input("Number: "))

arr=[15, 38, 7, 23, 14]

print(f"Array: {arr}")

if occurs(number,arr)==True:
    print(f"Result: number {number} appears in the array")
else:
    print(f"Result: number {number} doesnt appear in the array")


'''38.	Write a program that, for the given array of real numbers, 
displays the number of elements that are greater than the given value entered from the keyboard.'''

arr1 = [42, 17, 93, 55, 30, 85, 10, 68, 27, 77]
arr2=[1,2,3,4,5]

def greater(n,array):
    sum=0
    for a in array:
        if a>n:
            sum+=1
    return sum

n=int(input("num: "))
print(greater(n,arr1))
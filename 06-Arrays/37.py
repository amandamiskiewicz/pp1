'''37.	Create a module MyArrays containing functions to operate on an array of numbers:
a.	A function that returns the second largest element in an array
b.	A function that returns the difference between the largest and smallest values in an array
c.	A function that returns the median of numbers in an array. Do not use built-in functions. 
The median is the middle value in the ordered sequence of numbers:
https://en.wikipedia.org/wiki/Median#/media/File:Finding_the_median.png 
d.	A function that returns a two-element array containing the smallest and largest values in an array
e.	A function that returns array elements as a string, separated by the minus sign
Then, write a program that for the sequence of numbers:
7,3,8,5,2
calculates and displays results. Sample result:
Numbers: 7,3,8,5,2
Second largest number: 7 
Median: 5
Smallest and largest number: 2,8
Numbers as a string: 7-3-8-5-2
'''
import statistics

arr=[7,3,8,5,2]

def second_largest(array):
    array.sort()
    return array[-2]

print(second_largest(arr))

def diff(array):
    array.sort()
    return array[-1]-array[0]

print(diff(arr))

print(statistics.median(arr))

def two(array):
    array.sort()
    return [arr[0],arr[-1]]

print(two(arr))

def minus(array):
    res=""
    for i in array:
        res=res+str(i)+"-"
    return res[:-1]

arr=[7,3,8,5,2]
print(minus(arr))
'''28.	Define a function compare(array1, array2) that returns True if both arrays are the same or False otherwise.  
Two arrays are the same if they have the same number of elements and values of elements in cells of arrays 
with the same index are equal. Then create a program and try to compare the following arrays: 
a.	["water","book","sky"]   ["water","book","sky"]
b.	[True,False]   [True,False,True]
c.	[5,3,1]   [5,3,1]
d.	[3,2,1]   [3,2]
Display both arrays and the result of comparison. Sample result:
Array1: water book sky
Array2: water book sky
Comparison: arrays are the same
'''

def compare(array1, array2):
    return array1==array2

arr1=["water","book","sky"]
arr2=["water","book","sky"]

arr3=[True,False]   
arr4=[True,False,True]

arr5=[5,3,1]   
arr6=[5,3,1]

arr7=[3,2,1]   
arr8=[3,2]

print(compare(arr7,arr8))

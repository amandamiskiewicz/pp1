'''41.	Write a program that checks whether the first array is a subset of the second one 
(whether all elements of the first array appear in the second array).'''

arr1=[1,2,3]
arr2=[1,2,3,4,5]
arr3=[4,5,6]
arr4=[1,3,6]

for i in arr4:
    flag=0
    if i in arr2:
        continue
    else:
        flag+=1

if flag>0:
    print(False)
else:
    print(True)
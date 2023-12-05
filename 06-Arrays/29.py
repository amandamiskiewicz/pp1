'''29.	Two arrays contain the following integer numbers [4,36,12,28,9,44,5] and [5,1,36]. 
Create a program that displays the numbers from the first array that do not appear in the second array.'''

arr1=[4,36,12,28,9,44,5]
arr2=[5,1,36]

res=""
for i in arr1:
    if i in arr2:
        res=res
    else:
        res=res+str(i)+" \n"


res=res.split()
res = [int(x) for x in res]

print(res)
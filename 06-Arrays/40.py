'''40.	The array contains integer 8 numbers in the range 1 to 999. 
Write a program that displays elements of the array formatted as below.
-----------------------------------------
|   1|  23|   5| 382|   1|  17|   4| 906|
-----------------------------------------
'''
import random as r

arr=[r.randint(1,999) for i in range(8)]


x="-----------------------------------------"
#print(len(x))

print(41*"-")
res="|"
for a in arr:
    if len(str(a))==1:
        res=res+"   "+str(a)+"|"
    elif len(str(a))==2:
        res=res+"  "+str(a)+"|"
    elif len(str(a))==3:
        res=res+" "+str(a)+"|"
print(res)
print(41*"-")
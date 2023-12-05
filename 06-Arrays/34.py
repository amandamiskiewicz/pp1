'''34.	Write a program that displays the tuple (10,20,30,40,50) in reverse order. Sample result:
Tuple: 10,20,30,40,50
Reverse order: 50,40,30,20,10
'''

mytuple=(10,20,30,40,50)


ind=len(mytuple)-1
res=""
for i in mytuple:
    res=res+str(mytuple[ind])+" "
    ind-=1

print(res)
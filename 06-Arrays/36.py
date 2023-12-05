'''36.	Write a program that counts the number of occurrences of any value from a tuple. Sample result:
Tuple: 50,20,40,50,30,50
Value: 50
Number of occurrences: 3
'''

def occurs(n,tup):
    return tup.count(n)

tup=(50,20,40,50,30,50)
print(occurs(50,tup))

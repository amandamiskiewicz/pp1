'''32.	Define the function f(n1,n2,n3), which returns True if at least one of the numbers n1,n2,n3 is negative 
or False otherwise. Sample result:
f(11,6,-4) returns True
f(5,4,14) returns False
'''

def f(n1,n2,n3):
    l=[n1,n2,n3]
    for i in l:
        if i<0:
            return True
    return False
        
        
print(f(11,6,-4))
print(f(5,4,14))
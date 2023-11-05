'''37.	Define the function f(n), which returns the n-th value of the Fibonacci sequence. 
The sequence is defined as follows: the first value of the sequence is 0, the second value is 1. 
Each subsequent value is the sum of the previous two. Sample result:
f(5) returns 3
f(9) returns 21
'''

def f(n):
    first=0
    second=1
    next=first+second
    for i in range(n-3):
        first=second
        second=next
        next=first+second
    return next

if __name__=="__main__":
    print(f(5))
    print(f(9))

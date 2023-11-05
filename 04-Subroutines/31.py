'''31.	Define the function f(x,y) that returns the number of negative even numbers in the range <x,y>. 
Sample result:
f(-7,8) returns 3
f(-1,11) returns 0
'''

def f(x,y):
    sum=0
    for i in range(x,y+1):
        if i%2==0 and i<0:
            sum+=1
    return sum

print(f(-7,8))
print(f(-1,11))
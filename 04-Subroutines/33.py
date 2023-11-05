'''33.	Define a function f(n) that returns a string of n asterisks, separated by a slash sign. Sample result:
f(4) returns "*/*/*/*"
f(1) returns "*"
'''

def f(n):
    msg=""
    for i in range(n):
        msg=msg+ "*"
        if i < n - 1:
            msg = msg + "/"
    return msg

print(f(4))
print(f(1))
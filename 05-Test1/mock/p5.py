'''(p5.py) The binary system uses two symbols to represent a number: 0 and 1. 
Define a function f(binary_number) that returns True if the given notation is a valid binary number, 
or false otherwise. Example:
f("101101") returns True
f("1311a10100") returns False
'''

def f(binary_number):
    for i in binary_number:
        if i!="0" and i!="1":
            return False
    return True

if __name__=="__main__":
    print(f("101101"))
    print(f("1311a10100"))
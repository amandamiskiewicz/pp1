'''(p3.py) A text contains any number of words. 
Define a function f(name) that returns the acronym (first letters of all words). 
Sample result:
f("Internet of Things") returns "IoT"
f("For Your Information") returns "FYI"
f("Python") returns "P"
'''

def f(name):
    msg=""
    x=name.split()
    for i in x:
        msg=msg+i[0]
    return msg

if __name__ == "__main__":
    print(f("Internet of Things"))
    print(f("For Your Information"))
    print(f("Python"))
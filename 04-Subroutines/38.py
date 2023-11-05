'''38.	A palindrome is an expression that sounds the same when read backwards. 
Define a function f(palindrome) that returns True if the expression is a palindrome or False otherwise. 
Sample result:
f("radar") returns True
f("12-11-21") returns True
f("book") returns False
'''

def f(palindrome):
    reversed_text = palindrome[::-1]
    if palindrome==reversed_text:
        return True
    else:
        return False

if __name__=="__main__":
    print(f("radar"))
    print(f("12-11-21"))
    print(f("book"))


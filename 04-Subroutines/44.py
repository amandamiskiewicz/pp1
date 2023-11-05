'''44.	A valid password should consist of at least six different characters. 
Define a function f(password) that returns True if the password is correct or False otherwise. 
Sample result:
f("ax15") returns False
f("book123") returns False
f("A2water3") returns True
f("qwerty") returns True
f("") returns False
'''

def f(password):
    if len(password)>=6:
        for i in password:
            if password.count(i) > 1:
                return False
        return True
    return False

if __name__=="__main__":
    print(f("awdfghjw"))
    print(f("ax15"))
    print(f("book123"))
    print(f("A2water3"))
    print(f("qwerty"))
    print(f(""))
    print(f("wokljdii"))
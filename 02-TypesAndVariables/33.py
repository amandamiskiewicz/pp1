#The password is valid if it is at least 8 characters long. 
#Write a program that checks whether the password read from the keyboard is correct. 
#Sample result:
#Enter password: qwertyXX
#Password is valid: True

password=input("enter password: ")
def validation():
    if len(password)>=8:
        return True
    else:
        return False

print(f"Password is valid: {validation()}")

#len(smh)
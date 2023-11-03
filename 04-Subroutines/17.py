#17.Define the function different(n1,n2,n3), which returns True if all three numbers n1,n2,n3 are different 
#or False otherwise. Then, write a program that reads three integers from the keyboard. 
#Checks whether the numbers are different. Sample result:
#Enter first number: …
#Enter second number: …
#Enter third number: …
#Numbers …, …, and … are different

def different(n1,n2,n3):
    if n1 != n2 and n2 != n3 and n1 != n3:
        return True
    else:
        return False

n1=input("Enter first number: ")
n2=input("Enter second number: ")
n3=input("Enter third number: ")

if different(n1,n2,n3)==True:
    print(f"Numbers {n1}, {n2}, and {n3} are different")
else:
    print(f"Numbers {n1}, {n2}, and {n3} are not all different")
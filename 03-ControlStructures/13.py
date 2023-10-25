#13.	A user enters two integer numbers from the keyboard. 
#Write a program that checks whether at least one of them is not negative. 
#Sample result:
#Enter number 1: 25
#Enter number 2: -17
#At least one of entered numbers 25 and -17 is not negative

number1=int(input("Enter number 1: "))
number2=int(input("Enter number 2: "))
if number1 or number2 >=0:
    print(f"At least one of entered numbers {number1} and {number2} is not negative")

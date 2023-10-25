#10.	Write a program to calculate the absolute value of a number entered from the keyboard. 
#Sample result:
#Enter number: -17
#|-17| = 17

number=float(input("Enter number: "))
if number<0:
    print(f"|{number}| = {abs(number)}")

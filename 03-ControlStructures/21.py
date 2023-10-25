#21.	Write a program that displays two numbers entered from the keyboard in ascending order.
#Enter first number: 27
#Enter second number: 14
#Numbers in ascending order: 14, 27

num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
if num1>num2:
    print(f"Numbers in ascending order: {num2}, {num1}")
elif num2>num1:
    print(f"Numbers in ascending order: {num1}, {num2}")
elif num1==num2:
    print(f"Numbers are the same")
    



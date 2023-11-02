#44.	Write a program that calculates the sum and arithmetic mean of numbers entered from the keyboard. 
#Entering 0 ends entering numbers. Sample result:
#Enter number: 15
#Enter number: 8
#Enter number: 10
#Enter number: 0
#RESULT: Quantity=3, Sum=33, Mean=11

number=int(input("Enter number: "))
quantity=0
sum=number
mean=number
while number!=0:
    number=int(input("Enter number: "))
    sum+=number
    quantity=quantity+1
    mean=sum/quantity
    
print(f"RESULT: Quantity={quantity}, Sum={sum}, Mean={mean}")
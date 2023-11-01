#33.	Write a program that converts a decimal number into a binary number. 
#To convert a decimal number to binary, follow these steps:
#a.	Read a decimal number from the keyboard.
#b.	Divide the number by 2 and note the remainder.
#c.	Divide the quotient obtained by 2 and note the remainder.
#d.	Repeat the same process till we get 0 as the quotient.
#e.	Write the values of all the remainders starting from the bottom to the top. That will be the required binary number.
#Sample result:
#Enter decimal number: 12
#12(10) = 1100(2)

dec=int(input("Enter decimal number: "))
#bin do dokonczenia
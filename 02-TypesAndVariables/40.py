#The credit card number consists of 16 digits. 
#Write a program that allows you to enter a credit card number from the keyboard. 
#Display the credit card number in groups of 4 digits, separating the groups with a space character. 
#Sample result:
#Enter credit card number: 5020312109004442
#Card number: 5020 3121 0900 4442

number=input("enter credit card number: ")
card=number[:4]+" "+number[4:8]+" "+number[8:12]+" "+number[12:]
print(f"card number: {card}")
#41.	The payment card is secured with a four-digit PIN code (0805). 
#Write a program that checks if the PIN code entered in the payment terminal is correct. 
#The user has up to three possibilities for entering a PIN code. 
#In case of three unsuccessful attempts, the card is blocked. Sample result:
#Enter the PIN code: 2398
#Incorrect...
#Enter the PIN code: 0912
#Incorrect...
#Enter the PIN code: 7860
#Incorrect...
#Sorry, your payment card has been blocked.

code="0805"
for x in range(3):
    pin=str(input("Enter the PIN code: "))
    if pin==code:
        print("Correct!")
        break
    if pin!=code:
        print("Incorrect...")

if pin!=code:
    print("Sorry, your payment card has been blocked.")
#23% VAT was paid from an amount. 
#Write a program that reads an amount from the keyboard. 
#Then, it calculates and displays both the amount and its VAT. 
#Apply formatting with two decimal places. Sample result:
#Amount  : 15.84
#VAT 23% :  3.64

amount=round(float(input("enter amount: ")),2)
vat=round(23/100*amount,2)
print(f"Amount: {amount}\nVAT 23%: {vat}")

#25.In one of the online stores, a 25% discount is charged for each product purchased over two. 
#Write a program that calculates the amount to be paid. 
#Read the number of purchased products and the product price from the keyboard. 
#Sample result:
#Number of products purchased: 5
#Product price: 40
#Amount to pay: 170.00

number=int(input("Number of products purchased: "))
price=float(input("Product price: "))
if number<=2:
    print(f"Amount to pay: {price}")
elif number>=3:
    print(f"Amount to pay: {2*price+(75/100*((number-2)*price))}")
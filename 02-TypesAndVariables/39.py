#The price of the product on the price tag is given before and after the discount is applied. 
#Write a program that allows you to enter the product price and discount. 
#Display the product price, discount, discounted product price, 
#and the difference between the product price before and after the discount. 
#Display all prices with two decimal places. Sample result:
#Enter price: 24.72
#Enter discount %: 15
#Price with discount: 21.01
#Reduction: 3.71

price=float(input("enter price: "))
discount=float(input("enter discount: "))
price_with_discount=round(price-(discount/100*price),2)
reduction=round(price-price_with_discount,2)
print(f"price with discount: {price_with_discount}")
print(f"reduction {reduction}")
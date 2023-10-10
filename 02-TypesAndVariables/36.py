#A bank buys and sells Euro. 
#Write a program that, based on the Euro buying and selling rates entered from the keyboard, 
#calculates the difference between the buying and selling rates (spread). 
#Display result with 4 decimal places. Sample result:
#Bank buys EUR: 4.5940
#Bank sells EUR: 4.6250
#Spread: 0.0310

buy=float(input("Bank buys EUR: "))
sell=float(input("Bank sells EUR: "))
spread=round(sell-buy,4)
print(f"spread: {spread}")

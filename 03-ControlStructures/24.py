#24.	A computer program analyses the price of a product in an online store. 
#If the product price decreases by at least 10%, the program displays a purchase recommendation:
#Buy the product!!
#Product price reduced by 17%
#Create such program. The current and previous price of the product are included in the variables. Sample result:
#Current product price: 140.00
#Previous product price: 200.00
#Buy the product!!
#Product price reduced by 30%

current=180.00
previous=200.00
rabat=100-current*100/previous
if rabat>=10:
    print(f"Buy the product!!\nProduct price reduced by {rabat}%")

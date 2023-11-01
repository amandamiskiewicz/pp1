#29.A washing machine allows you to wash a jacket, which takes 40 minutes, 
#wash underwear, which takes 70 minutes, and wash shoes, which takes 20 minutes. 
#In addition, it is possible to program an additional rinse (15 minutes) and an additional spin (9 minutes). 
#The washing machine settings are saved in variables. 
#Write a program that calculates and displays the total washing time. Sample result:
#washing_product = "shoes"
#rinse = True
#spin = False
#Total washing time: 35 minutes

def washing_machine(product,rin,spi):
    total=0
    washing_product= product
    rinse=rin
    spin=spi
    if washing_product == "shoes":
        total+=20
    elif washing_product == "jacket":
        total+=40
    elif washing_product == "underwear":
        total+=70
    if rinse == True:
        total+=15
    elif spin == True:
        total+=9
    return total    

print(washing_machine("shoes",True,False))

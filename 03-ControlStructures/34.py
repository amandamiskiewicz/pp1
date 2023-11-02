#34.	There are coins of 1, 2 and 5 Polish Zlotys (PLN). Write a program showing any amount 
#(natural number) read from the keyboard with as few coins as possible.
#Enter the amount in PLN: 18
#The amount of PLN 18 in coins:
#5 zł – 3 
#2 zł – 1 
#1 zł – 1

pln=int(input("Enter the amount in PLN: "))
while pln>0:
    piec=pln//5
    dwa=(pln%5)//2
    jeden=pln-piec*5-dwa*2
    pln=0
print(f"5 zł – {piec} \n2 zł – {dwa} \n1 zł – {jeden}")


#37.	Write a program that creates the following pattern. Sample result:
#* 
#* * 
#* * * 
#* * * * 
#* * * * * 
#* * * * 
#* * * 
#* * 
#*

for i in range(6):
    star= "* "
    print(f"{star*i}")
j=4
while j>0:
    star= "* "
    print(f"{star*j}")
    j-=1
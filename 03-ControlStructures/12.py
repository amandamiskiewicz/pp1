#12.	Write a program that checks that two people are adults. 
#Read people’s data from the keyboard. Sample result:
#Enter first person name: Peter
#Enter first person age: 21
#Enter second person name: Ann
#Enter second person age: 18
#Both Peter and Ann are adults

name1=input("Enter first person name: ")
age1=int(input("Enter first person age: "))
name2=input("Enter second person name: ")
age2=int(input("Enter second person age: "))
if age1 and age2>=18:
    print(f"Both {name1} and {name2} are adults")

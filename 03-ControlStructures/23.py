#23.	Write a program that calculates a dog's age in dog’s years. 
#For the first two years, a dog's life is equal to 10.5 human years. 
#After that, each dog year is equal to 4 human years. Sample result:
#Enter the dog's age in human years: 15
#The dog's age in dog’s years is 73 years.

dog_age=int(input("Enter the dog's age in human years: "))
if dog_age<=2:
    print(f"The dog's age in dog\'s years is {dog_age*10.5} years")
elif dog_age>2:
    print(f"The dog's age in dog\'s years is {2*10.5+(dog_age-2)*4} years")

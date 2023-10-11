#37.	In Python, to read a range of characters from the string, a slicing method can be used.
#https://www.w3schools.com/python/python_strings_slicing.asp 
#The employee file contains the employee's data in a descriptive form. 
#Write a program in which the personal_data variable contains employee data:
#Mr. John May, born on 1998-02-16"
#Display the employee's name, surname, initials and date of birth on separate lines. Sample result:
#Description: Mr. John May, born on 1998-02-16
#Name: John
#Surname: May
#Initials: JM
#Born: 1998-02-16

personal_data="Mr. John May, born on 1998-02-16"
name=personal_data[4:8]
surname=personal_data[9:12]
intials=personal_data[4]+personal_data[9]
born=personal_data[-10:]
print(f"Name: {name}\nSurname: {surname}\nInitials: {intials}\nBorn: {born}")

#22.	Most female names in Polish end with the letter "a". 
#Write a program that displays the name entered from the keyboard, provided it is a female name. 
#Sample result:
#Enter name: Anna
#Anna – Polish female name

name=input("Enter name: ")
if name[-1]=="a":
    print(f"{name} – Polish female name")
else:
    print(f"{name} – not a Polish female name")
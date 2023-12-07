'''21.	Create a program that writes to a text file integer numbers in the range <1,50>, 
every number in a separate line.'''

with open("numbers.txt","w") as file:
    for i in range(1,51):
        file.write(str(i))
        file.write("\n")

'''with open("numbers.txt", "w") as file:
    for i in range(1, 51):
        file.write(str(i))
        if i != 50:  # Dodaj warunek, aby nie dodać nowej linii po ostatniej liczbie
            file.write("\n") '''

#by nie bylo ostatniego \n
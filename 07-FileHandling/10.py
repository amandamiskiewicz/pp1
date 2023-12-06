'''10.	Find any text file on the Internet and download it to your computer. 
Then, write a program that displays its content.'''

file = open("lorem.txt" , "r")
result = file.read()
print(result)
file.close()

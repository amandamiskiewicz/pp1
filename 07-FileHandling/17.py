'''17.Find any text file on the Internet that contains at least 30 lines of text 
and download that file to your computer. Then, write a program that displays the first five lines from the file 
and then waits for the Enter key to be pressed. 
The program repeats displaying the next five lines from the file, 
waiting for the Enter key to be pressed each time.'''

file = open("lorem.txt","r")
print(file.readline(),end="")
print(file.readline(),end="")
print(file.readline(),end="")
print(file.readline(),end="")
print(file.readline(),end="")
i=input("")
while i=="":
    print(file.readline(),end="")
    print(file.readline(),end="")
    print(file.readline(),end="")
    print(file.readline(),end="")
    print(file.readline(),end="")
    i=input("")
    
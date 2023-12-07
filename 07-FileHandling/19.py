'''19.	Find any text file on the Internet and download it to your computer. 
Then, write a program that copies the contents of this file to the copylines.txt file. 
Copy the contents of the file line by line. 
Finally, open both files in any text editor and check that their contents are the same.'''

file = open("countries.txt", "r")
copy = open("copylines.txt", "w")
for line in file:
    copy.write(line)
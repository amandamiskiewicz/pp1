'''20.	Using any text editor, create the following two text files:
MeatAndFish.txt
Skinless white meat
Tuna fish
Luncheon meat
Lean cuts of red meat
GrainsAndBread.txt
Bread
Rice
All purpose flour
Breakfast cereal
Pasta 
Then, write a program that creates the allproducts.txt file, 
in which save the contents of the MeatAndFish.txt and the GrainsAndBread.txt files.
'''

new_file = open("allproducts.txt", "w")
file1 = open("MeatAndFish.txt", "r")
file2 = open("GrainsAndBread.txt", "r")

new_file.write(file1.read())
new_file.write(file2.read())

file1.close()
file2.close()
new_file.close()
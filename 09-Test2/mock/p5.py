'''(p5.py) Create a function f(first_letter,last_letter) that, for the data.txt file, 
returns the number of words that start with the first_letter and end with the last_letter. Example:
f("w","d")  compare your result with other students 
'''
first_letter="w"
last_letter="d"

import re

def f(first_letter,last_letter):
    file = open("data.txt" , "r")
    txt = file.read()
    x = re.findall(fr'\b{first_letter}\w*{last_letter}\b',txt)
    file.close()
    return len(x)

print(f(first_letter,last_letter))
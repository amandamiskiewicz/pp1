"""20.	In the module mykeyboard.py, define a function read_number() that returns an integer number entered 
from the keyboard. The function should print a text prompting user to enter data 'Enter a number: '. 
Then, use the function to read two numbers from the keyboard. To test the function, use the __name__ variable. 
Display the sum of two entered numbers. Sample result:
Enter a number: 34
Enter a number: 7
34 + 7 = 41"""

import mykeyboard

n1=mykeyboard.read_number()
n2=mykeyboard.read_number()
msg=f"{n1} + {n2} = {n1+n2}"
print(msg)
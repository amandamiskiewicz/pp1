#12.	Using built-in Python functions, write a program that calculates and displays:
#a.	the largest number given: 7,5,6,3,8,2
#b.	binary string representing decimal number 304
#c.	hexadecimal string representing decimal number 304
#d.	integer representing the Unicode code of the € sign
#e.	absolute value of -17

# task a
max_number = max(7,5,6,3,8,2)
print('Max number of 7,5,6,3,8,2 is', max_number) 

# task b
print(bin(304))

# task c
print(hex(304))

# task d
print(ord("€"))

# task e
print(abs(-17))

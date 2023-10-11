#Write a program that allows you to enter a binary, four-digit number. 
#Convert the entered number from binary to decimal value. 
#Do not use available Python functions. Sample result:
#Enter binary number: 0110
#Binary number in decimal notation: 6

binary=input("enter binary number: ")
number=int(binary[0])*8+int(binary[1])*4+int(binary[2])*2+int(binary[3])*1
print(f"binary number in decimal notation: {number}")

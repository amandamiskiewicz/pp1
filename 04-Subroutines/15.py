#15.Define a function phone_keyboard() that displays numbers in the layout as below (like on a phone keypad). 
#Apply a loop statement. Then, call the function. Sample result:
#1 2 3
#4 5 6
#7 8 9

def phone_keyboard():
    for i in range(0,9,3):
        print()
        for j in range(1,4):
            print(i+j, end=" ")

phone_keyboard()
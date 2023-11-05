'''40.	Define a function f(number) that returns the sum of repeated digits in a number. Sample result:
f(1027) returns 0
f(230335) returns 9
f(513553007) returns 21 
'''

def f(number):
    number_str = str(number)
    sum_repeated_digits = 0
    
    for digit in number_str:
        if number_str.count(digit) > 1:
            sum_repeated_digits += int(digit)
    
    return sum_repeated_digits

if __name__=="__main__":
    print(f(1027))
    print(f(230335))
    print(f(513553007))
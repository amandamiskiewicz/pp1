'''42.	Define the function f(number1,number2,number3), which returns the difference between the largest and 
smallest numbers. Sample result:
f(7,4,9) returns 5
f(2,12,8) returns 10
'''

def f(number1,number2,number3):
    max_number=max(number1,number2,number3)
    min_number=min(number1,number2,number3)
    return max_number-min_number

if __name__=="__main__":
    print(f(7,4,9))
    print(f(2,12,8))
#Enter your height in cm: ...
#Enter your weight in kg: ...
#Your BMI index: ...
#Correct weight: True

height=float(input("Enter your height in cm: "))
weight=float(input("Enter your weight in kg: "))
bmi=weight/height**2
if bmi<=24.99 and bmi>=18.5:
    print(f"Correct weight: {True}")
else:
    print(f"Correct weight: {False}")
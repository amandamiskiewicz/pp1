'''11.	Create a program that displays the name of month for a given month number (1 to 12). 
Define a month(n) function that returns the name of month for the number n. 
Store month names in an array. Using defined function, display month names for the following month numbers: 1, 9, 12. Sample result:
def month(n):
    month_name = ["January","February",…]
    return month_name[…]
Enter month number: 10
Month name: October
'''

def month(n):
    month_name = ["Styczeń", "Luty", "Marzec", "Kwiecień", "Maj", "Czerwiec", "Lipiec", "Sierpień", "Wrzesień", "Październik", "Listopad", "Grudzień"]
    return month_name[n-1]

n=int(input("Enter month number: "))
print(f"Month name: {month(n)}")


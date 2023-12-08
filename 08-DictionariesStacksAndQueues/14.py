'''14.	A dictionary contains course names along with the number of hours. 
Write a program that calculates and displays the total number of hours. Sample results:
winter_semester = {
    "math":60,
    "programming":30,
    "history":15
}
The total number of hours in the winter semester is …
'''

winter_semester = {
    "math":60,
    "programming":30,
    "history":15
}

total = 0
for hours in winter_semester.values():
    total+=hours
print(total)
'''(p6.py) Create a function f(years, course) that, for the data.json file, 
returns the number of students who are at least the given number of years and have a grade average of at 
least 4 in the given course name. Example:
f(21, "statistics")  compare your result with other students
'''
import json
def f(year, course, average):
    count=0
    with open('data.json', 'r') as file:
        data=json.load(file)
    for i in data:
        for j in i['studies']['courses']:
            if course==j['name']:
                if sum(j['grades'])/len(j['grades'])>=average and i['age']>=year:
                    count+=1
    return count

print(f(21,"statistics",4))


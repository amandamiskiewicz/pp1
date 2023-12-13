'''(p6.py) Create a function f(years, course) that, for the data.json file, 
returns the number of students who are at least the given number of years and have a grade average of at 
least 4 in the given course name. Example:
f(21, "statistics")  compare your result with other students
'''
import json
def f(years, course):
    res=0
    with open("data.json") as file:
        txt = json.load(file)
        for i in txt:
            for j in i["studies"]["courses"]:
                if course==j["name"]:
                    if i["age"]>=years and sum(j["grades"])/len(j["grades"])>=4:
                        res+=1
    return res

if __name__=="__main__":
    print(f(21, "statistics"))
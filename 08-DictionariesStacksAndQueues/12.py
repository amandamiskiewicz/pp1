'''12.	Write a program in which you create a dictionary containing student data. 
Try to describe a student in detail, using different data types that can be used in the dictionary. 
Then, save the data about student in the file student.json, in a readable form.'''

import json 

student = {
    "name":"wiktor",
    "surname":"abc",
    "age":20,
}

with open("student.json", "w") as file:
    json.dump(student, file, indent=2)
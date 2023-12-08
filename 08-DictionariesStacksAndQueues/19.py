'''19.	Using the website https://mockaroo.com, generate a list of 500 students, 
containing the following data: name, surname, student ID, gender, age, year of study, email. 
Write the data to the students.json file. 
Then, write a program that creates the limited.json file containing the list of students limited to data: 
first name, last name, student id.'''

import json
x = open("students.json")
js = json.load(x)
f = open("limited.json", "w")
mass = []
for student in js:
    mass.append({"name" : student["name"], 'surname' : student["surname"], 'student_id' : student["student_id"]})
json.dump(mass, f, indent=6)
x.close()
f.close()
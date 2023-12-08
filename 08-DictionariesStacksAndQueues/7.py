'''7.	Create a dictionary as in the example below. Note the structure of the dictionary (key-value) 
and the value types in the example below. What type of value was used in each of the six key-value pairs?
person = {
    "name": "Marek",
    "surname": "Banach",
    "age": 25,
    "hobby": ["swimming","excursions"],
    "married": True,
    "phone":{"landline":"123444321","mobile":"777888999"}
   }
Then, create a program that:
a.	Displays contents of the dictionary
b.	Displays name
c.	Displays hobby
d.	Changes surname to 'Nowak'
e.	Changes person's marriage status
f.	Adds gender: 'male'
g.	Adds a new hobby: 'bicycle'
h.	Adds work phone to existing phones: '313131444'
'''

person = {
    "name": "Marek",
    "surname": "Banach",
    "age": 25,
    "hobby": ["swimming","excursions"],
    "married": True,
    "phone":{"landline":"123444321","mobile":"777888999"}
   }
#a
print(person)
#b
print(person["name"])
#c
print(person["hobby"])
#d
person["surname"] = "Nowak"
print(person["surname"])
#e
person["married"] = False
print(person["married"])
#f
person["gender"] = "male"
print(person["gender"])
#g
if "bicycle" not in person["hobby"]:
    person["hobby"].append("bicycle")
print(person["hobby"])
#h
person["phone"]["work"]="313131444"
print(person["phone"])

'''11.	Create a dictionary that describes your favorite book or movie with at least five key-value pairs. 
Then, create a program that writes the dictionary data to the favourite.json file. Use the dump() method. 
Pay attention to the formatting of the data in the json file. 
Use the 'indent' parameter in the dump() method. Sample result:
'''

import json

movie = {
    "title": "abc",
    "year": 2010,
    "actor": {"leading": "aaa", "supporting": "bbb"},
    "oscar": False,
    "grade": 4
}

with open("favourite.json", "w") as file:
    json.dump(movie, file, indent=2)
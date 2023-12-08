'''8.	Create a dictionary describing your mobile phone. Use at least 6 key-value pairs of data of different types. 
Then, using 'for' loop, display the contents of the dictionary. 
To read a key and value, use the items() method. Sample result:
mobile = {
    "OS":"Android",
    …
    …
    …
    …
    …
}
for key,value in mobile.items():
    print(f"{key} : {…}")
'''

mobile = {
    "OS":"iOs",
    "model":"iPhone",
    "number":1234558903,
    "aplikacje":["twitter","facebook"],
    "color":"black",
    "year":2020
}

for key,value in mobile.items():
    print(f"{key} : {value}")
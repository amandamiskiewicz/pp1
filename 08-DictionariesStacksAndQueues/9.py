'''9.	Create an array with 5 dictionaries, each containing a country and its population. 
Then, using a ‘while’ loop, display the array contents. Sample result:

COUNTRY  POPULATION
Poland   38000000
…        …
…        …
…        …
…        …
'''
countries = [
    {"name": "Poland", "population": 38000000},
    {"name": "Germany", "population": 83000000},
    {"name": "France", "population": 67000000},
    {"name": "Italy", "population": 60300000},
    {"name": "Spain", "population": 47000000}
]

x = 0
print("COUNTRY\tPOPULATION")
while x < len(countries):
    country = countries[x]["name"]
    population = countries[x]["population"]
    print(f"{country}\t{population}")
    x += 1
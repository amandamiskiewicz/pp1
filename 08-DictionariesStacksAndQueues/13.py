'''13.	A program contains any defined dictionary, with any number of key-value pairs of information. 
Write a program that displays the number of pairs of information available in the dictionary.'''

x = {
  "name": "wiktor",
  "surname": "abc",
  "age": 20
}

result=0
for i in x.items():
    result+=1

print(result)
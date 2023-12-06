'''43.	A variable contains text:
An apple a day keeps the doctor away
Create a module MyText, containing:
a.	A function that returns the number of words in the text
b.	A function that returns an ordered array of words, from longest to shortest
c.	A function that returns an alphabetically ordered array of words
Then, write a program, call the functions and display results. Sample result:
Text: An apple a day keeps the doctor away
Number of words: 8
Words from the longest: doctor,apple,…
Words ordered alphabetically: a,An,apple,away,…
'''

text = "An apple a day keeps the doctor away"

def num_of_words(text):
    words = text.split()
    return len(words)

def ordered_by_length(text):
    words = text.split()
    return sorted(words, key=len, reverse=True)

def ordered_alphabetically(text):
    words = text.split()
    return sorted(words, key=str.lower)

# Wywołanie funkcji i wyświetlenie wyników
print("Text:", text)
print("Number of words:", num_of_words(text))
print("Words from the longest:", ordered_by_length(text))
print("Words ordered alphabetically:", ordered_alphabetically(text))

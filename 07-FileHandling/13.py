'''13.	An array movie_titles contains any five movie titles. 
Write a program that writes the movie titles to the movies.txt file, each title on a separate line. 
After executing the program, open the created text file and check its content.'''

movie_titles = ["a","b","c","d","e"]

file = open("movies.txt","w")
for movie in movie_titles:
    file.write(movie+"\n")

#with open("movies.txt","w") as file:
#    file.write("\n".join(movie_titles))

file = open("movies.txt","r")
print(file.read())
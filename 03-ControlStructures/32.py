#32.Yes-no question are often used in surveys to gauge people's attitudes with regard to specific ideas or beliefs.
#Write a program that displays a survey consisting of three questions. 
#Save the answers to logical type variables. Then view the survey result. Sample result:
#Are you interested in computer science? (Y/N): Y 
#Do you like playing computer games? (Y/N): N
#Do you have an Instagram account? (Y/N): Y
#Interested in computer science: Yes
#Playing computer games: No
#Has an Instagram account: Yes

q1=input("Are you interested in computer science? (Y/N): ")

q2=input("Do you like playing computer games? (Y/N): ")

q3=input("Do you have an Instagram account? (Y/N): ")

if q1=='Y':
    print("Interested in computer science: Yes")
else:
    print("Interested in computer science: No")
if q2=='Y':
    print("Playing computer games: Yes")
else:
    print("Playing computer games: No")
if q3=='Y':
    print("Has an Instagram account: Yes")
else:
    print("Has an Instagram account: No")    
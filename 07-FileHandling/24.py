'''24.	In any text editor, create a text file studentslist.txt containing the following data in the CSV format:
first_name,last_name,age,gender,email
Decca,Blackstone,52,Male,dblackstone0@time.com
Elena,Rechert,27,Female,erechert1@ucoz.com
Bibbye,Norree,26,Female,bnorree2@reddit.com
Alasdair,McCoole,53,Male,amccoole3@foxnews.com
Hogan,Hatrey,26,Male,hhatrey4@zimbio.com
Then, create a program that reads data from the CSV file and displays the first name, 
last name and email address of students under 30. Format the data as below. Sample result:
Elena   Rechert  erechert1@ucoz.com
Bibbye  Norree   bnorree2@reddit.com
Hogan   Hatrey   hhatrey4@zimbio.com
Tip: import and use the CSV module. 
'''

import csv

with open('studentslist.txt') as csvfile:
    reader = csv.DictReader(csvfile)
    
    # Display header
    print(f"{'First Name':15}{'Last Name':15}{'Email Address'}")

    # Iterate through rows and display data for students under 30
    for row in reader:
        if int(row['age']) < 30:
            print(f"{row['first_name']:15}{row['last_name']:15}{row['email']}")

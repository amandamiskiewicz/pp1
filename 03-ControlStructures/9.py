#9.	A test is passed when the number of correctly completed tasks is at least 50%. 
#Write a program that checks whether the test is passed. 
#The total number of test tasks and the number of correctly completed tasks are included in variables. 
#Sample result:
#Test passed

number_of_tasks=20
correct_tasks=11
if correct_tasks>=1/2*number_of_tasks:
    print("Test passed")
else:
    print("Test failed")

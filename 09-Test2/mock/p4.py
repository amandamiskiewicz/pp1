'''(p4.py) The dictionary contains the names of subjects and the grades obtained. 
Create a function f(subjects) that, for the given subjects and their grades, 
returns the name of the subject for which the average grade is the highest. Example:
f({"math":[3,4,4],"geo":[5,4,4,4],"comp":[5,4]})  "comp"
'''


def f(subjects):
    max_subject = None
    max_average = 0

    for subject, grades in subjects.items():
        average = sum(grades) / len(grades)

        if average > max_average:
            max_average = average
            max_subject = subject

    return max_subject

# Example usage:
subjects_grades = {"math": [3, 4, 4], "geo": [5, 4, 4, 4], "comp": [5, 4]}
result = f(subjects_grades)

print(result)  # Output: "comp"
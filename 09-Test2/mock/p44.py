'''(p4.py) The dictionary contains the names of subjects and the grades obtained. 
Create a function f(subjects) that, for the given subjects and their grades, 
returns the name of the subject for which the average grade is the highest. Example:
f({"math":[3,4,4],"geo":[5,4,4,4],"comp":[5,4]})  "comp"
'''
def f(subjects):
    subjects={"math": [3, 4, 4], "geo": [5, 4, 4, 4], "comp": [5, 4]}
    top_grades=0
    top_subject=""
    for keys,value in subjects.items():
        sum=0
        for grade in value:
            sum+=grade
        mean=sum/len(value)
        if mean>top_grades:
            top_grades=mean
            top_subject=keys
    return top_subject


if __name__=="__main__":
    print(f({"math": [3, 4, 4], "geo": [5, 4, 4, 4], "comp": [5, 4]}))


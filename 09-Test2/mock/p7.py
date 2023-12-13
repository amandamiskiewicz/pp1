'''(p7.py) A valid username consists of 4 to 12 characters: lowercase letters, numbers and the underscore character. 
Create a function f(arr) that, for a given array of usernames, returns the number of valid usernames in the array. Example:
f(["uek","water_7_x","anna.may","a_b_c_d_e_f"])  2
'''
import re
def f(arr):
    res=0
    for username in arr:
        y = re.findall(r"^[a-z0-9_]{4,12}$",username)
        res+=len(y)
    return res

a ="uek"
y = re.findall("^[a-z0-9_]*$",a)
print(y)

print(f(["uek","water_7_x","anna.may","a_b_c_d_e_f"]))
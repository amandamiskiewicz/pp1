'''13.	In a certain company, 25 employees commute by car, 19 employees commute by public transport, 
32 people commute by bike, and 7 people commute on foot. Write a program that displays this data in a bar chart. 
Remember to add a title for the chart and a description of the chart axes. Sample result:
See a similar task from the BEFORE CLASS section.
'''

import matplotlib.pyplot as plt

x = ["by car", "by public transport", "by bike", "on foot"]
y = [25, 19, 32, 7]

plt. title("tytuł")
plt.bar(x,y)
plt.show()
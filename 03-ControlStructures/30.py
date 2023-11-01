#30.	Write a program that allows you to convert time in 24-hour format to 12-hour format. 
#The time in 24-hour format (hh:mm) is read from the keyboard. Sample result:
#Enter time (24-hour format): 16:32
#Time in 12-hour format: 4:32pm


time=input("Enter time (24-hour format): ")
hour=int(time[:2])
min=time[3:]
if hour==24:
    print(f"12:{min}am")
elif hour==12:
    print(f"{hour}:{min}pm")
elif hour>12:
    hour-=12
    print(f"{hour}:{min}pm")
else:
    print(f"{hour}:{min}am")
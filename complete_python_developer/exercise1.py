import datetime as time

year = input("What year are you born :  ")   
#calculate age
#print(time.datetime.now().year)
age = time.datetime.now().year - int(year)
print(f'You are {age} years old')
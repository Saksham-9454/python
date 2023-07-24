import time
timestamp = time.strftime('%H:%M:%S')
print("The time is",timestamp)
timestamp = int(time.strftime('%H'))
print("Right now the Hours is",timestamp)
if(timestamp<12):
    print("Good Morning Sir!")
elif(timestamp>12 and timestamp<=16):
    print("Good Afternoon Sir!")
elif(timestamp>16 and timestamp<=20):
    print("Good evening Sir!")
else:
    print("Good night Sir!")

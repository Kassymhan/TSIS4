import datetime

x = datetime.date.today()
t = datetime.timedelta(days = 1)

print('Yesterday:' ,x - t)
print('Today:', x)
print('Tomorrow:', x+t)
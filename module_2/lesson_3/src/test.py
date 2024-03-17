from datetime import datetime

current_datetime = datetime.now()
date_work = current_datetime.day
print("Сегодня ", current_datetime.day, "число" )

workers = ['Маша', 'Света', 'Паша', 'Олег']

if date_work % 2 == 0:
    print(f"На работу выходят ", *workers[::2])
else:
    print(f"На работу выходят ", *workers[1::2])
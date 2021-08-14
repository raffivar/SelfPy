import calendar
date = input("date: ")
date_as_list = date.split('/')

day = int(date_as_list[0])
month = int(date_as_list[1])
year = int(date_as_list[2])

day_num = calendar.weekday(year, month, day)

if day_num == 0:
    print('Monday')
elif day_num == 1:
    print('Tuesday')
elif day_num == 2:
    print('Wednesday')
elif day_num == 3:
    print('Thursday')
elif day_num == 4:
    print('Friday')
elif day_num == 5:
    print('Saturday')
elif day_num == 6:
    print('Sunday')
else:
    print('Never supposed to reach here')

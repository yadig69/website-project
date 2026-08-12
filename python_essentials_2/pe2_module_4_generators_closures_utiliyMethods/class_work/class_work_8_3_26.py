import calendar


# print(calendar.calendar(2026))
# calendar.setfirstweekday(calendar.SUNDAY)
# calendar.prmonth(2026, 1)


c= calendar.Calendar(2)

for weekday in c.iterweekdays():
    print(weekday, end=" ")

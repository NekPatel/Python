from datetime import date

date1 = (6,6,2023)
date2 = (20,3,2006)

d1 = date(date1[2], date1[1], date1[0])
d2 = date(date2[2], date2[1], date2[0])

days_difference = abs((d2-d1).days)

print(f"the number of days between the two dates is: {days_difference} days")

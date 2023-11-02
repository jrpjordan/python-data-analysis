from datetime import datetime, date, time

dt = datetime(2024, 10, 29, 20, 30, 21)
print(dt.day)
print(dt.minute)

print(dt.strftime("%Y-%m-%d %H:%M"))

# Applies an offset to the existing datetime
dt2 = dt.timedelta(days=17, seconds=7179)
# datetime_basic.py
# Basic usage of datetime module

from datetime import datetime, date, timedelta

now = datetime.now()
today = date.today()

print("Current datetime:")
print(now)

print("\nToday's date:")
print(today)

tomorrow = today + timedelta(days=1)
print("\nTomorrow's date:")
print(tomorrow)

formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print("\nFormatted datetime:")
print(formatted)

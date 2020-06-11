#Write a Python program to subtract 30 days from current date.

from datetime import timedelta, datetime;

date_now = datetime.now() - timedelta(days=30);
print("Substracted 30 days to the actual date: " + str(date_now));

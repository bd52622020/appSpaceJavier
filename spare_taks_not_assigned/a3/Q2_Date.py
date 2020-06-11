# Write a Python script to display the various Date Time formats.
# 
# a. Current date and time
# b. Current year
# c. Month of year
# d. Week number of the year
# e. Weekday of the week
# f. Day of year
# g. Day of the month
# h. Day of week

import datetime;

date_now = datetime.datetime.now();

print("Date today - " + str(date_now));
print("Year - " + str(date_now.year));
print("Month of year - " + str(date_now.strftime("%B")));
print("Week number of the year - " + str(date_now.strftime("%U")));
print("Weekday of the week - " + str(date_now.strftime("%A")));
print("Day of year - " + str(date_now.strftime("%j")));
print("Day of the month - " + str(date_now.strftime("%d")));
print("Day of the week - " + str(date_now.strftime("%w")));



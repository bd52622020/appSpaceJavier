inp = 1992

first_condition = (inp % 4 == 0) and (inp % 100 != 0)
second_condition = (inp % 4 == 0) and (inp % 100 == 0) and (inp % 400 == 0)

if first_condition or second_condition:
    print("Congratulations! It is a leap year")
else:
    print("This year we did not have luck")
    

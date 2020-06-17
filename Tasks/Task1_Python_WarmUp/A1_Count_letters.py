#Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters. 

string = input("Introduce your string to calculate; ");

lowercase, uppercase = 0, 0;

for c in string:
    if c.isupper():
        uppercase += 1;
    elif c.islower():
        lowercase += 1;

print("There are " + str(uppercase) +" uppercases and " + str(lowercase) +" lowercases");
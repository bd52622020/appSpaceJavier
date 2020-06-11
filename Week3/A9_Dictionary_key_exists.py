# Write a Python script to check whether a given key already exists in a dictionary.

key = 9
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

if key in d.keys():
    print("This key exists in the dictionary.")
else:
    print("This key NOT exists in the dictionary")

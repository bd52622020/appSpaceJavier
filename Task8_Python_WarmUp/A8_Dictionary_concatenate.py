# Write a Python script to concatenate following dictionaries to create a new one

a={1:10, 2:20} 
b={3:30, 4:40} 
c={5:50, 6:60}

a.update(b)
a.update(c)

print("Concatenated dictionary:")
print(a)
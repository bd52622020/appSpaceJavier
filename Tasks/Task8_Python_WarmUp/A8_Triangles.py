# Write a Python program to check whether three given lengths (integers) of three sides form a right triangle. 
# Print "Yes" if the given sides form a right triangle otherwise print "No".
import math

def check_right_triangle(a, b, c=0):
    # If we do not have c, calculate with a & b
    if c == 0:
        c = math.sqrt(a**2 + b**2)
        
    return a**2 + b**2 == c**2
    
    
    
print("Triangle checker!")
print("Write 3 or 2 sides of your triangle in our fantastic method")  
print(check_right_triangle(3, 4))
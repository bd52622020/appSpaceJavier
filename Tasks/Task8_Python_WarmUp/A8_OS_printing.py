# Write a Python program to display some information about the OS where the script is running
import platform
import os



print("API -", os.name)
print("OS Name -", platform.system())
print("Release -", platform.release())
print("Architecture -", platform.architecture())  
print("Machine -", platform.machine()) 
print("Hostname -", platform.node())
print("Processor -", platform.processor())

path_file = "/home/javi/Desktop/Links"

try:
    f = open(path_file, "r")
    for _ in range(10):
        print(next(f))
except Exception:
    print("The path variable was incorrect!")
finally:
    f.close()
    print("Thank you so much for using my program.")
res = []

n = int(input("How many * would you like to get: ", ))

def printHalfPattern(initial, end, b):
    for i in range(initial, end, b):
        line = ""
        ast = "* "
        for j in range(i):
            line = ast + line
        print(line + "\n")
   
def printPattern(n):
    printHalfPattern(1, n+1, 1)
    printHalfPattern(n, 0, -1)
    
printPattern(n)


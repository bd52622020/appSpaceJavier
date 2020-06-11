not_valid = "3-598-21508-8"
valid = "0-19-852663-6"

def check_isbn(n):
    isbn = list(n.replace("-", "")[::-1])
    acum = 0
    for i in range(10):
        acum += int(isbn[i]) * (i+1)
    res = acum * 11
    
    return res % 11 == 0


print(check_isbn(valid))
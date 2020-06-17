inp = 45

def check_prime(numberToCheck):
    prime = True
    for i in range(2, numberToCheck):
        if (numberToCheck % i == 0):
            prime = False
    return prime


def calculate_list_primes(n):
    res = []
    for num in range(1, n+1):
        prime = check_prime(num)
        if prime:
            res.append(num)
    return res

print(calculate_list_primes(inp))
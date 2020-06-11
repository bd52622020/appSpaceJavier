# Write a Python function that prints out the first n rows of Pascal's triangle
def pascal(n):
    rows = [[1]]
    for _ in range(1, n):
        rows.append([1] +
                    [sum(pair) for pair in zip(rows[-1], rows[-1][1:])] +
                    [1])
    return rows

n = int(input("Type how many rows you want in the pascal triangle: "))

res = pascal(n);

print(res)

    


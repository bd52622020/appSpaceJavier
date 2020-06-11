example = [1, 2, 3, 3, 4, 5, 5, 8]

def remove_duplicates_loop(example):
    res = []
    for i in example:
        if i not in res:
            res.append(i)
    return res
                
                
def remove_duplicates_set(example):
    newset =set(example)
    return newset;

print('The example will be : ')
print(example)

print('First we will remove duplicates by loops')
res = remove_duplicates_loop(example)
print('Result: ', res)

print('Second we will remove duplicates by set')
res = remove_duplicates_set(example)
print('Result: ', res)
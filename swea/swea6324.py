def relist(x):
    return (list(set(x)))
a = [1, 2, 3, 4, 3, 2, 1]
b = relist(a)
print(a)
print(b)
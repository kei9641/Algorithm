a = input()
n1, n2 = a.split(', ')
c = 0
def compare(x, y):
    for i in range(len(a)):
        if(len(x) > len(y)):
            c = x
        else:
            c = y
    return c
result = compare(n1, n2)
print(result)

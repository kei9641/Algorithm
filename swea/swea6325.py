def selec(x, y): #x리스트 y특정숫자
    g = False
    for i in range(len(x)):
        if(x[i] == y):
            g = True
    return g

a = [2, 4, 6, 8, 10]
m, n = 5, 10
p = selec(a, m)
q = selec(a, n)
print(a)
print("{} => {}" .format(m, p))
print("{} => {}" .format(n, q))
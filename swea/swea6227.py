even = []
e=0
k = True
for i in range(100, 301):
    if (((i//100) % 2 == 0) and ((i//10) % 2 == 0) and (i % 2 == 0)):
        even.append(i)
        if not k:
            print(",", end="")
        print(even[e], end="")
        k = False
        e = e+1
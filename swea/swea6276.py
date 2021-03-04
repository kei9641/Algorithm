result = []
for i in range(2, 10):
    multi = []
    for j in range(1, 10):
        x = i * j
        if not (x % 3) or not (x % 7):
            continue
        multi.append(x)
    result.append(multi)
print(result)
n = input()
m = []
num = [0,0,0,0,0,0,0,0,0,0]
for i in range(len(n)):
    m.append(n[i])
for i in m:    
    for j in range(9):
        if int(i) == j:
            num[j] += 1
print("0 1 2 3 4 5 6 7 8 9")
print(" ".join(map(str, num)))
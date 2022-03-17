N = int(input())
pinary = [0, 1]

for n in range(2, N + 1):
    pinary.append(pinary[n - 2] + pinary[n - 1])

print(pinary[N])
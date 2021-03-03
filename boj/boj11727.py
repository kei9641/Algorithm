lect = [1 for _ in range(1001)]

n = int(input())
for i in range(2, n+1):
    lect[i] = lect[i-1] + (lect[i-2] * 2)

print(lect[n] % 10007)
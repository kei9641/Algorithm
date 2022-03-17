M = int(input())
N = int(input())

n = 1
sumN, minN = 0, 0

while n ** 2 <= N:
    if (n ** 2) >= M:
        sumN += n ** 2
        if minN == 0:
            minN = n ** 2

    n += 1

if minN == 0:
    print(-1)
else:
    print(sumN)
    print(minN)
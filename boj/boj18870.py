N = int(input())
X = list(map(int, input().split()))

orderX = []
for i in range(N):
    orderX.append((X[i], i))
orderX.sort()

result = [0 for _ in range(N)]
pos = 0
num = orderX[0][0]
result[orderX[0][1]] = pos
for j in range(1, N):
    if num < orderX[j][0]:
        pos += 1
    result[orderX[j][1]] = pos
    num = orderX[j][0]
    
print(*result)
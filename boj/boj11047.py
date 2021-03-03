N, K = map(int, input().split())
coin = []
for _ in range(N):
    coin.append(int(input()))

count = 0
for i in range(N-1, -1, -1):
    if K == 0:
        break

    if coin[i] <= K:
        while 1:
            if K >= coin[i]:
                K -= coin[i]
                count += 1
            else:
                break

print(count)
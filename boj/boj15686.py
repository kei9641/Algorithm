from itertools import combinations

city = []
N, M = map(int, input().split())
for _ in range(N):
    city.append(list(map(int, input().split())))

house = []
chicken = []
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            house.append((i, j))
        elif city[i][j] == 2:
            chicken.append((i, j))

minLength = 10 ** 6
openStore = combinations(chicken, M)
for store in openStore:
    chickenLength = 0
    for hx, hy in house:
        length = N * 2
        for sx, sy in store:
            length = min(length, abs(hx - sx) + abs(hy - sy))
        chickenLength += length
    minLength = min(minLength, chickenLength)

print(minLength)
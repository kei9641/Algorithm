T = int(input())
for _ in range(T):
    n = int(input())
    spots = []
    for _ in range(n + 2):
        spots.append(list(map(int,input().split())))

    distance = [[10**10 for _ in range(n+2)] for _ in range(n+2)]

    for i in range(n+2):
        for j in range(n+2):
            if i != j:
                meter = abs(spots[i][0] - spots[j][0]) + abs(spots[i][1] - spots[j][1])
                if meter <= 1000:
                    distance[i][j] = 1

    for k in range(n+2):
        for i in range(n+2):
            for j in range(n+2):
                if distance[i][j] > distance[i][k] + distance[k][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]

    if 0 <= distance[0][n+1] < 10**10:
        print('happy')
    else:
        print('sad')

from collections import deque
import heapq

waters = []
N = int(input())
for _ in range(N):
    waters.append(list(map(int, input().split())))

size = 2

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

def isNotWall(x, y):
    return (0 <= x < N) and (0 <= y < N)

def bfs(x, y):
    visited[x][y] = 1
    nearby = []
    while move:
        x, y, d = move.popleft()
        for n in range(4):
            xn, yn = x + dx[n], y + dy[n]
            if isNotWall(xn, yn) and visited[xn][yn] == 0:
                if not waters[xn][yn] > size:
                    visited[xn][yn] = 1
                    move.append((xn, yn, d+1))
                    if waters[xn][yn] and waters[xn][yn] < size:
                        if nearby and nearby[0][0] < d+1:
                            return heapq.heappop(nearby)
                        heapq.heappush(nearby, (d+1, xn, yn))
    if nearby:
        return heapq.heappop(nearby)
    return 0, 0, 0

for i in range(N):
    for j in range(N):
        if waters[i][j] == 9:
            sharkX, sharkY = i, j
            waters[i][j] = 0

eat = 0
time = 0
while 1:
    move = deque()
    move.append((sharkX, sharkY, 0))
    visited = [[0 for _ in range(N)] for _ in range(N)]
    dist, sharkX, sharkY = bfs(sharkX, sharkY)
    waters[sharkX][sharkY] = 0
    if not dist:
        break
    time += dist
    eat += 1
    if eat == size:
        size += 1
        eat = 0
print(time)

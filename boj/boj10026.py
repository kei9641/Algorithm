from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N = int(input())
picture = [list(input()) for _ in range(N)]

def isPicture(x, y):
    return (0 <= x < N) and (0 <= y < N)

def isBlue(color):
    return color == 'B'

def bfs(x, y, t):
    deq = deque()
    deq.append((x, y))
    
    while deq:
        x, y = deq.popleft()
        currentColor = picture[x][y]

        for n in range(4):
            xn, yn = x + dx[n], y + dy[n]
            if isPicture(xn, yn) and visited[t][xn][yn] == 0:
                color = picture[xn][yn]
                if t == 0 and color == currentColor:
                    visited[t][xn][yn] = 1
                    deq.append((xn, yn))
                elif t == 1 and isBlue(color) == isBlue(currentColor):
                    visited[t][xn][yn] = 1
                    deq.append((xn, yn))

count = [0, 0]
visited = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(2)]

for x in range(N):
    for y in range(N):
        if not visited[0][x][y]:
            count[0] += 1
            visited[0][x][y] = 1
            bfs(x, y, 0)
        if not visited[1][x][y]:
            count[1] += 1
            visited[1][x][y] = 1
            bfs(x, y, 1)

print(*count)
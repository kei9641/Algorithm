from collections import deque

N = int(input())
area = []
for _ in range(N):
    area.append(list(map(int, input().split())))

height = 1
max_cnt = 1
deq = deque()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def isNotWall(x, y):
    return (0 <= x < N) and (0 <= y < N)

def bfs(x0, y0, visited):
    deq.append((x0, y0))
    visited[x0][y0] = -1

    while deq:
        x, y = deq.popleft()
        for n in range(4):
            xn, yn = x + dx[n], y + dy[n]
            if isNotWall(xn, yn) and visited[xn][yn] == 0:
                visited[xn][yn] = -1
                deq.append((xn, yn))

while height <= 100:   
    savezone = 0
    visited = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if area[i][j] <= height:
                visited[i][j] = height
    
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                savezone += 1 
                bfs(i, j, visited)

    max_cnt = max(max_cnt, savezone)
    height += 1

    if not savezone:
        break

print(max_cnt)
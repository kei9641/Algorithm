from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

pos = deque()
pos.append((0, 0))

mirror = []
N, M = map(int, input().split())
for _ in range(N):
    mirror.append(list(map(int, input())))

visited = [[0 for _ in range(M)] for _ in range(N)]
visited[0][0] = 1

def isNotWall(x, y):
    if 0 <= x < N and 0 <= y < M:
        return True
    return False

while pos:
    x, y = pos.popleft()
    for n in range(4):
        xn, yn = x + dx[n], y + dy[n]
        if isNotWall(xn, yn) and mirror[xn][yn]:
            if not visited[xn][yn]:
                visited[xn][yn] = visited[x][y] + 1
                pos.append((xn, yn))

print(visited[-1][-1])
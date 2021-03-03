from collections import deque
from copy import deepcopy

M, N = map(int, input().split())
boxes = []
for _ in range(N):
    boxes.append(list(map(int, input().split())))

day = 1
spread = deque()
done = deepcopy(boxes)
for i in range(N):
    for j in range(M):
        if boxes[i][j]:
            done[i][j] = boxes[i][j]
            if boxes[i][j] == 1:
                spread.append((i, j))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
while spread:
    x, y = spread.popleft()
    for n in range(4):
        xn = x + dx[n]
        yn = y + dy[n]
        if (0 <= xn < N) and (0 <= yn < M):
            if not done[xn][yn]:
                spread.append((xn, yn))
                done[xn][yn] = done[x][y] + 1
                if day < done[xn][yn]:
                    day = done[xn][yn]

def tomato():
    for i in range(N):
        for j in range(M):
            if not done[i][j]:
                return -1
    return day-1

print(tomato())
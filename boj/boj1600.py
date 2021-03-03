from collections import deque

dx = [-1, 0, 1, 0, -2, -2, -1, 1, 2, 2, -1, 1]
dy = [0, -1, 0, 1, -1, 1, -2, -2, -1, 1, 2, 2]

K = int(input())
W, H = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(H)]
visited = [[[0 for _ in range(W)] for _ in range(H)] for _ in range(K+1)]

move = deque()
move.append([0, 0, 0])

def isNotWall(x, y):
    return (0 <= x < H) and (0 <= y < W)

def step():
    while move:
        x, y, likeH = move.popleft()

        if x == H-1 and y == W-1:
            return visited[likeH][x][y]

        for n in range(12):
            xn, yn = x + dx[n], y + dy[n]
            if isNotWall(xn, yn):
                if n < 4:
                    if visited[likeH][xn][yn] == 0 and ground[xn][yn] == 0:
                        visited[likeH][xn][yn] = visited[likeH][x][y] + 1
                        move.append([xn, yn, likeH])
                elif likeH < K:
                    if visited[likeH+1][xn][yn] == 0 and ground[xn][yn] == 0:
                        visited[likeH+1][xn][yn] = visited[likeH][x][y] + 1
                        move.append([xn, yn, likeH+1])
    return -1

print(step())

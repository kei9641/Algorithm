from collections import deque

matrix = []
N = int(input())
connect = [[0 for _ in range(N)] for _ in range(N)]

for _ in range(N):
    matrix.append(list(map(int, input().split())))

def bfs(start, end):
    while move:
        node = move.popleft()
        for v in range(N):
            if matrix[node][v] and visited[v] == 0:
                if v == end:
                    return 1
                visited[v] = 1
                move.append(v)
    return 0

for i in range(N):
    for j in range(N):
        if matrix[i][j] == 0:
            move = deque()
            move.append(i)
            
            visited = [0 for _ in range(N)]
            
            connect[i][j] = bfs(i, j)
        else:
            connect[i][j] = 1
        
for k in range(N):
    print(*connect[k])
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
route = [[0, 1, 4, 5, 8, 9, 12, 13], [0, 1, 2, 3, 4, 5, 6, 7], [0, 2, 4, 6, 8, 10, 12, 14], [0, 1, 2, 3, 8, 9, 10, 11]]
area = 0

def isNotWall(x, y):
    return (0 <= x < m) and (0 <= y < n)

def dfs(x, y):
    global area
    room[x][y] = idx
    area += 1
    for n in range(4):
        if isNotWall(x+dx[n], y+dy[n]):
            if castle[x][y] in route[n]:
                if room[x+dx[n]][y+dy[n]] == 0:
                    dfs(x+dx[n], y+dy[n])
            elif room[x+dx[n]][y+dy[n]]:
                if room[x+dx[n]][y+dy[n]] != room[x][y]:
                    if (room[x+dx[n]][y+dy[n]], room[x][y]) not in connects:
                        connects.append((room[x+dx[n]][y+dy[n]], room[x][y]))

n, m = map(int, input().split())
castle = [list(map(int, input().split())) for _ in range(m)]
room = [[0 for _ in range(n)] for _ in range(m)]
size = [0]
connects = []
extends = []
idx = 1
for x in range(m):
    for y in range(n):
        if room[x][y] == 0:
            area = 0
            dfs(x, y)
            size.append(area)
            idx += 1

for connet in connects:
    n1, n2 = connet
    extend = size[n1] + size[n2]
    if extend not in extends:
        extends.append(extend)
        
print(idx-1)
print(max(size))
print(max(extends))
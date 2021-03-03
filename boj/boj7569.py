from collections import deque

dx = [0, 0, 0, 0, -1, 1]
dy = [0, 0, -1, 1, 0, 0]
dz = [-1, 1, 0, 0, 0, 0]

def inBox(x, y, z):
    if 0 <= x < N and 0 <= y < M and 0 <= z < H:
        return True
    return False

def diffusion():
    global ripe

    while tomato:
        x, y, z = tomato.popleft()
        for n in range(6):
            xn, yn, zn = x + dx[n], y + dy[n], z + dz[n]
            if inBox(xn, yn, zn):
                if warehouse[zn][xn][yn] == 0:
                    day = warehouse[z][x][y] + 1
                    warehouse[zn][xn][yn] = day
                    tomato.append((xn, yn, zn))
                    if day > ripe:
                        ripe = day


def complete():
    for z in range(H):
        for x in range(N):
            for y in range(M):
                if warehouse[z][x][y] == 0:
                    return False
    return True

ripe = 1
tomato = deque()
warehouse = []
M, N, H = map(int, input().split())
for _ in range(H):
    floor = []
    for _ in range(N):
        floor.append(list(map(int, input().split())))
    warehouse.append(floor)

for z in range(H):
    for x in range(N):
        for y in range(M):
            if warehouse[z][x][y] == 1:
                tomato.append((x, y, z))
diffusion()

if complete():
    print(ripe - 1)
else:
    print(-1)
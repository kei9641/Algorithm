from collections import deque

dx, dy = [-1, 1, 0, 0],[0, 0, -1, 1]

def isNotWall(x, y):
    return (0 <= x < R) and (0 <= y < C)

R, C = map(int,input().split())
forest = list(input() for _ in range(R))
water = [[-1]*C for _ in range(R)]
visited = [[-1]*C for _ in range(R)]
q = deque()

# 초기 위치 저장
for x in range(R):
    for y in range(C):
        if forest[x][y] == '*':
            # 물부터,, 
            q.append((x, y))
            water[x][y] = 0
        # 고슴도치 출발
        elif forest[x][y] == 'S':
            Sx, Sy = x, y
        # 비버네 집
        elif forest[x][y] == 'D':
            Ex, Ey = x, y

# 물이 퍼지는 것을 체크
while q:
    x, y = q.popleft()
    for n in range(4):
        if isNotWall(x+dx[n], y+dy[n]):
            # 돌도 아니고 비버 집도 아니면
            if forest[x+dx[n]][y+dy[n]] not in 'DX':
                # 방문하지 않았다면
                if water[x+dx[n]][y+dy[n]] == -1:
                    water[x+dx[n]][y+dy[n]] = water[x][y] + 1
                    q.append((x+dx[n], y+dy[n]))

q.append((Sx, Sy))
visited[Sx][Sy]=0

# 고슴도치 이동을 체크
while q:
    x, y = q.popleft()
    for n in range(4):
        if isNotWall(x+dx[n], y+dy[n]):
            # 돌도 아니고 물도 아니면
            if forest[x+dx[n]][y+dy[n]] not in '*X':
                # 방문하지 않았다면
                if visited[x+dx[n]][y+dy[n]] == -1:
                    # 물이 퍼지지 않거나 고슴도치보다 늦게 퍼진다면
                    if water[x+dx[n]][y+dy[n]] == -1 or visited[x][y] + 1 < water[x+dx[n]][y+dy[n]]:
                        visited[x+dx[n]][y+dy[n]] = visited[x][y] + 1
                        q.append((x+dx[n], y+dy[n]))
    
# 도착했다면
if visited[Ex][Ey] == -1:
    print('KAKTUS')
else:
    print(visited[Ex][Ey])
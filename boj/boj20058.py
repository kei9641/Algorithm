import copy
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N, Q = map(int, input().split())
A = []
for _ in range(2**N):
    A.append(list(map(int, input().split())))
L = list(map(int, input().split()))

for i in range(len(L)):
    B = [[0 for _ in range(2**N)] for _ in range(2**N)]
    
    # 90도 돌리기
    size = 2**L[i]
    sX, sY, eX, eY = 0, 0, size, size
    while sX < 2**N:
        bX, bY = sX, sY
        for aX in range(eX-1, sX-1, -1):
            for aY in range(sY, eY):
                B[bX][bY] = A[aX][aY]
                bX += 1
                if bX == eX:
                    bX = sX
                    bY += 1
        sY += size
        if sY >= 2**N:
            sY, eY = 0, size
            sX += size
            eX += size
        else:
            eY += size
    
    # 얼음녹이기
    melt = []
    for x in range(2**N):
        for y in range(2**N):
            neighbor = 0
            if B[x][y]:
                for n in range(4):
                    xn = x + dx[n]
                    yn = y + dy[n]
                    if 0 <= xn < 2**N and 0 <= yn < 2**N:
                        if B[xn][yn]:
                            neighbor += 1
                if neighbor < 3:
                    melt.append((x, y))

    for xm, ym in melt:        
        B[xm][ym] -= 1

    # 덩어리 만들기 & 얼음세기
    ice = 0
    num = 1
    chunk = 0
    check = deque()
    visited = [[0 for _ in range(2**N)] for _ in range(2**N)]
    for x in range(2**N):
        for y in range(2**N):
            ice += B[x][y]
            if visited[x][y] == 0 and B[x][y]:
                cnt = 0
                check.append((x, y))
                visited[x][y] = num
                while check:
                    x0, y0 = check.popleft()
                    cnt += 1
                    for n in range(4):
                        xn = x0 + dx[n]
                        yn = y0 + dy[n]
                        if 0 <= xn < 2**N and 0 <= yn < 2**N:
                            if visited[xn][yn] == 0 and B[xn][yn]:
                                check.append((xn, yn))
                                visited[xn][yn] = num
                if cnt > chunk:
                    chunk = cnt
                num += 1

    # 복사 B -> A & B 리셋
    A = copy.deepcopy(B)
    
print(ice)
print(chunk)
  
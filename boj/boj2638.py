import sys
sys.setrecursionlimit(100000)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def isNotWall(x, y):
    return (0 <= x < N) and (0 <= y < M)

# 외부 공기 체크
def inout(x, y):
    cheese[x][y] = -1
    for i in range(4):
        if isNotWall(x+dx[i], y+dy[i]):
            # 외부 공기 사방에 치즈가 있으면 접촉 횟수만큼 증가
            if cheese[x+dx[i]][y+dy[i]] > 0:
                cheese[x+dx[i]][y+dy[i]] += 1
            # 외부 공기이면 dfs 계속
            elif cheese[x+dx[i]][y+dy[i]] == 0:
                inout(x+dx[i], y+dy[i])

# 남은 치즈 체크
def meltCnt():
    cnt = 0
    for i in range(N):
        for j in range(M):
            # 치즈면 cnt 증가
            if cheese[i][j] == 1 or cheese[i][j] == 2:
                cheese[i][j] = 1
                cnt += 1
            else:
                cheese[i][j] = 0
    return cnt

N, M = map(int, input().split())
cheese = []
for _ in range(N):
    cheese.append(list(map(int, input().split())))

hour = 0
# 남은 치즈가 있으면 반복
while meltCnt():
    inout(0, 0)
    hour += 1

print(hour)
# 선언
pos = []

# 입력
N = int(input())
for _ in range(N):
    x, y = map(int, input().split())
    pos.append((x, y))

# 정렬
result = sorted(pos, key=lambda x: (x[1], x[0]))

# 출력
for i in range(N):
    print(*result[i])
# 선언
location = []

# 입력
N = int(input())
for _ in range(N):
    x, y = map(int, input().split())

    # 정렬
    location.append((x, y))
location = sorted(location)

# 출력
for i in range(N):
    x, y = location[i]
    print(x, y)
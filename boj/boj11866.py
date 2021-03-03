# 입력
N, K = map(int, input().split())

# 선언
circle = [0 for _ in range(N)]
Josephus = []
index = -1

# 모든 사람이 제거될 때까지 반복
while circle != [1 for _ in range(N)]:
    n = 0 
    # 제거되지 않은 사람들 중 K번째 제거
    while n < K:
        index += 1
        if index >= N:
            index -= N
        if not circle[index]:
            n += 1
    circle[index] = 1
    Josephus.append(index+1)

# 출력
print('<', end="")
for i in range(N-1):
    print(Josephus[i], end=", ")
print(Josephus[-1], end="")
print('>')

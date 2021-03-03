#  선언
ground = []
heightCnt = dict()
H, T = 257, 65000000

# 입력
N, M, B = map(int, input().split())
for _ in range(N):
    ground += list(map(int, input().split()))

# 같은 높이의 땅 카운트
A = N * M
for n in range(A):
    if ground[n] in heightCnt:
        heightCnt[ground[n]] += 1
    else:
        heightCnt[ground[n]] = 1

# 땅 고르기
for maxHeight in range(min(heightCnt), 257):
    block = B
    time = 0
    for key, val in heightCnt.items():
        if key > maxHeight:
            time += 2 * (key - maxHeight) * val
            block += (key - maxHeight) * val
        else:
            time += (maxHeight - key) * val
            block -= (maxHeight - key) * val
    # 최소값 저장
    if block >= 0:
        if time < T:
            H, T = maxHeight, time
        elif time == T:
            H = maxHeight
    else:
        break

# 출력
print(T, H)
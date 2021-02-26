# 입력
N = int(input())

# 선언
roomEnd = 1
passby = 1

# 지나간 방 수 계산
while N > roomEnd:
    passby += 1
    roomEnd += 6 * (passby-1)

# 출력
print(passby)
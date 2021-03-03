# 입력
Id = list(map(int, input().split()))

# 선언
keyNum = 0

# 검증 수 계산
for num in Id:
    keyNum += num**2
keyNum %= 10

# 출력
print(keyNum)
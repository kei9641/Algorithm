# 입력
rhythm = list(map(int, input().split()))

# 올라가는 음인 경우
if rhythm[1] - rhythm[0] > 0:
    scale = 'ascending'
# 내려가는 음인 경우
else:
    scale = 'descending'

# 음계 확인
firstNote = rhythm[0]
for index in range(1, len(rhythm)):
    # 차례대로 연주되지 않았을 경우
    if abs(firstNote - rhythm[index]) != 1:
        scale = 'mixed'
        break
    firstNote = rhythm[index]
# 출력
print(scale)
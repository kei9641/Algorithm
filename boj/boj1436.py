# 입력
N = int(input())

# 선언
title = 665

while N:
    title += 1
    # 종말 숫자인 경우에만 세기
    if '666' in str(title):
        N -= 1

# 출력
print(title)
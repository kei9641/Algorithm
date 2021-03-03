# 입력
A, B, V = map(int, input().split())

# 나무 막대 오르기
day = (V - A) / (A - B) + 1
if day == int(day):
    day = int(day)
else:
    day = int(day) + 1

# 출력
print(day)

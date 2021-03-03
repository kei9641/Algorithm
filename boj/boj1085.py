# 입력
x, y, w, h = map(int, input().split())

# 가로 세로 중 더 적은 값
if x >= y:
    distance = y
else:
    distance = x

# 가장 적은 거리 찾기
if distance > w-x:
    distance = w-x
if distance > h-y:
    distance = h-y

# 출력
print(distance)
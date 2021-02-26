# 선언
number = []
maxNum = 0
maxIdx = 0

# 입력
for _ in range(9):
    number.append(int(input()))

# 큰 수 찾기
for index in range(len(number)):
    if maxNum < number[index]:
        maxNum = number[index]
        maxIdx = index

# 출력
print(maxNum)
print(maxIdx+1)
# 입력
A = int(input())
B = int(input())
C = int(input())

# 선언
numCnt = [0] * 10

# 계산
number = str(A*B*C)
# 숫자 카운트
for num in number:
    numCnt[int(num)] += 1

# 출력
for i in numCnt:
    print(i)

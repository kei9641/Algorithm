import sys

# 선언
numbers = [0] * 10001

# 입력
N = int(input())
for _ in range(N):
    num = int(sys.stdin.readline())
    numbers[num] += 1

# 출력
for i in range(10001):
    if numbers[i]:
        for _ in range(numbers[i]):
            print(i)
# 선언
arr = []

# 입력
N, X = map(int, input().split())
A = list(map(int, input().split()))

# X보다 작은 수 구하기
for num in A:
    if num < X:
        arr.append(num)

# 출력
print(*arr)

# 입력
M, N = map(int, input().split())

# 선언
primeNum = []
sieve = [True for _ in range(N+1)]

# 소수 찾기
for i in range(2, int((N+1)**0.5)+1):
    if sieve[i]:
        for j in range(i+i, N+1, i):
            sieve[j] = False

# 출력
for idx in range(M, N+1):
    if idx > 1 and sieve[idx]:
        print(idx)
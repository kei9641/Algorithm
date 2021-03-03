# 선언
binomial = 1

# 입력
N, K = map(int, input().split())

# 이항계수 계산
for n in range(K):
    binomial *= (N-n)/(n+1)

# 출력
print(int(binomial))
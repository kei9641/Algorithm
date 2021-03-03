memo = [0, 1, 1]

def dp(n):
    for _ in range(n-2):
        memo.append(memo[-2] + memo[-3])
    
    return memo[n]

T = int(input())
for _ in range(T):
    N = int(input())
    print(dp(N))
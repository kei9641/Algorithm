N = int(input())
dp = [0 for _ in range(N+1)]

for i in range(N+1):
    if i <= 3:
        dp[i] = i
    else:
        dp[i] = dp[i-2] + dp[i-1]

print(dp[N] % 10007)
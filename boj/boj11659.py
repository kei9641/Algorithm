import sys

N, M = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

sums = [nums[0]]
for i in range(1, N):
    sums.append(sums[i-1] + nums[i])

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    if (i == 1):
        print(sums[j-1])
    else:
        print(sums[j-1] - sums[i-2])

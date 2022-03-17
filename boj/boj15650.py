from itertools import combinations

N, M = map(int, input().split())
nums = list(range(1, N+1))
combinationList = list(combinations(nums, M))
for i in range(len(combinationList)):
    print(*combinationList[i])
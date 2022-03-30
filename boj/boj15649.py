from itertools import permutations
N, M = map(int, input().split())

nums = list(range(1, N + 1))
permuteList = list(permutations(nums, M))

for permute in permuteList:
    print(*permute)
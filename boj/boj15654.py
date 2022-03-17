from itertools import permutations

N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

permuList = list(permutations(nums, M))

for n in permuList:
    print(*n)
N, M = map(int, input().split())
extract = list(map(int, input().split()))
nums = list(range(1, N+1))
operation = 0

for num in extract:
    i = 0
    while 1:
        if num == nums[i]:
            nums = nums[i+1:] + nums[:i+1]
            operation += i
            break
        elif num == nums[-(i+1)]:
            nums = nums[-i:] + nums[:-i]
            operation += i+1
            break
        i += 1
    nums.pop()

print(operation)
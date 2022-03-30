N = int(input())

nums = [0, 1, 2]

for i in range(3, N + 1):
    nums.append((nums[i-1] + nums[i-2]) % 15746)

print(nums[N])
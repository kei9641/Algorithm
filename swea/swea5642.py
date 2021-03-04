T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    
    total = nums[0]
    for i in range(N-1):
        if nums[i] >= 0 and nums[i] + nums[i+1] >= 0:
            nums[i+1] += nums[i]
        total = max(total, nums[i+1])

    print('#{} {}'.format(tc, total))

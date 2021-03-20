H, W = map(int, input().split())
height = list(map(int, input().split()))

amount = 0
left, right = 0, W - 1
left_max, right_max = height[left], height[right]

while left < right:
    left_max = max(left_max, height[left])
    right_max = max(right_max, height[right])

    if left_max <= right_max:
        amount += left_max - height[left]
        left += 1
    else:
        amount += right_max - height[right]
        right -= 1

print(amount)
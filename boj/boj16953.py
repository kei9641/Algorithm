from collections import deque

A, B = map(int, input().split())

result = -1
nums = deque([(A, 1)])
while nums:
    n, cnt = nums.popleft()

    if n == B:
        result = cnt
        break
    
    pushOne = int(str(n) + '1')
    if pushOne <= B:
        nums.append((pushOne, cnt + 1))
    
    doubleNum = n * 2
    if doubleNum <= B:
        nums.append((doubleNum, cnt + 1))

print(result)

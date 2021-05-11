from collections import deque

stack = []
queue = deque()
N = int(input())
numbers = list(map(int, input().split()))
queue.extend(numbers)
num = 1

while num <= N:
    if queue and queue[0] == num:
        queue.popleft()
        num += 1
    else:
        if stack and stack[-1] == num:
            stack.pop()
            num += 1
        elif queue:
            stack.append(queue.popleft())
        else:
            break

if queue or stack:
    print("Sad")
else:
    print("Nice")
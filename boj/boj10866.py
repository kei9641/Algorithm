import sys
from collections import deque

# 선언
deque = deque()

# 입력
N = int(input())
for _ in range(N):
    command = list(sys.stdin.readline().split())

    # 명령 실행
    if command[0] == "push_front":
        deque.appendleft(command[1])
    elif command[0] == "push_back":
        deque.append(command[1])
    elif command[0] == "pop_front":
        if deque:
            print(deque.popleft())
        else:
            print(-1)
    elif command[0] == "pop_back":
        if deque:
            print(deque.pop())
        else:
            print(-1)
    elif command[0] == "size":
        print(len(deque))
    elif command[0] == "empty":
        if deque:
            print(0)
        else:
            print(1)
    elif command[0] == "front":
        if deque:
            print(deque[0])
        else:
            print(-1)
    elif command[0] == "back":
        if deque:
            print(deque[-1])
        else:
            print(-1)
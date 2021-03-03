'''
시간초과시 input() 대신 sys.stdin.readline()
'''

import sys

# 선언
stack = []

# 입력
N = int(input())
for _ in range(N):
    command = list(sys.stdin.readline().split())

    # 명령어 실행
    if command[0] == 'push':
        stack.append(command[1])
    elif command[0] == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif command[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
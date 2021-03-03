from collections import deque

T = int(input())
for _ in range(T):
    register = deque()
    visited = [0 for _ in range(10000)]
    A, B = map(int, input().split())
    register.append([A, ''])
    while register:
        number, commend = register.popleft()

        if number == B:
            print(commend)
            break
        
        D = (number * 2) % 10000
        if not visited[D]:
            visited[D] = 1
            register.append([D, commend + 'D'])
        
        S = number - 1 if number != 0 else 9999
        if not visited[S]:
            visited[S] = 1
            register.append([S, commend + 'S'])
        
        L = (number % 1000) * 10 + (number // 1000)
        if not visited[L]:
            visited[L] = 1
            register.append([L, commend + 'L'])
        
        R = (number % 10) * 1000 + (number // 10)
        if not visited[R]:
            visited[R] = 1
            register.append([R, commend + 'R'])

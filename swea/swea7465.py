from collections import defaultdict, deque

def bfs(i):
    deq = deque()
    deq.append(i)
    checked[i] = 1
    while deq:
        node = deq.popleft()
        for v in connect[node]:
            if not checked[v]:
                checked[v] = 1
                deq.append(v)

T = int(input())
for tc in range(1, T+1):
    connect = defaultdict(list)

    N, M = map(int, input().split())
    for _ in range(M):
        people, friend = map(int, input().split())
        connect[people].append(friend)
        connect[friend].append(people)
    
    group = 0
    checked = [0 for _ in range(N+1)]
    for i in range(1, N+1):
        if not checked[i]:
            group += 1
            bfs(i)

    print('#{} {}'.format(tc, group))
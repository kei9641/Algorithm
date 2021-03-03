from collections import defaultdict, deque

friends = defaultdict(list)
N, M = map(int, input().split())
for _ in range(M):
    A, B = map(int, input().split())
    friends[A].append(B)
    friends[B].append(A)

bacon = [[0 for _ in range(N+2)] for _ in range(N+1)]
for i in range(1, N+1):
    relation = deque()
    relation.append((i, 0))

    while relation:
        friend = relation.popleft()
        for n in friends[friend[0]]:
            if n != i and bacon[i][n] == 0:
                connect = friend[1] + 1
                relation.append((n, connect))
                bacon[i][n] = connect
                bacon[i][-1] += connect

minConnect, bestFriend = 10000, 0
for j in range(1, N+1):
    if minConnect > bacon[j][-1]:
        minConnect = bacon[j][-1]
        bestFriend = j
print(bestFriend)
import sys
from collections import defaultdict

N, M = map(int, sys.stdin.readline().split())
visited = [0 for _ in range(N+1)]
connect = defaultdict(list)
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    connect[u].append(v)
    connect[v].append(u)

def dfs(node):
    visited[node] = 1
    for n in connect[node]:
        if not visited[n]:
            dfs(n)

group = 0
for i in range(1, N+1):
    if not visited[i]:
        group += 1
        dfs(i)

print(group)

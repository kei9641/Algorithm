from collections import defaultdict, deque

N, M, V = map(int, input().split())
visited = [[0, 0] for _ in range(N+1)]
visited[V][1] = 1
graph = defaultdict(list)
resultD, resultB = [], []
deqB = deque()
deqB.append(V)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph.keys():
    graph[i].sort()

def dfs(n):
    visited[n][0] = 1
    resultD.append(n)
    for node in graph[n]:
        if not visited[node][0]:
            dfs(node)

def bfs():
    while deqB:
        n = deqB.popleft()
        resultB.append(n)
        for node in graph[n]:
            if not visited[node][1]:
                deqB.append(node)
                visited[node][1] = 1
dfs(V)
bfs()

print(*resultD)
print(*resultB)
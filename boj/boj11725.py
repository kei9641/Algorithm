from collections import defaultdict, deque

N = int(input())
connect = defaultdict(list)
visited = [0 for _ in range(N+1)]
parrent = [0 for _ in range(N+1)]
search = deque()

for _ in range(N-1):
    a, b = map(int, input().split())
    connect[a].append(b)
    connect[b].append(a)

visited[1] = 1
search.append(1)
while search:
    node = search.popleft()
    for n in connect[node]:
        if visited[n] == 0:
            visited[n] = 1
            parrent[n] = node
            search.append(n)

for i in range(2, N+1):
    print(parrent[i])
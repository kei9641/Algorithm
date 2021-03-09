from collections import defaultdict

max_dist, max_node = 0, 1
connects = defaultdict(list)
V = int(input())
for _ in range(V):
    data = list(map(int, input().split()))
    for i in range(1, len(data)-1, 2):
        connects[data[0]].append((data[i], data[i+1]))

def longest(node, dist):
    global max_dist, max_node
    if max_dist < dist:
        max_dist = dist
        max_node = node

    visited[node-1] = 1
    for n, d in connects[node]:
        if not visited[n-1]:
            longest(n, dist + d)

visited = [0 for _ in range(V+1)]
longest(1, 0)
visited = [0 for _ in range(V+1)]
longest(max_node, 0)
print(max_dist)
from collections import defaultdict
import heapq

pos = []
graph = defaultdict(list)

V, E = map(int, input().split())
K = int(input())
distance = [10**6 for _ in range(V)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

def move():
    while pos:
        dist, node = heapq.heappop(pos)
        if distance[node-1] > dist:
            distance[node-1] = dist
            for n, d in graph[node]:
                heapq.heappush(pos, (dist + d, n))

heapq.heappush(pos, (0, K))
move()

for i in range(V):
    if distance[i] == 10 ** 6:
        print("INF")
    else:
        print(distance[i])
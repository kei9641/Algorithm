import sys
from collections import defaultdict
from heapq import heappop, heappush

INF = sys.maxsize

goParty = defaultdict(list) # 역, X에서
goHome = defaultdict(list) # 정, X에서
N, M, X = map(int, input().split())
for _ in range(M):
    A, B, T = map(int, input().split())
    goParty[B-1].append([T, A-1])
    goHome[A-1].append([T, B-1])
    
def dijkstra(road):
    while heap:
        currentTime, currentPos = heappop(heap)
        for time, pos in road[currentPos]:
            if distParty[pos] > currentTime + time:
                distParty[pos] = currentTime + time
                heappush(heap, [distParty[pos], pos])

spend = [0 for _ in range(N)]

heap = []
heappush(heap, [0, X-1])
distParty = [INF for _ in range(N)]
distParty[X-1] = 0
dijkstra(goParty)
for i in range(N):
    spend[i] += distParty[i]

heap = []
heappush(heap, [0, X-1])
distParty = [INF for _ in range(N)]
distParty[X-1] = 0
dijkstra(goHome)
for i in range(N):
    spend[i] += distParty[i]

print(max(spend))
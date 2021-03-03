import sys
import heapq

heap = []

N = int(sys.stdin.readline())
for _ in range(N):
    x = int(sys.stdin.readline())
    if x:
        heapq.heappush(heap, (abs(x), x))
    elif len(heap):
        print(heapq.heappop(heap)[1])
    else:
        print(0)
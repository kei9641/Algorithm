import sys
import heapq

left, right = [], []
N = int(sys.stdin.readline())
for i in range(1, N+1):
    num = int(sys.stdin.readline())
    if i % 2:
        heapq.heappush(left, -num)
    else:
        heapq.heappush(right, num)
    
    if right and -left[0] > right[0]:
        l, r = -heapq.heappop(left), heapq.heappop(right)
        heapq.heappush(left, -r)
        heapq.heappush(right, l)

    print(-left[0])
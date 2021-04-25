import heapq

dummy = []
N = int(input())
for _ in range(N):
    heapq.heappush(dummy, int(input()))

if len(dummy) == 1:
    print(0)
else:
    cnt = 0
    while len(dummy) > 1:
        A = heapq.heappop(dummy)
        B = heapq.heappop(dummy)
        cnt += A + B
        heapq.heappush(dummy, A + B)

    print(cnt)
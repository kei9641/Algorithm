import heapq

T = int(input())
for tc in range(1, T+1):
    heap = []
    result = []

    N = int(input())
    for _ in range(N):
        command = list(input().split())
        if command[0] == '1':
            heapq.heappush(heap, -(int(command[1])))
        elif len(heap):
            result.append(-heapq.heappop(heap))
        else:
            result.append(-1)
    print('#', end="")
    print(tc, end=" ")
    print(*result)


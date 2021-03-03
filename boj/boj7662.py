import heapq

T = int(input())
for _ in range(T):
    minH, maxH = [], []
    k = int(input())
    contain = [0 for _ in range(k)]
    for i in range(k):
        operation, number = input().split()
        if operation == 'I':
            heapq.heappush(minH, (int(number), i))
            heapq.heappush(maxH, (-int(number), i))
            contain[i] = 1
        elif number == '1':
            while maxH and contain[maxH[0][1]] == 0:
                heapq.heappop(maxH)
            if maxH:
                contain[maxH[0][1]] = 0
                heapq.heappop(maxH)
        else:
            while minH and contain[minH[0][1]] == 0:
                heapq.heappop(minH)
            if minH:
                contain[minH[0][1]] = 0
                heapq.heappop(minH)
            
    while maxH and contain[maxH[0][1]] == 0:
        heapq.heappop(maxH)
    while minH and contain[minH[0][1]] == 0:
        heapq.heappop(minH)

    if minH and maxH:
        print(-maxH[0][0], minH[0][0])
    else:
        print('EMPTY')

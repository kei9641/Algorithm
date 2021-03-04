T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    pizza = list(map(int, input().split()))
    complete = 0
    oven = [0] * (N+1)
    number = 0
    cheese = [0] * (N+1)
    while complete != M-1:
        if oven[0] == 0 and number < M:
            oven[0] = pizza[number]
            cheese[0] = number
            number += 1
        if oven[0] != 0:
            oven[0] //= 2
            if oven[0] == 0:
                complete += 1
        oven.insert(-1, oven.pop(0))
        cheese.insert(-1, cheese.pop(0))
    for i in range(N):
        if oven[i] != 0:
            idx = cheese[i]+1
    
    print('#{} {}'.format(tc, idx))

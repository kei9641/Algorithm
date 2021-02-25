T = int(input())
for _ in range(T):
    x, y = map(int, input().split())
    distance = y - x
    count = 0
    k = 1
    move = 0
    while move < distance:
        count += 1
        move += k
        if count % 2 == 0:
            k += 1
    print(count)
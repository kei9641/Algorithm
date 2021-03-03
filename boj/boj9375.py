from collections import defaultdict

T = int(input())
for _ in range(T):
    clothes = defaultdict(int)
    
    n = int(input())
    for _ in range(n):
        name, kind = input().split()
        clothes[kind] += 1

    count = 1
    for val in clothes.values():
        count *= (val + 1)

    print(count - 1)
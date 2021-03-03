import sys

mySet = set()
M = int(sys.stdin.readline())
for _ in range(M):
    commend = sys.stdin.readline().split()

    if len(commend) == 1:
        if commend[0] == 'all':
            mySet = set(range(1, 21))
        else:
            mySet = set()
        continue

    operation, num = commend[0], int(commend[1])

    if operation == 'add':
        mySet.add(num)

    elif operation == 'remove':
        mySet.discard(num)

    elif operation == 'check':
        print(1 if num in mySet else 0)

    elif operation == 'toggle':
        if num in mySet:
            mySet.discard(num)
        else:
            mySet.add(num)


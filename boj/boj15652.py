N, M = map(int, input().split())

nums = list(range(1, N + 1))
seqNum = []

def scan(num):
    if (len(seqNum) == M):
        print(*seqNum)
        return

    for i in range(num, N + 1):
        seqNum.append(i)
        scan(i)
        seqNum.pop()

scan(1)

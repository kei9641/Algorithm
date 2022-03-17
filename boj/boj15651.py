N, M = map(int, input().split())

permuteList = []

def permute():
    if len(permuteList) == M:
        print(*permuteList)
        return
    
    for n in range(1, N + 1):
        permuteList.append(n)
        permute()
        permuteList.pop()

permute()

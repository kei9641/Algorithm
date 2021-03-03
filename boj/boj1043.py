from collections import defaultdict, deque

N, M = map(int, input().split())
visitPeople = [0 for _ in range(N+1)]
visitParty = [0 for _ in range(M+1)]

check = deque()
check.append(list(map(int, input().split()))[1:])
people, party = defaultdict(list), defaultdict(list)

for n in range(1, M+1):
    party[n] = list(map(int, input().split()))[1:]
    for p in party[n]:
        people[p].append(n)

toggle = True
while check:
    truly = check.popleft()
    temp = []
    for i in truly:
        if toggle:
            if visitPeople[i] == 0:
                visitPeople[i] = 1
                for j in people[i]:
                    if visitParty[j] == 0:
                        temp.append(j)
        else:
            if visitParty[i] == 0:
                visitParty[i] = 1
                for j in party[i]:
                    if visitPeople[j] == 0:
                        temp.append(j)
    if temp:
        check.append(temp)
    toggle = not toggle

print(visitParty.count(0) - 1)
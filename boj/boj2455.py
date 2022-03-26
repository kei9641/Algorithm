maxPeople = 0
currentPeople = 0

for _ in range(4):
    outPeople, inPeople = map(int, input().split())
    currentPeople += inPeople - outPeople

    maxPeople = max(maxPeople, currentPeople)

print(maxPeople)
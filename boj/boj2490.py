yut = ["D", "C", "B", "A", "E"]

for _ in range(3):
    play = list(map(int, input().split()))
    print(yut[sum(play)])
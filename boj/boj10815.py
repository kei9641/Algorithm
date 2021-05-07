from collections import defaultdict

N = int(input())
cards = list(map(int, input().split()))
M = int(input())
find_num = list(map(int, input().split()))
have_cards = defaultdict(bool)
check = [0 for _ in range(M)]

for card in cards:
    have_cards[card] = True

for i in range(M):
    if have_cards[find_num[i]]:
        check[i] = 1
print(*check)
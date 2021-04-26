from collections import deque

N = int(input())
cards = deque()
cards.extend(list(range(1, N+1)))
remove = []

i = 0
while cards:
    card = cards.popleft()
    if i % 2:
        cards.append(card)
    else:
        remove.append(card)
    i += 1
print(*remove)
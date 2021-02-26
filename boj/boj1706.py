R, C = map(int, input().split())
puzzle = [list(input()) for _ in range(R)]

words = []
for x in range(R):
    word = ''
    for y in range(C):
        if puzzle[x][y] == '#':
            if len(word) > 1:
                words.append(word)
            word = ''
            continue
        word += puzzle[x][y]

    if len(word) > 1:
        words.append(word)

for y in range(C):
    word = ''
    for x in range(R):
        if puzzle[x][y] == '#':
            if len(word) > 1:
                words.append(word)
            word = ''
            continue
        word += puzzle[x][y]

    if len(word) > 1:
        words.append(word)

print(sorted(words)[0])

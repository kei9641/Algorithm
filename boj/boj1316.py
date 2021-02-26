N = int(input())
count = 0

for _ in range(N):
    alpha = [0 for _ in range(26)]
    word = input()

    alpha[ord(word[0]) - ord('a')] = 1
    for i in range(1, len(word)):
        if word[i-1] == word[i]:
            continue
        index = ord(word[i]) - ord('a')
        if alpha[index]:
            break
        alpha[index] = 1
    else:
        count += 1

print(count)
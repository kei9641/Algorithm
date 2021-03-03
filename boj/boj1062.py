from sys import stdin

def learn(i, know):
    global maxRead

    if know == K:
        read = 0
        for word in words:
            for s in word:
                if not alphabet[ord(s) - ord('a')]:
                    break
            else:
                read += 1
        maxRead = max(maxRead, read)
        return

    for n in range(i, 26):
        if not alphabet[n]:
            alphabet[n] = 1
            learn(n, know + 1)
            alphabet[n] = 0

words = []
N, K = map(int, stdin.readline().split())
for _ in range(N):
    words.append(set(stdin.readline()[4:-4]))

if K < 5:
    print(0)
else:
    maxRead = 0
    alphabet = [0 for _ in range(26)]
    for alpha in ['a', 'n', 't', 'i', 'c']:
        alphabet[ord(alpha) - ord('a')] = 1

    learn(0, 5)    
    print(maxRead)
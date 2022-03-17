T = int(input())

for _ in range(T):
    sentence = list(input().split())
    
    for i in range(len(sentence)):
        sentence[i] = ''.join(reversed(sentence[i]))

    print(*sentence)
words = input().split(', ')
words.sort()

for i in range(len(words)-1):
    print(words[i], end=', ')
print(words[-1])
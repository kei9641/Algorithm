words = input()
result = ''
for idx in range(len(words)):
    if idx % 2 == 0:
        result += words[idx]
print(result)
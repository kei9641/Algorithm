N = int(input())
files = []
for _ in range(N):
    files.append(input())
length = len(files[0])
pattern = ['?' for _ in range(length)]

for i in range(length):
    word = files[0][i]
    for j in range(1, N):
        if word != files[j][i]:
            break
    else:
        pattern[i] = word

print(''.join(pattern))
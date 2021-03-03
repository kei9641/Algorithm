X = int(input())
count = 0
divide = format(X, 'b')

for stick in divide:
    if stick == '1':
        count += 1

print(count)

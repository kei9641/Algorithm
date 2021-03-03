X = int(input())
start, length = 1, 0

while not start <= X <= start + length:
    length += 1
    start += length

if length % 2:
    numerator, denominator = 1, length + 1
    while start != X:
        numerator += 1
        denominator -= 1
        start += 1
else:
    numerator, denominator = length + 1, 1
    while start != X:
        numerator -= 1
        denominator += 1
        start += 1

print('{}/{}'.format(numerator, denominator))
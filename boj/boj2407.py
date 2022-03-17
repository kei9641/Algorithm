n, m = map(int, input().split())

a, b, c = 1, 1, 1
for i in range(1, n + 1):
    a *= i
    if i <= m:
        b *= i
    if i <= n - m:
        c *= i

print(a // (b * c))
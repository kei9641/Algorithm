N = int(input())
factorial = 1
for n in range(1, N+1):
    factorial *= n

string = str(factorial)
for i in range(1, len(string)+1):
    if string[-i] != '0':
        break

print(i-1)

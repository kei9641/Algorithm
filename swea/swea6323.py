n = int(input())
a = [1, 1]


#idx0 +idx1 = idx2
for i in range(8):
    x = a[i] + a[i+1]
    a.append(x)
print(a)

#1~9
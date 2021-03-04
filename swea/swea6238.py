s1 = list()
for i in range(1, 101):
    if((i%2) != 0):
        s1.append(i)
for i in range(len(s1)-1):
    print("%d" %(s1[i]), end = ", ")
print(s1[-1])
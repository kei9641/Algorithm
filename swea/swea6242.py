student = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
a = 0
b = 0
c = 0
d = 0
for i in range(len(student)):
    if(student[i] == 'A'):
        a = a + 1
    elif(student[i] == 'B'):
        b = b + 1
    elif(student[i] == 'O'):
        c = c + 1
    elif(student[i] == 'AB'):
        d = d + 1

print("{'A': %d, 'O': %d, 'B': %d, 'AB': %d} " %(a, c, b, d)) 
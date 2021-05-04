N = int(input())
students = []

for _ in range(N):
    name, korean, english, math = input().split()
    students.append((-int(korean), int(english), -int(math), name))

students.sort()
for i in range(N):
    print(students[i][3])
from re import M


A, B = map(int, input().split())
C = int(input())

h, m = divmod(C, 60)

B += m
if (B >= 60):
    B -= 60
    h += 1

A += h
if (A >= 24):
    A -= 24

print(A, B)
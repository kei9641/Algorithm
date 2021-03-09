import sys

def mul(a, b):
    if b == 1:
        return A % C
    else:
        half = mul(a, b//2)
        if b % 2 == 0:
            return half ** 2 % C
        else:
            return half ** 2 * a % C

A, B, C = map(int, sys.stdin.readline().split())
print(mul(A, B))
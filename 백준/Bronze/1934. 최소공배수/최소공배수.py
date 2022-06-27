import sys
import math
A = int(input())
for i in range(A):
    a,b = map(int, sys.stdin.readline().split())
    print(int(a*b/math.gcd(a,b)))
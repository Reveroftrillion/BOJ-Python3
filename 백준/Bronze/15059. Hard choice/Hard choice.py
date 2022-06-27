A,B,C = map(int,input().split())
D,E,F = map(int,input().split())
S = 0
if D>A: S+=(D-A)
if E>B: S+=(E-B)
if F>C: S+=(F-C)
print(S)
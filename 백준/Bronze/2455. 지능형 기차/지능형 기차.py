a,b = map(int, input().split())
c,d = map(int, input().split())
e,f = map(int, input().split())
g,h = map(int, input().split())
A = b-c
B = A+d
C = B-e
D = C+f
E = D-g
F = E+h
print(max(A,B,C,D,E,F))
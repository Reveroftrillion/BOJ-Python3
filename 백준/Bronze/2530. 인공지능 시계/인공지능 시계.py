A,B,C = map(int,input().split())
D = int(input())
E = (C+D)%60
F = (C+D)//60
G = (B+F)%60
H = (B+F)//60
I = (A+H)%24
print(I,G,E)
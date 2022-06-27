a,b,c,d = map(int, input().split())
A = abs(c-a)
B = abs(d-b)
print(min(a,b,A,B))
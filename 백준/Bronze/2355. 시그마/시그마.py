a,b = map(int,input().split())
A = min(a,b)
B = max(a,b)
print((B*(B+1)//2)-((A-1)*A//2))
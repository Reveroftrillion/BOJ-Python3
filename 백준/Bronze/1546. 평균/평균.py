A = int(input())
L = list(map(int, input().split()))
M = max(L)
for i in range(A):
    L[i] = L[i]/M*100
print("%.3f" %(sum(L)/A))
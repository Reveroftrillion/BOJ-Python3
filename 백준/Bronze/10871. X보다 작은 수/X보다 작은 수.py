A,B = map(int, input().split())
num = list(map(int, input().split()))
for i in range(A):
    if num[i]<B:
        print(num[i], end=' ')
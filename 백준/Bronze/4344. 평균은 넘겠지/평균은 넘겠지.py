N = int(input())
for i in range(N):
    A = list(map(int, input().split()))
    B = sum(A[1:])/A[0]
    num = 0
    for j in A[1:]:
        if j>B:
            num+=1
    Answer = num/A[0]*100
    print('%.3f'% Answer+'%')
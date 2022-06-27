N = int(input())
for i in range(1,N+1):
    print(" "*(i-1)+"*"*(2*(N-i)+1))
for j in range(N+1,2*N):
    print(" "*(2*N-1-j)+"*"*(2*(j-N)+1))
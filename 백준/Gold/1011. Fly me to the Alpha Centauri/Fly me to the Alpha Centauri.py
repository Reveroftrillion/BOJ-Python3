import sys
readline = sys.stdin.readline

A = int(input())
for i in range(A):
    a,b = map(int, readline().split())
    d = b-a

    i, x, y = 1, 1, 1
    while not d<=x:
        x+=y
        i+=1
        if i%2==0:
            y+=1

    print(i)